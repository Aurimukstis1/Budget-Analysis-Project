
from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from dependencies import get_db
from schemas import IncomeCreate, IncomeOut
from services import IncomeService

router = APIRouter(prefix="/income", tags=["Income"])


@router.post("", response_model=IncomeOut, status_code=status.HTTP_201_CREATED)
async def create_income(
    payload: IncomeCreate,
    db: AsyncSession = Depends(get_db),
):
    return await IncomeService.create_income(db, payload)