import asyncio
from sqlalchemy import select
from database.session import AsyncSessionLocal

from models import Income, IncomeCategory


async def seed_data() -> None:
    async with AsyncSessionLocal() as session:

        # =====================
        # CATEGORIES
        # =====================
        categories_data = [
            {"category": "Salary", "description": "Monthly salary"},
            {"category": "Freelance", "description": "Freelance income"},
            {"category": "Investments", "description": "Dividends, stocks"},
        ]

        category_objects = {}

        for cat_data in categories_data:
            result = await session.execute(
                select(IncomeCategory).where(
                    IncomeCategory.category == cat_data["category"]
                )
            )
            category = result.scalar_one_or_none()

            if category is None:
                category = IncomeCategory(
                    category=cat_data["category"],
                    description=cat_data["description"],
                    created_at="2026-01-01",
                    updated_at="2026-01-01",
                )
                session.add(category)
                await session.flush()

            category_objects[cat_data["category"]] = category

        # =====================
        # INCOME
        # =====================
        incomes_data = [
            {
                "name": "Main Job Salary",
                "amount": 2500.0,
                "category": "Salary",
            },
            {
                "name": "Side Freelance Project",
                "amount": 800.0,
                "category": "Freelance",
            },
            {
                "name": "Stock Dividends",
                "amount": 200.0,
                "category": "Investments",
            },
        ]

        for inc_data in incomes_data:
            result = await session.execute(
                select(Income).where(Income.name == inc_data["name"])
            )
            income = result.scalar_one_or_none()

            category = category_objects[inc_data["category"]]

            if income is None:
                income = Income(
                    name=inc_data["name"],
                    amount=inc_data["amount"],
                    category_id=category.category_id,
                    created_at="2026-01-01",
                    updated_at="2026-01-01",
                )
                session.add(income)
            else:
                # jei yra, atnaujinam kategoriją (optional)
                income.category_id = category.category_id

        await session.commit()
        print("Seed data inserted successfully.")


if __name__ == "__main__":
    asyncio.run(seed_data())