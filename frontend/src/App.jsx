import TransactionForm from "./components/TransactionForm";
import TransactionsList from "./components/TransactionsList";
import Sidebar from "./components/Sidebar"
// import { Routes, Route } from "react-router";

function App() {
  return(
    <>
      <Sidebar/>
      <TransactionForm />
      <TransactionsList />
    </>
  );
}

export default App;
