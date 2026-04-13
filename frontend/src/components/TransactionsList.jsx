import { useState, useEffect } from "react";
import { getIncome } from "../services/incomeService";
import { getExpense } from "../services/expenseService";
import { getIncomeCategories } from "../services/incomeCategoryService";
import { getExpenseCategories } from "../services/expenseCategoryService";
import { FaArrowUp, FaArrowDown, FaEdit, FaTrash } from "react-icons/fa";
import "../styles/TransactionsList.css";

function TransactionsList() {
  const [income, setIncome] = useState([]);
  const [expense, setExpense] = useState([]);
  const [incomeCategories, setIncomeCategories] = useState([]);
  const [expenseCategories, setExpenseCategories] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const incomeRes = await getIncome();
        const expenseRes = await getExpense();
        const incomeCategoriesRes = await getIncomeCategories();
        const expenseCategoriesRes = await getExpenseCategories();
        setIncome(incomeRes.data);
        setExpense(expenseRes.data);
        setExpenseCategories(expenseCategoriesRes.data);
        setIncomeCategories(incomeCategoriesRes.data);
      } catch (err) {
        console.error("Failed to fetch transactions", err);
      }
    };

    fetchData();
  }, []);

  return (
    <div className="transactions-container">
      {[...income.map((inc) => ({ ...inc, type: "income" })), 
        ...expense.map((exp) => ({ ...exp, type: "expense" }))].map((t) => (
        <div key={t.id} className={`transaction-card ${t.type}`}>
          <div className="icon">
            {t.type === "income" ? (
              <FaArrowUp />
            ) : (
              <FaArrowDown />
            )}
          </div>

          <div className="details">
            <div className="description">{t.name}</div>
            <div className="category-date">
              {t.category || t.category_id || "Category"} &nbsp;&middot;&nbsp;{" "}
              {t.date ? new Date(t.date).toLocaleDateString() : ""}
            </div>
          </div>

          <div className={`amount ${t.type === "income" ? "positive" : "negative"}`}>
            {t.type === "income" ? "+" : "-"}€{t.amount.toFixed(2)}
          </div>

          <div className="actions">
            <FaEdit className="action-icon" />
            <FaTrash className="action-icon" />
          </div>
        </div>
      ))}
    </div>
  );
}

export default TransactionsList;