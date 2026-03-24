from sqlalchemy.ext.asyncio import AsyncSession

from repositories import IncomeRepository
from schemas import IncomeCreate


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