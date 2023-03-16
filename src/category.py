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

    def transfer(self):
        pass

    #def check_funds(self):
        

    #def __str__(self):
        #pass
        

rent = Category("Rent")
utilities = Category("Utilities")
insurance = Category("Insurance")
food = Category("Food")
gas = Category("Gas")
clothes = Category("Clothes")

#print(food)
#print(jm)

rent.deposit(2000, 'Deposit')
rent.withdrawal(1000, 'Withdrawal')
rent.get_balance()


#Jack.check_funds()
#food.deposit(22, 'Sandwich')
