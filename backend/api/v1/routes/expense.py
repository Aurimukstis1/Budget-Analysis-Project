from typing import Annotated

from fastapi import APIRouter, Depends, Path, status
from sqlalchemy.ext.asyncio import AsyncSession

from dependencies import get_db
from schemas.expense import ExpenseCreate, ExpenseOut, ExpensePut
from services import ExpenseService

router = APIRouter(prefix="/expense", tags=["Expense"])


@router.post("", response_model=ExpenseOut, status_code=status.HTTP_201_CREATED)
async def create_expense(
    payload: ExpenseCreate,
    db: AsyncSession = Depends(get_db),
):
    return await ExpenseService.create_expense(db, payload)


@router.put(
    "/{expense_id}",
    response_model=ExpenseOut,
    status_code=status.HTTP_200_OK,
)
async def update_expense(
    expense_id: Annotated[int, Path(gt=0)],
    payload: ExpensePut,
    db: AsyncSession = Depends(get_db),
):
    return await ExpenseService.update_expense(db, expense_id, payload)
