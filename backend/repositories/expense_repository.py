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
