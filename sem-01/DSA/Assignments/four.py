import random

class BankAccount:
    def __init__(self, initial_bal):
        self.initial_bal = initial_bal
        self.balance = initial_bal
        self.owner = ''
        self.transactions = []
        self.account_number = 0
        self.generate_account_number()
        print(f'Profile of ACC.NO.{self.account_number} opened.')
        print(f'Initial balance of ACC.NO.{self.account_number} = {initial_bal}')
    
    def deposit(self, amount):
        print()
        self.balance+=amount
        print(f'Deposited Rs.{amount} successfully to ACC.NO.{self.account_number}\nCurrent Balance of ACC.NO.{self.account_number} = Rs.{self.balance}')
        self.transactions+=[amount]
        
    def withdraw(self,amount):
        print()
        print(f'Fetching to withdraw Rs.{amount} from ACC.NO.{self.account_number}')
        x = self.balance - amount
        if x<0:
            print('Insufficient Balance!')
            return
        else:
            self.balance = x
            print(f'Withdrawal of Rs.{amount} successful from ACC.NO.{self.account_number}\nCurrent Balance of ACC.NO.{self.account_number} = Rs.{self.balance}')
            self.transactions+=[-amount]
    
    def generate_account_number(self):
        #Randomly generate a number between 1000 and 10000 to be set only once, it cannot be changed thereafter. Add this logic while implementing this method.
        acc = random.randint(1000,10001)
        self.account_number = acc
    
    def transfer(self,amount,other_acc):
        print()
        print(f'Transferring Rs.{amount} from {self.account_number} to {other_acc}')
        self.withdraw(amount)
    
    def set_owner(self,owner):
        self.owner = owner
    
    def display(self):
        print()
        print('Displaying details of the Bank Account')
        print(f'Balance of ACC.NO.{self.account_number} = Rs.{self.balance}')
        print(f'Owner Name = {self.owner}')
    
    def get_transaction_history(self):
        print(f'Transaction History of ACC.NO.{self.account_number} = {self.transactions}')
    

print('\nFourth Question Solution\n')
acc = BankAccount(500)
acc.deposit(200)
acc.set_owner('Abhik')
acc.transfer(100,2560)
acc.withdraw(400)
acc.display()
acc.withdraw(400)
acc.set_owner('Anand')
acc.get_transaction_history()

