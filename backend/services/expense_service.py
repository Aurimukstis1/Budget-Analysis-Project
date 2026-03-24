# from datetime import datetime, date
from sqlalchemy.ext.asyncio import AsyncSession

from repositories import ExpenseRepository
from schemas import ExpenseCreate


class ExpenseService:
    @staticmethod
    async def create_expense(db: AsyncSession, payload: ExpenseCreate):
        
        return await ExpenseRepository.create(
                    db=db,
                    expense_data=payload.model_dump()
                )
    # @staticmethod
    # async def create_expense(db: AsyncSession, payload: ExpenseCreate):
    #     if payload.amount is None:
    #         raise HTTPException(status_code = 400, detail = "Amount is required")

    #     if payload.amount <= 0:
    #         raise HTTPException(status_code = 400, detail = "Amount must be greater than 0")
        
    #     if not payload.name or not payload.strip():
    #         raise HTTPException(status_code = 400, detail = "Name is required")
        
    #     if len(payload.name) > 255:
    #         raise HTTPException(status_code = 400, detail = "Name to long (max 255)")
        
    #     if not payload.category_id:
    #         raise HTTPException(status_code = 400, detail = "Category is required")

    #     expense_data = payload.model_dump()

    #     return await ExpenseRepository.create(
    #         db,
    #         expense_data
    #         )