from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models import Expense, ExpenseCategory

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
    
    async def get_by_id(db: AsyncSession, category_id: int):
        result = await db.execute(
            select(ExpenseCategory).where(
                ExpenseCategory.category_id == category_id
            )
        )
        return result.scalar_one_or_none()
    @staticmethod
    async def get_all(db: AsyncSession) -> list[ExpenseCategory]:
        result = await db.execute(select(ExpenseCategory))
        return result. Scalars().all()