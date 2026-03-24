from sqlalchemy.ext.asyncio import AsyncSession

from repositories import ExpenseRepository
from schemas import ExpenseCreate


class ExpenseService:
    @staticmethod
    async def create_expense(db: AsyncSession, payload: ExpenseCreate):
        return await ExpenseRepository.create(db, payload.model_dump())