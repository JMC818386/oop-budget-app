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
        print(f'${self.amount}.00 has been deposited into {self.name}\'s account')
        print(self.ledger)
        
    def withdrawal(self, transaction, description):
        self.ledger.append({"Amount": transaction, "Description": description})
        if transaction > self.amount:
            print('Insufficent Funds')
        elif transaction <= self.amount:    
            self.amount -= transaction
            print(f'${transaction}.00 has been withdrawn from {self.name}\'s account')
            print(self.ledger)
            
    def get_balance(self):
        print(f'{self.name} has an account balance of ${self.amount}.00.')

    def transfer(self):
        pass

    #def check_funds(self):
        #print(f'{self.name} has an account balance of ${self.amount}.00.')

    #def __str__(self):
        #pass
        
jack = Category("Jack")
food = Category("Food")
#print(food)
#print(jm)

jack.deposit(1000, 'Deposit')
jack.withdrawal(1000, 'Withdrawal')
jack.deposit(500)
jack.get_balance()
#Jack.check_funds()
#food.deposit(22, 'Sandwich')
