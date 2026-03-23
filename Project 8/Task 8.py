# Tumhare paas employees data hai.
# Har employee ke paas: Name, Age, Salary
# Tumhe ye kaam karna hai:
# 1️⃣ Sirf wahi employees lo jinki age > 25 ho
# 2️⃣ Unki salary me 10% increment lagao
# 3️⃣ Increment ke baad total salary payout calculate karo

from functools import reduce
employees = [
    {"name": "Amit", "age": 24, "salary": 30000},
    {"name": "Neha", "age": 28, "salary": 40000},
    {"name": "Rahul", "age": 32, "salary": 50000},
    {"name": "Pooja", "age": 22, "salary": 28000},
    {"name": "Karan", "age": 29, "salary": 45000}
]
eligible_employees = filter(
    lambda emp: emp["age"] > 25,
    employees
)
updated_salaries = map(
    lambda emp: emp["salary"] * 1.10,
    eligible_employees
)
total_salary = reduce(
    lambda total, salary: total + salary,
    updated_salaries,
    0
)
print("Total Salary after increment:", total_salary)