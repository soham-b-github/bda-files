class MyString(str):
    
    def is_palindrome(self):
        return self == self[::-1]
        

a = MyString('hello')
print(a.is_palindrome())

