from sqlalchemy import Boolean, Integer, String, ForeignKey, Text, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base

from datetime import datetime

class Review(Base):
    __tablename__="reviews"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"), nullable=False)
    comment: Mapped[str | None] = mapped_column(nullable=True)
    comment_date: Mapped[datetime] = mapped_column(default=datetime.now())
    grade: Mapped[float] = mapped_column(Float, nullable=False)
    is_active: Mapped[bool] = mapped_column(default=True)

    product = relationship("Product", back_populates="reviews")
    user = relationship("User", back_populates="reviews")
