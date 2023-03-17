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

    def check_funds(self, amount):
        if self.amount < amount:
            print(False)
            return False
        elif self.amount >= amount:
            print(True)
            return True
        
    #def __str__(self):
        #print(f'{self.name}: {self.amount}')
        #return f'{self.name}: {self.amount}'
        

initial_deposit = Category("Initial Deposit")
rent = Category("Rent")
utilities = Category("Utilities")
insurance = Category("Insurance")
food = Category("Food")
gas = Category("Gas")
internet = Category("Internet")