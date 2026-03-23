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