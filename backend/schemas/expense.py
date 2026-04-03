from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class ExpenseBase(BaseModel):
    user_id: Optional[int] = None
    amount: float = Field(..., gt=0)
    name: str = Field(..., min_length=1, max_length=255)
    category_id: int

    model_config = ConfigDict(
        str_strip_whitespace=True,
        extra="forbid",
    )


class ExpenseCreate(ExpenseBase):
    pass


class ExpensePut(ExpenseBase):
    pass


class ExpenseOut(BaseModel):
    expense_id: int
    user_id: Optional[int]
    amount: float
    name: str
    category_id: int
    created_at: Optional[str]
    updated_at: Optional[str]

    model_config = ConfigDict(from_attributes=True)
