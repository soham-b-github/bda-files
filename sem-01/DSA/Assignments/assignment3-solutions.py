# To run a solution of one particular question, it is advised to comment out the remaining code lines

#-------------------------------------------------------------------------------#
# 1. First question solution
class Factorial:
    def __init__(self, n):
        self.n = n
        self.result = 1
        if(self.n<=1):
            self.result = self.n
        elif(self.n<0):
            self.result = -1
        else:
            fact = 1
            for i in range(1,self.n+1):
                fact*=i
            self.result = fact
        

print('\nFirst Question Solution\n')
n = int(input('Enter any number = '))
fobj = Factorial(n)
print('Result =',fobj.result)

#-------------------------------------------------------------------------------#
# 2. Second Question Solution
class FileOperation:
    def __init__(self, filename):
        self.filename = filename
        self.lines = []
    
    
    def readContent(self):
        print('\nReading contents from file!\n')
        with open(self.filename, 'r') as file:
            content = file.read()
            print(content)
    
    # 2(a)
    def convertContentsToUpper(self):
        print('\nConverting contents of file to uppercase!\n')
        with open(self.filename, 'r+') as file:
            content = file.read()
            # print(type(content))
            
            new_content = content.upper()
            print(new_content)
    
    # 2(b)
    def toggleCaseOfContents(self):
        print('\nToggling the case of the contents of the file!\n')
        with open(self.filename, 'r+') as file:
            content = file.read()
            new_content = ''
            for i in content:
                ch = i.upper()
                if ch==i:
                    new_content+=i.lower()
                else:
                    new_content+=ch
            
            print(new_content)
    
    # 2(c)
    def countWords(self):
        with open(self.filename, 'r+') as file:
            content = file.read()
            words = content.split(' ')
            
            print(f'The number of words present in the file = {len(words)}')
    
    # 2(d)
    def countAlphaNumeric(self):
        with open(self.filename, 'r+') as file:
            content = file.read()
            valid_char = [i for i in range(65,91)]+[i for i in range(97,123)]+[i for i in range(48,58)]
            count = 0
            for i in content:
                if ord(i) in valid_char:
                    count+=1
            
            print(f'The number of alphanumeric characters present in the file = {count}')
            



contents = 'The sun was beginning to set, casting a warm golden glow over the quiet village. Birds chirped their final songs of the day, while the gentle breeze carried the scent of blooming flowers. In the distance, children laughed and played, their joyful voices mingling with the soft rustling of leaves. It was a peaceful evening, one that seemed to slow time and remind everyone of life’s simple pleasures.'


print('\nSecond Question Solution\n')
filename = 'sample.txt'

file = open(filename, 'w+')
content = file.write(contents)
file.close()

fileobj = FileOperation('sample.txt')

fileobj.readContent()

fileobj.convertContentsToUpper()

fileobj.toggleCaseOfContents()

fileobj.countWords()
fileobj.countAlphaNumeric()

#-------------------------------------------------------------------------------#
# 3. Third Question
class MyString(str):
    def __init__(self,value):
        super().__init__()
    
    def checkPalindrome(self):
        rev = self[::-1]
        print('\nHere the methods are case-sensitive.')
        if(rev==self):
            print(f'\'{self}\' is a Palindrome string.')
        else:
            print(f'Given string is a non-Palindrome string.')
    
    def countWords(self):
        c = len(self.split())
        print(f'Number of words present in the string = {c}')
    
    def countNonAlphanumericChar(self):
        count = 0
        valid_ord = [i for i in range(65,91)]+[i for i in range(97,123)]+[i for i in range(48,58)]+[32]
        for i in self:
            if ord(i) in valid_ord:
                continue
            else:
                count+=1
        
        print(f'Number of non-alphanumeric (any character other than alphabets/numbers/blankspaces) characters = {count}')


print('\nThird Question Solution\n')
s = input('Enter a string : ')
sobj = MyString(s)
sobj.checkPalindrome()
sobj.countWords()
sobj.countNonAlphanumericChar()


#-------------------------------------------------------------------------------#
# 4. Fourth Question Solution

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




#-------------------------------------------------------------------------------#
# 5. Fifth Question

class BinarySearch:
    def __init__(self,arr):
        self.arr = arr
    
    def search(self,s):
        n = len(arr)
        lo,hi=0,n-1
        
        arr.sort()
        print(f'Sorted list = {arr}')
        print('Searching the element...')
        
        #delay
        for i in range(10000):
            continue
        
        while(lo<=hi):
            mid=(lo+hi)//2
            c = arr[mid]
            if c==s:
                print(f'Found {s} in the given list of elements at index {mid}!')
                return
            elif c<s:
                lo=mid+1
            else:
                hi=mid-1
        
        if arr[mid]==s:
            print(f'Found {s} in the given sorted-list of elements at index {mid}!')
        else:
            print(f'Asked element {s} is not found in the list!')


print('\nFifth Question Solution\n')
arr = list(map(int, input('Enter a list of numbers :').split()))
elem = int(input('Enter a number to be searched in the given list of numbers :'))
bs = BinarySearch(arr)
bs.search(elem)

