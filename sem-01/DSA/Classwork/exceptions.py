import math

def read_age():
    age = float(input('Enter your age:'))
    # you need to have an except block for this to work as intended
    if age <= 0:
        raise ValueError('Age cannot be negative')
    elif age - math.floor(age) != 0:
        raise ValueError('Age cannot be non-integral')
    return age


try:
    read_age()
except ValueError as e:
    print('Value error:', e)
