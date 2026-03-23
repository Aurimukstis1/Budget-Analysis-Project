from sqlalchemy.ext.asyncio import AsyncSession


from schemas import ExpenceCreate, ExpenseOut

class ExpenceServices:
    @staticmethod
    async def create_expense(db: AsyncSession, payload: ExpenseCreate):
        return await ExpenseRepository.create(db, payload.model_dump())