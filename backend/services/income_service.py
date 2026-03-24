from sqlalchemy.ext.asyncio import AsyncSession

from repositories import IncomeRepository
from schemas import IncomeCreate, IncomePut


class IncomeService:
    @staticmethod
    async def create_income(db: AsyncSession, payload: IncomeCreate):
        # category = await CategoryRepository.get_by_id(db, payload.category_id)

        # if not category:
        #     raise NotFoundException("Category not found")

        return await IncomeRepository.create(
                    db=db,
                    data=payload.model_dump()
                )
    

    @staticmethod
    async def update_income(
        db: AsyncSession,
        income_id: int,
        payload: IncomePut,
    ):
        try:
            income = await IncomeRepository.get_by_id(db, income_id)

            if not income:
                raise ValueError("Income not found")

            update_data = payload.model_dump(exclude_unset=True)

            for field in ["amount", "name", "category_id"]:
                if field in update_data:
                    setattr(income, field, update_data[field])

            await db.commit()
            await db.refresh(income)

            return income

        except Exception:
            await db.rollback()
            raise
