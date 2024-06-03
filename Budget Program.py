# -*- coding: utf-8 -*-
"""
Created on Thu May 23 20:57:50 2024

@author: zohai
"""

def add_expense(expenses, description, amount):
    expenses.append({"description": description, "amount": amount})
    print(f"Added expense: {description}, Amount: {amount}")
    
def get_total_expenses(expenses):
    sum = 0
    for expense in expenses:
        sum += expense["amount"]
    return sum

def get_balance(budget, expenses):
    return budget - get_total_expenses(expenses)
    
def show_budget_details(budget, expenses):
    print(f"Total Budget: {budget}")
    print("Expenses:")
    for expense in expenses:
        print(f"- {expense['description']}: {expense['amount']}")
    print(f"Total Spent: {get_total_expenses(expenses)}")
    print(f"Remaining Budget: {get_balance(budget, expenses)}")
        
    
def main():
    print("Welcome to the Budget Program")
    initial_budget = float(input("Please enter your initial budget: "))
    # filepath = 'budget_data.json' # Define path to your JSON file
    # initial_budget, expenses = load_budget_data(filepath)
    budget = initial_budget
    expenses = [] 
    
    while True:
        print("\nWhat would you like to do?")
        print("1. Add an expense")
        print("2. Show budget details")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == "1":
            description = input("Enter expense description: ")
            amount = float(input("Enter expense amount: "))
            add_expense(expenses, description, amount)
        elif choice == "2":
            show_budget_details(budget, expenses)
        elif choice == "3":
            print("Exiting Budget Program.")
            break
        else:
            print("Invalid choice, please choose again.")
            
if __name__ == "__main__": # to properly run the function
    main()                 # ^ 