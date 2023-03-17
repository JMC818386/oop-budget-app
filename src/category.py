class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.amount = 0
        self.description = ""

    def deposit(self, transaction, description = None):
        if description == None:
            description = ""
        self.ledger.append({"Amount": transaction, "Description": description})
        self.amount += transaction
        print(f'${self.amount}.00 has been deposited into {self.name}.')
        print(self.ledger)
        
    def withdrawal(self, transaction, description):
        self.ledger.append({"Amount": -abs(transaction), "Description": description})
        if transaction > self.amount:
            print('Insufficent Funds')
        elif transaction <= self.amount:    
            self.amount -= transaction
            print(f'${transaction}.00 has been withdrawn from the {self.name}.')
            print(self.ledger)
            
    def get_balance(self):
        print(f'{self.name} has a balance of ${self.amount}.00.')

    def transfer(self, transfer_amount, name):
        if transfer_amount <= self.amount:    
            name.amount += transfer_amount
        if transfer_amount > self.amount:
            print('Cannot Complete Transfer: Insufficent Funds')
        elif transfer_amount <= self.amount:
            self.amount -= transfer_amount
        print(f'${transfer_amount}.00 has been transfered to {name.name}')
        self.ledger.append(f'Transfered [${transfer_amount}.00] to [{name.name}]')
        self.ledger.append(f'Transfered [${transfer_amount}.00] from [{self.name}]')
        print(self.ledger)
        print(f'${initial_deposit.amount}.00 {self.name} amount after transfer')
        print(f'${name.amount}.00 {name.name} amount after transfer')

    #def check_funds(self):
        #pass
        
    #def __str__(self):
        #pass
        
initial_deposit = Category("Initial Deposit")
rent = Category("Rent")
utilities = Category("Utilities")
insurance = Category("Insurance")
food = Category("Food")
gas = Category("Gas")
internet = Category("Internet")

#Initial Deposit
initial_deposit.deposit(3000, "Deposit")
initial_deposit.get_balance()

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



#rent.deposit(2000, 'Deposit') #deposit into rent
#rent.transfer(1000, initial_deposit)


#initial_deposit.get_balance()#balance of initial_deposit
#print(rent.amount)
#rent.withdrawal(1000, 'Withdrawal')
