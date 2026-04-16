from pydantic import BaseModel, ConfigDict
from typing import Optional, Literal
from datetime import date, datetime

class TransactionOut(BaseModel):
    id: int
    type: Literal["income", "expense"]
    date: date
    amount: float
    name: str
    category_id: int
    category_name: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class TransactionListResponse(BaseModel):
    total: int
    page: int
    page_size: int
    data: list[TransactionOut]