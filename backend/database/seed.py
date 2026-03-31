import asyncio
from sqlalchemy import select
from database.session import AsyncSessionLocal

from models import Expense, ExpenseCategory


async def seed_data() -> None:
    async with AsyncSessionLocal() as session:

        # =====================
        # CATEGORIES
        # =====================
        categories_data = [
            {"category": "Food", "description": "Food and groceries"},
            {"category": "Transport", "description": "Public transport, fuel"},
            {"category": "Entertainment", "description": "Movies, games, fun"},
        ]

        category_objects = {}

        for cat_data in categories_data:
            result = await session.execute(
                select(ExpenseCategory).where(
                    ExpenseCategory.category == cat_data["category"]
                )
            )
            category = result.scalar_one_or_none()

            if category is None:
                category = ExpenseCategory(
                    category=cat_data["category"],
                    description=cat_data["description"],
                    created_at="2026-01-01",
                    updated_at="2026-01-01",
                )
                session.add(category)
                await session.flush()

            category_objects[cat_data["category"]] = category

        # =====================
        # EXPENSES
        # =====================
        expenses_data = [
            {
                "name": "Lunch",
                "amount": 15.0,
                "category": "Food",
            },
            {
                "name": "Bus Ticket",
                "amount": 2.5,
                "category": "Transport",
            },
            {
                "name": "Cinema",
                "amount": 12.0,
                "category": "Entertainment",
            },
        ]

        for exp_data in expenses_data:
            result = await session.execute(
                select(Expense).where(Expense.name == exp_data["name"])
            )
            expense = result.scalar_one_or_none()

            category = category_objects[exp_data["category"]]

            if expense is None:
                expense = Expense(
                    name=exp_data["name"],
                    amount=exp_data["amount"],
                    category_id=category.category_id,
                    user_id=None,
                    created_at="2026-01-01",
                    updated_at="2026-01-01",
                )
                session.add(expense)
            else:
                # optional update
                expense.category_id = category.category_id

        await session.commit()
        print("Seed data inserted successfully.")


if __name__ == "__main__":
    asyncio.run(seed_data())