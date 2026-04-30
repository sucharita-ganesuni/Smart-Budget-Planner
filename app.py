from flask import Flask, render_template, request
from greedy import greedy_budget
from knapsack import knapsack

app = Flask(__name__)

# Global variables
budget = 0
expenses = []
result = []
algo = ""

@app.route("/", methods=["GET", "POST"])
def index():
    global budget, expenses, result, algo

    if request.method == "POST":
        action = request.form.get("action")

        # ADD BUDGET
        if action == "add_budget":
            b = request.form.get("budget")
            if b:
                budget = int(b)

        # ADD EXPENSE
        elif action == "add_expense":
            name = request.form.get("name")
            amount = request.form.get("amount")
            priority = request.form.get("priority")

            if name and amount and priority:
                expenses.append((name, int(amount), int(priority)))

        # GREEDY
        elif action == "greedy":
            algo = "Greedy Optimization"
            result = []   # 🔥 clear old result
            result, _ = greedy_budget(expenses, budget)

        # DP
        elif action == "dp":
            algo = "Dynamic Programming"
            result = []   # 🔥 clear old result
            result, _ = knapsack(expenses, budget)

        # RESET
        elif action == "reset":
            budget = 0
            expenses = []
            result = []
            algo = ""

    # CALCULATIONS
    total_expense = sum(e[1] for e in expenses)
    remaining = budget - total_expense

    return render_template(
        "index.html",
        budget=budget,
        expenses=expenses,
        total_expense=total_expense,
        remaining=remaining,
        result=list(result),   # 🔥 force refresh
        algo=algo
    )

if __name__ == "__main__":
    app.run(debug=False)v
