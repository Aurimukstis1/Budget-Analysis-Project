from sqlalchemy import (
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import Mapped, mapped_column

from database import Base


class User(Base):
    __tablename__ = "users"
    # __table_args__ defines additional table-level configuration
    # __table_args__ = (
    #     # CheckConstraint is fully defined by us: we write the condition and optionally give it a name
    #     CheckConstraint("pages > 0", name="check_book_pages_positive"),
    #     CheckConstraint("price >= 0", name="check_book_price_non_negative"),
    # )

    user_id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    credential_id: Mapped[int] = mapped_column(ForeignKey("credentials.credential_id", ondelete="RESTRICT"), nullable=True, index=True)
    role_id: Mapped[int] = mapped_column(ForeignKey("roles.role_id", ondelete="RESTRICT"), nullable=True, index=True)
    email: Mapped[str] = mapped_column(String(255), nullable=True, index=False)
    username: Mapped[str] = mapped_column(String(255), nullable=True, index=False)
    created_at: Mapped[str] = mapped_column(String(255), nullable=True, index=True)
    updated_at: Mapped[str] = mapped_column(String(255), nullable=True, index=True)

    # categories: Mapped[list["Category"]] = relationship(
    #     secondary=book_category,
    #     back_populates="books",
    # )