# Destroying Arrays

n = int(input())
A = list(map(int, input().split()))
P = list(map(int, input().split()))

indices=[]
sums=[]

for i in range(1,11):
    index = P.index(i)
    A[index] = 0
    indices+=[index]
    print(f'{i}th iteration')
    maxi_sum = -1
    init = -1
    
    indices = sorted(indices)
    print(f'\tIndices = {indices}')
    
    for index in indices:
        S = sum(A[init:index]) if init!=-1 else sum(A[init+1:index])
        maxi_sum = max(maxi_sum, S)
        init = index
        print('\t',S)
    
    maxi_sum = max(maxi_sum, sum(A[init:]))
    print('\t',sum(A[init:]))
    sums+=[maxi_sum]

print(sums)