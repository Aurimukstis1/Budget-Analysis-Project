from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models import Income


class IncomeRepository:
    @staticmethod
    async def create(db: AsyncSession, data: dict) -> Income:
        income = Income(**data)
        db.add(income)
        await db.commit()
        await db.refresh(income)
        return income

    @staticmethod
    async def get_by_id(db: AsyncSession, income_id: int) -> Income | None:
        result = await db.execute(select(Income).where(Income.income_id == income_id))
        return result.scalar_one_or_none()
