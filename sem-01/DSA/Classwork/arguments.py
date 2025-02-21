
def mul(a, b, *argc, **kwargs):
    prod = 1
    for i in argc:
        prod *= i
        
    for k, v in kwargs.items():
        print(f"keys: {k} and values: {v}")
    
    return prod
    
print(mul(1,1,2,3,4,5,6, one=1, two=2))
print(mul(1,2,3,4,5))

'''
def operation(a, b=2, c=3, d): # ERROR
    pass    
'''

# IN KEYWORD ARGUMENTS IN PYTHON, THE KEYWORD ARGUMENTS NEED NOT BE IN ORDER.

