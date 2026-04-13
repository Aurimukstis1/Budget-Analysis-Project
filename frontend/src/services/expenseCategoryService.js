import api from "../lib/axios";

export const getExpenseCategories = () => {
  const result = api.get("/expensecategories/");
  return api.get("/expensecategories/");
};