from sqlalchemy import select, func
from database.session import AsyncSessionLocal
from models import Income, Expense


async def get_stats():
    async with AsyncSessionLocal() as session:

        # Total income
        income_result = await session.execute(
            select(func.sum(Income.amount))
        )
        total_income = income_result.scalar() or 0

        # Total expense
        expense_result = await session.execute(
            select(func.sum(Expense.amount))
        )
        total_expense = expense_result.scalar() or 0

        # Balance
        balance = total_income - total_expense

        return {
            "total_income": total_income,
            "total_expense": total_expense,
            "balance": balance,
        }