n = int(input())

A = [i+1 for i in range(n)]

X = list(map(int, input().split()))
I = [1 if X[i]==i+1 else 0 for i in range(n-1)]

print(I)
lo = 0
hi = n-2
while(lo<=hi):
    mid = (lo+hi)//2
    if(I[mid-1]==0):
        hi=mid-1
    elif(I[mid+1]==1):
        lo=mid+1
    else:
        print(mid+1)
        break
