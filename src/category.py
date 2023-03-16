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
        #print(self.ledger)
        
    def withdrawal(self, transaction, description):
        self.ledger.append({"Amount": -abs(transaction), "Description": description})
        if transaction > self.amount:
            print('Insufficent Funds')
        elif transaction <= self.amount:    
            self.amount -= transaction
            print(f'${transaction}.00 has been withdrawn from the {self.name}.')
            #print(self.ledger)
            
    def get_balance(self):
        print(f'{self.name} has a balance of ${self.amount}.00.')

    def transfer(self, transaction, name):
        #accepts an amount and another budget category as arguments
        if transaction > name.amount:
            print('Cannot Complete Transfer: Insufficent Funds')
        elif transaction <= name.amount:    
            name.amount -= transaction
        print(f'${transaction}.00 has been transfered to {self.name}')

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
#print(food)
#print(jm)
initial_deposit.deposit(2000, 'Deposit') #deposit into initial deposit
rent.deposit(2000, 'Deposit') #deposit into rent
rent.transfer(1000, initial_deposit)
initial_deposit.get_balance()
rent.get_balance()

#print(initial_deposit.amount)
#print(rent.amount)

#initial_deposit.get_balance()#balance of initial_deposit
#print(rent.amount)
#rent.withdrawal(1000, 'Withdrawal')
