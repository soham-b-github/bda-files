import time
# optimized code for 3-sum
# we shall use binary search

def binarySearch(L, elem):
    n = len(L)
    lo, hi = 0, n-1
    mid = 0
    while(lo<hi):
        mid = (lo+hi)//2
        if(L[mid]==elem):
            return True
        elif L[mid]>elem:
            hi = mid-1
        else:
            lo = mid+1
    
    return False



L = list(map(int, input('Please enter a list of numbers seperated by blankspaces: ').split()))
n = len(L)

print('Let us see if there exists 3-sum, we shall print it.')

flag = 0 # variable to check if 3-sum exists or not

# delay
for i in range(10000):
    continue

start_time = time.time()

for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1, n):
            if binarySearch(L[k:], (-(L[i]+L[j]))):
                flag = 1
                print(f'{L[i]}+{L[j]}+{L[k]} = 0')


if not flag:
    print('Sorry in this list there does not exist any 3-sum!')

end_time = time.time()

print(f'Time taken to execute the piece of code = {end_time-start_time} seconds')