from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload, joinedload
from sqlalchemy import select, func

from models import expense_category
from schemas import expense

class ExpenseCategory:
    @staticmethod
    async def create(
        db: AsyncSession,
        data: dict,
    ) -> Expence:
        expence = Expence(**data)
        db.add(expence)
        await db.commit()
        await db.refresh(expence)
        return expence

