import api from "../lib/axios";

export const createIncome = (incomeData) => {
    return api.post("/income/", incomeData)
};