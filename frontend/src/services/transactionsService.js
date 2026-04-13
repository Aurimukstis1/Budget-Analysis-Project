import api from "../lib/axios";

export const getExpense = () => {
  return api.get("/expense/");
};

export const getIncome = () => {
  return api.get("/income/");
};