import { useEffect, useState } from "react";
import { useForm} from "react-hook-form";
import { createIncome } from "../services/incomeService";
import { getIncomeCategories } from "../services/incomeCategoryService";



function CreateIncome() {
    const {
        register,
        handleSubmit,
        formState: { errors },
        reset
    } = useForm({
        defaultValues: {
            amount: "",
            name: "",
            category_id: "",
        },
    });


    const [categories, setCategories] = useState([]);
    const [serverError, setServerError] = useState("");
    const [successMessage, setSuccessMessage] = useState("");


    useEffect(() => {
        const fetchData = async () => {
            try {
                const categoriesRes = await getIncomeCategories();
                
                setCategories(categoriesRes.data);
            } catch (error) {
                console.error(error);
                setServerError("Failed to load categories");
            }
        };

        fetchData();
    }, []);


    const onSubmit = async (data) => {
        try {
            setServerError("");
            setSuccessMessage("");

            const payload = {
                amount: Number(data.amount),
                name: data.name,
                category_id: Number(data.category_id),
            };

            await createIncome(payload);

            setSuccessMessage("Income added successfully");
            reset();
        } catch (error) {
            console.error(error);
            setServerError("Failed to add income");
        }
    };


    return (
        <div>
            <h1>Add Income</h1>

            {serverError && <p>{serverError}</p>}
            {successMessage && <p>{successMessage}</p>}

            <form onSubmit={handleSubmit(onSubmit)}>
                <div>
                    <label>Name</label>
                    <input
                        type="text"
                        {...register("name", { required: "Name is required" })}
                    />
                    {errors.name && <p>{errors.name.message}</p>}
                </div>

                <div>
                    <label>Amount</label>
                    <input
                        type="number"
                        {...register("amount", {
                            required: "Amount is required",
                            min: { value: 0, message: "Amount must be 0 or more" },
                            max: { value: 1000000, message: "Amount must be 1000000 or less" },
                        })}
                    />
                    {errors.amount && <p>{errors.amount.message}</p>}
                </div>


                <div>
                    <label htmlFor="category_id">Category</label>

                    <select
                        id="category_id"
                        {...register("category_id", {
                            required: "Select a category",
                        })}
                    >
                        <option value="">-- Pasirink kategoriją --</option>

                        {categories.map((category) => (
                            <option key={category.category_id} value={category.category_id}>
                                {category.description}
                            </option>
                        ))}
                    </select>

                    {errors.category_id && <p>{errors.category_id.message}</p>}
                </div>

                <button type="submit">Add Income</button>
            </form>
        </div>
    );
}

export default CreateIncome;