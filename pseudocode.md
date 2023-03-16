# **Budget App**

## **Concept**
- Create a budget application that can run in the terminal.

## **MVP**
- A Category class with the methods:
	- check_funds
	- deposit
	- withdrawal
    - get_balance
    - __str__
    - transfer
- A function to:
    - create_spend_chart

**Write a script that runs in the terminal to simulate the usage of the app, with or without the user as an option.**

## **Requirements:**
- Complete the Category class in category.py
	- Should be able to instantiate objects based on different budget categories.
- When objects are created they are passed in the name of the category only.
- The class should have an instance variable called ledger that is a list
- The class should also contain the following methods:
    - deposit
        - Method that accepts an amount and description
        - If no description is given, it should default to an empty string
        - Method should append an object to the ledger list in the form of:
        - {“amount”: amount, “description”: description}
    - withdrawal
        - Method that is similar to the deposit method, but the amount passed in should be stored in the ledger as a negative number.
        - If there are not enough funds, nothing should be added to the ledger.
        - Method should return True if the withdrawal took place, and False otherwise
    - get_balance
        - Method that returns the current balance of the budget category based on the deposits and withdrawals that have occurred
	- transfer
		- Method that accepts an amount and another budget category as arguments
        - Method should add a withdrawal with the amount and the description “Transfer to [Destination Budget Category]”
        - Method should then add a deposit to the other budget category with the amount and the description “Transfer from [Source Budget Category]”
        - If there are not enough funds, nothing should be added to either ledgers
        - Method should return True if the transfer took place, and False other otherwise
	- check_funds
		- Method that accepts an amount as an argument
        - Returns False if the amount is less than the balance of the budget category and returns True otherwise
        - Method should be used by both the withdrawal method and transfer method

### **When the budget object is printed (__str__method) it should display:**
1. **A title line where the name and category is centered in a line of character**
2. **A list of items in the ledger**
3. **A line displaying the category total**

## **Classes/Methods**

    class Category:
        def __init__(self):
            pass
        def check_funds(self):
            pass
        def deposit(self):
            pass
        def withdrawal(self):
            pass
        def get_balance(self):
            pass
        def __str__(self):
            pass
        def transfer(self):
            pass