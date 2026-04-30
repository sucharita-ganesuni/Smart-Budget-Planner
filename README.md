  Smart Budget Planner (Greedy vs Dynamic Programming)

 Project Overview

The **Smart Budget Planner** is a web-based application built using **Flask (Python)** that helps users manage their expenses efficiently within a given budget.

This project demonstrates the use of:

* **Greedy Algorithm**
* **Dynamic Programming (Knapsack)**

to optimize expense selection and maximize priority/value.

 Features

* Add total budget
* Add multiple expenses (with cost & priority)
* View total expenses and remaining budget
* Compare:

  * Greedy Optimization
  * Dynamic Programming Optimization
* Demo dataset for algorithm comparison
* Clean and responsive UI



#  Algorithms Used

 🔹 Greedy Algorithm

* Selects items based on highest priority first
* Faster but not always optimal

 🔹 Dynamic Programming (Knapsack)

* Checks all possible combinations
* Guarantees optimal solution


 Greedy vs DP Example

| Item | Cost | Priority |
| ---- | ---- | -------- |
| A    | 10   | 60       |
| B    | 20   | 100      |
| C    | 30   | 120      |
| D    | 40   | 130      |

Budget = 50

* Greedy Result → D + A = 190
* DP Result → B + C = 220 )



 Tech Stack

* Python
* Flask
* HTML
* CSS



 Project Structure


codind_skills/
│
├── app.py
├── greedy.py
├── knapsack.py
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
└── README.md
