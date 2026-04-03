import api from "../lib/axios";

export const getIncomeCategories = () => {
  const result = api.get("/incomecategories/");
  return api.get("/incomecategories/");
};