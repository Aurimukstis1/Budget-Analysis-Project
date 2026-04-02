from typing import Annotated

from fastapi import APIRouter, Depends, Path, status
from sqlalchemy.ext.asyncio import AsyncSession

from dependencies import get_db
from schemas import IncomeCreate, IncomeOut, IncomePut
from services import IncomeService

router = APIRouter(prefix="/income", tags=["Income"])


@router.post("", response_model=IncomeOut, status_code=status.HTTP_201_CREATED)
async def create_income(
    payload: IncomeCreate,
    db: AsyncSession = Depends(get_db),
):
    return await IncomeService.create_income(db, payload)


@router.put(
    "/{income_id}",
    response_model=IncomeOut,
    status_code=status.HTTP_200_OK,
)
async def update_income(
    income_id: Annotated[int, Path(gt=0)],
    payload: IncomePut,
    db: AsyncSession = Depends(get_db),
):
    return await IncomeService.update_income(db, income_id, payload)


@router.delete("/{income_id}")
async def delete_income(
    income_id: Annotated[int, Path(gt=0)],
    db: AsyncSession = Depends(get_db),
):
    await IncomeService.delete_income(db, income_id)
    return {"message": "Income deleted successfully"}
