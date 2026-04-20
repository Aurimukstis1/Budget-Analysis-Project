import { useEffect, useState } from "react";
import "../styles/Transaction.css";
import TransactionsList from "./TransactionsList";
function Transaction() {
  const [sortBy, setSortBy] = useState("date");

  return (
    <>
      <div>
        <div>
          <p>All Transactions</p>
          <p>View and manage all your transactions.</p>
        </div>
        <div className="choice_style">
          <div>
            <ul className="category_transactions">
              <li>
                <a href="">All</a>
              </li>
              <li>
                <a href="">Income</a>
              </li>
              <li>
                <a href="">Expenses</a>
              </li>
            </ul>
          </div>
          <div>
            <label>Sort by: </label>

            <select value={sortBy} onChange={(e) => setSortBy(e.target.value)}>
              <option value="date">Date</option>
              <option value="amount">Amount</option>
            </select>
          </div>
        </div>
        <div>
          
        </div>
        <div className="transaction_list_style">
            <TransactionsList/>
        </div>
      </div>
    </>
  );
}
export default Transaction;
