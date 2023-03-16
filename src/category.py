class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.amount = 0
        self.description = ""

    def deposit(self, total, description):
        self.ledger.append({"Amount": total, "Description": description})
        self.amount += total
        print(f'${self.amount}.00 has been deposited into {self.name}\'s account')
        #print(self.ledger)
        
    def withdrawal(self, total, description):
        self.ledger.append({"Amount": total, "Description": description})
        self.amount -= total
        print(f'${self.amount}.00 has been withdrawn from {self.name}\'s account')
        print(self.ledger)
        #if total == 0
            

    def get_balance(self):
        print(f'{self.name} has an account balance of ${self.amount}.00.')

    def transfer(self):
        pass

    def check_funds(self):
        print(f'{self.name} has an account balance of ${self.amount}.00.')

    #def __str__(self):
        #pass
        
Jack = Category("Jack")
food = Category("Food")
#print(food)
#print(jm)

Jack.deposit(1000, 'Deposit')
Jack.withdrawal(50, 'Withdrawal')
Jack.get_balance()
Jack.check_funds()
#food.deposit(22, 'Sandwich')

