import os

def read_age():
    age = int(input('enter your age: '))
    if(age <= 0):
        raise ValueError('age cannot be -ve')
    return age

def read_file(filename):
  try:
    f = open(filename, 'r')
    data = f.read()
    print(data)
    
    age = read_age()
    
    a = 5 + age
    b = 10
    num = a/b  
  except FileNotFoundError:
    print(f"Error: File '{filename}' is not found.")
  except ZeroDivisionError:
       print(f"zero division error.")
  except ValueError as e:
      print(f"{e}")
  except IOError as e:
    print(f"Error: An I/O error occurred while reading the file: {e}")
  finally:
    f.close()
    print("This will always be executed")

def factorial(n):
  if(n <= 1):
    return 1
  else:
    return n * factorial(n-1)

if __name__ == '__main__':
 read_file('input.txt')
 print("hello I have recovered")

 num = 5
 if not isinstance(num,(int, float)):
   raise TypeError('num should be numeric')
elif (num < 0):
   raise ValueError('value should be negative')
   
print(f"factorial of {num} is {factorial(num)}")

