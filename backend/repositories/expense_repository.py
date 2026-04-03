from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models import Expense

# from schemas import expense


class ExpenseRepository:
    @staticmethod
    async def create(
        db: AsyncSession,
        data: dict,
    ) -> Expense:
        expense = Expense(**data)
        db.add(expense)
        await db.commit()
        await db.refresh(expense)
        return expense

    @staticmethod
    async def get_by_id(db: AsyncSession, expense_id: int) -> Expense | None:
        result = await db.execute(
            select(Expense).where(Expense.expense_id == expense_id)
        )
        return result.scalar_one_or_none()

    @staticmethod
    async def get_by_category(db: AsyncSession, category_id: int) -> list[Expense]:
        result = await db.execute(
            select(Expense).where(Expense.category_id == category_id)
        )
        return result.scalars().all()
    

    @staticmethod
    async def get_all(db: AsyncSession) -> list[Expense]:
        result = await db.execute(select(Expense))
        return result.scalars().all()
