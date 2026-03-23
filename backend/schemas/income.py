from typing import Literal
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field

class IncomeBase(BaseModel):
    user_id: Optional[int] = None
    amount: float = Field(..., gt=0)
    name: str = Field(..., min_length=1, max_length=255)
    category_id: Optional[int] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

    model_config = ConfigDict(
        str_strip_whitespace=True,
        extra="forbid",
    )

class IncomeCreate(IncomeBase):
    pass


class IncomeOut(BaseModel):
    income_id: int
    user_id: int
    amount: float
    name: str
    category_id: int
    created_at: str
    updated_at: str

    model_config = ConfigDict(from_attributes=True)


# class IncomeCreate(BaseModel):
#     amount: float = Field(..., gt=0)
#     name: str = Field(..., min_length=1, max_length=255)
#     category_id: int = Field(..., gt=0)

# class IncomeBase(BaseModel):
#     user_id: int
#     amount: float
#     name: str
#     category_id: int

# class IncomeResponse(IncomeBase):
#     income_id: int
#     created_at: datetime
#     updated_at: datetime