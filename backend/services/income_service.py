from sqlalchemy.ext.asyncio import AsyncSession

from schemas import IncomeCreate
from repositories import IncomeRepository, CategoryRepository

class IncomeService:
    @staticmethod
    async def create_income(db: AsyncSession, payload: IncomeCreate, user_id: int):

        category = await CategoryRepository.get_by_id(db, payload.category_id)

        if not category:
            raise NotFoundException("Category not found")

        income_data = payload.model_dump()

        income_data["user_id"] = user_id

        income = await IncomeRepository.create(
            db=db,
            income_data=data
        )

        return await IncomeRepository.get_by_id(db, income.income_id)