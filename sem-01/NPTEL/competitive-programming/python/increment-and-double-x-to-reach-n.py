n = int(input())

# Goal : To reach n, from 1, either by incrementation, or by doubling strategy
# Or in other words, we can reach 1 from n, by decrementation or by halving the number

N = n
count=0

while N>1:
    if not N%2: 
        # if even
        N=N//2
    else:
        N-=1
    count+=1


print(f"Minimum number of steps required to reach {n} using this strategy = {count}")