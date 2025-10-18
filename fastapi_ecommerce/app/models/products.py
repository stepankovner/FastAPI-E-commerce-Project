from sqlalchemy import String, Boolean, Float, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base
from typing import List

# from app.models.categories import Category


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str | None] = mapped_column(String(500), nullable=True)
    price: Mapped[float] = mapped_column(Float, nullable=False)
    image_url: Mapped[str | None] = mapped_column(String(200), nullable=True)
    stock: Mapped[int] = mapped_column(Integer, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"), nullable=False)
    rating: Mapped[float | None] = mapped_column(Float, default=None, nullable=True) 
    seller_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    seller = relationship("User", back_populates="products")

    category: Mapped["Category"] = relationship(
        "Category",
        back_populates="products"
    )
    reviews: Mapped[List["Review"]] = relationship(
        "Review", 
        back_populates="product", 
        cascade="all, delete-orphan" 
    )