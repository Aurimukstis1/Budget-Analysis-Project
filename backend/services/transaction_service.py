from sqlalchemy.ext.asyncio import AsyncSession

from repositories import IncomeRepository, ExpenseRepository

class TransactionService:
    @staticmethod
    async def get_transactions(db: AsyncSession, transaction_type: str = "all", sort_by: str = "date", page: int = 1,
        page_size: int = 10,):

        incomes = await IncomeRepository.get_all(db)
        expenses = await ExpenseRepository.get_all(db)

        transactions = []

        for income in incomes:
            transactions.append({
                "id": income.income_id,
                "type": "income",
                "amount": income.amount,
                "date": income.date,
                "name": income.name,
                "category_id": income.category_id,
                "category_name": income.category.category if income.category else None,
                "created_at": income.created_at,
                "updated_at": income.updated_at,
            })

        for expense in expenses:
            transactions.append({
                "id": expense.expense_id,
                "type": "expense",
                "amount": expense.amount,
                "date": expense.date,
                "name": expense.name,
                "category_id": expense.category_id,
                "category_name": expense.category.category if expense.category else None,
                "created_at": expense.created_at,
                "updated_at": expense.updated_at,
            })


        if transaction_type != "all":
            transactions = [t for t in transactions if t["type"] == transaction_type]

        if sort_by in ["date", "amount"]:
            transactions.sort(key=lambda x: x[sort_by], reverse=True)

        start = (page - 1) * page_size
        end = start + page_size

        paginated = transactions[start:end]

        return {
            "total": len(transactions),
            "page": page,
            "page_size": page_size,
            "data": paginated,
        }