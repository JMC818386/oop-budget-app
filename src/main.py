from category import Category

initial_deposit = Category("Initial Deposit")
rent = Category("Rent")
utilities = Category("Utilities")
insurance = Category("Insurance")
food = Category("Food")
gas = Category("Gas")
internet = Category("Internet")


#Deposit/Check Funds/Withdrawal/Get Balance
initial_deposit.deposit(2000, "Deposit")
initial_deposit.get_balance()
initial_deposit.check_funds(100)
initial_deposit.check_funds(2001)
initial_deposit.withdrawal(100, "Withdrawal")

#initial_deposit.__str__()
#initial_deposit.check_funds(2000)

#Transfer $500 to Rent
initial_deposit.transfer(500, rent)
rent.get_balance()
initial_deposit.get_balance()

#Transfer $100 to Utilities
initial_deposit.transfer(100, utilities)
utilities.get_balance()
initial_deposit.get_balance()

#Transfer $200 to Insurance
initial_deposit.transfer(200, insurance)
insurance.get_balance()
initial_deposit.get_balance()

#Transfer $400 to Food
initial_deposit.transfer(400, food)
food.get_balance()
initial_deposit.get_balance()

#Transfer $400 to Gas
initial_deposit.transfer(100, gas)
gas.get_balance()
initial_deposit.get_balance()

#Transfer $400 to Internet
initial_deposit.transfer(100, internet)
food.get_balance()
initial_deposit.get_balance()
