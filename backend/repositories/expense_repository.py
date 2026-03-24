from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload, joinedload
from sqlalchemy import select, func
 
from models import Expense
# from schemas import expense
 
class ExpenseRepository:
    @staticmethod
    async def create(
        db: AsyncSession,
        data: dict,
    ) -> Expense:
        expence = Expense(**data)
        db.add(expense)
        await db.commit()
        await db.refresh(expense)
        return expense