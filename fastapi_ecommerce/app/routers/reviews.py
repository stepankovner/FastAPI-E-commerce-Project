from fastapi import APIRouter, Depends, HTTPException, status

from sqlalchemy import select, update, func
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.categories import Category as CategoryModel
from app.models.products import Product as ProductModel
from app.models.users import User as UserModel
from app.models.reviews import Review as ReviewModel

from app.schemas import Review as ReviewSchema, ReviewCreate


from app.db_depends import get_async_db
from app.auth import get_current_seller, get_current_user, get_current_buyer, get_current_admin


router = APIRouter(
    prefix="/reviews",
    tags=["reviews"]
)

@router.get("/", response_model=list[ReviewSchema])
async def get_reviews(db: AsyncSession = Depends(get_async_db)):
    result = await db.scalars(select(ReviewModel).where(ReviewModel.is_active == True))
    return result.all()


@router.get("/{product_id}/reviews", response_model=list[ReviewSchema])
async def get_products_reviews(product_id: int, db: AsyncSession = Depends(get_async_db)):
    product_res = await db.scalars(select(ProductModel).where(ProductModel.is_active == True, ProductModel.id == product_id))
    if product_res.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found or inactive")

    result = await db.scalars(select(ReviewModel).where(ReviewModel.is_active == True, ReviewModel.product_id == product_id))
    return result.all()


@router.post("/", response_model=ReviewSchema)
async def post_review(review: ReviewCreate, db: AsyncSession = Depends(get_async_db), current_user: UserModel = Depends(get_current_buyer)):
    product_res = await db.scalars(select(ProductModel).where(ProductModel.is_active == True, ProductModel.id == review.product_id))
    if product_res.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found or inactive")
    
    is_correct_grade = 1 <= review.grade <= 5
    if not is_correct_grade:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_CONTENT, detail="Grade must be in [1, 5]")
    
    db_review = ReviewModel(**review.model_dump(), user_id=current_user.id)

    db.add(db_review)
    

    avg_grade = await db.scalars(select(func.avg(ReviewModel.grade)).where(ReviewModel.is_active == True, ReviewModel.product_id == review.product_id))
    avg_grade_result = avg_grade.first()

    await db.execute(
        update(ProductModel).where(ProductModel.id == review.product_id).values(rating=avg_grade_result)
    )

    await db.commit()
    await db.refresh(db_review)
    return db_review

@router.delete("/{review_id}")
async def delete_review(review_id: int, db: AsyncSession = Depends(get_async_db), current_user: UserModel = Depends(get_current_admin)):
    review_result = await db.scalars(select(ReviewModel).where(ReviewModel.id == review_id, ReviewModel.is_active == True))
    db_review = review_result.first()
    if db_review is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Review not found!")
    
    await db.execute(
        update(ReviewModel).where(ReviewModel.id == review_id).values(is_active=False)
    )

    avg_grade = await db.scalars(select(func.avg(ReviewModel.grade)).where(ReviewModel.is_active == True, ReviewModel.product_id == db_review.product_id))
    avg_grade_result = avg_grade.first()

    await db.execute(
        update(ProductModel).where(ProductModel.id == db_review.product_id).values(rating=avg_grade_result)
    )

    await db.commit()
    return {"message": "Review deleted"}