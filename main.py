import pandas as pd
import matplotlib.pyplot as plt

choice = input("Do you want to add a new expense? (yes/no): ")

if choice.lower() == "yes":

    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category: ")
    amount = int(input("Enter amount: "))

    data = pd.read_csv("expenses.csv")

    new_row = {
        "Date": date,
        "Category": category,
        "Amount": amount
    }

    data.loc[len(data)] = new_row

    data.to_csv("expenses.csv", index=False)

    print("\nNew expense added successfully!\n")

data = pd.read_csv("expenses.csv")

print("\n========== EXPENSE DATA ==========\n")
print(data)

total = data["Amount"].sum()

print("\n=================================")
print("TOTAL EXPENSE =", total)
print("=================================\n")

category_sum = data.groupby("Category")["Amount"].sum()

print("Category Wise Expense:\n")
print(category_sum)

plt.figure(figsize=(7,7))

plt.pie(
    category_sum,
    labels=category_sum.index,
    autopct='%1.1f%%',
    shadow=True
)

plt.title("Expense Distribution")

plt.show()

plt.figure(figsize=(8,5))

bars = plt.bar(
    category_sum.index,
    category_sum.values
)

plt.xlabel("Category")
plt.ylabel("Amount")
plt.title("Category Wise Expenses")

for bar in bars:
    yval = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width()/2,
        yval + 5,
        yval,
        ha='center'
    )

plt.show()
