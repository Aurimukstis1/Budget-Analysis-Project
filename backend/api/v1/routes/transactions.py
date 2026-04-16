from fastapi import APIRouter, Depends, Query
from typing import Annotated, Optional, Literal
from sqlalchemy.ext.asyncio import AsyncSession

from dependencies import get_db
from schemas import TransactionListResponse
from services import TransactionService

router = APIRouter(prefix="/transactions", tags=["Transactions"])

@router.get("", response_model=TransactionListResponse)
async def get_transactions(
    db: AsyncSession = Depends(get_db),
    transaction_type: Annotated[Literal["all", "income", "expense"], Query()] = "all",
    sort_by: Annotated[Optional[Literal["date", "amount"]], Query()] = "date",
    limit: Annotated[int, Query(gt=0, le=100)] = 10,
    offset: Annotated[int, Query(ge=0)] = 0,
):
    return await TransactionService.get_transactions(
        db=db,
        transaction_type=transaction_type,
        sort_by=sort_by,
        page_size=limit,
        page=(offset // limit) + 1,
    )