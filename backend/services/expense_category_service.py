from sqlalchemy.ext.asyncio import AsyncSession
from repositories.expense_repository import ExpenseCategory
from sqlalchemy import select

class ExpenseCategoryService:
    @staticmethod
    async def get_all(db: AsyncSession) -> list[ExpenseCategory]:
        result = await db.execute(select(ExpenseCategory))
        return result. Scalars().all()