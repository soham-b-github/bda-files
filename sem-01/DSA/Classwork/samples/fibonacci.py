def fibonacci(n):
    a , b  = 0, 1
    arr = []
    for i in range(n):
        arr.append(a)
        a,b = b,a+b
    
    return arr


def gen_func_fibo():
    x, y = 0, 1
    while(True):
        yield x
        x, y = y, x+y


def simple_gen():
    for i in range(100000):
        yield i

def add(a, *argv):

    sum = a
    for i in argv:
        sum +=i
    return sum    


print(fibonacci(20))

g = gen_func_fibo()

for i in range(20):
    print(next(g))

print(add(3,4))
print(add(4,5,6,7,8))

lst = [1,4,5,2,4,8]
i = iter(lst)
print(next(i))

g = simple_gen()

for _ in range(20):
    print(next(g))