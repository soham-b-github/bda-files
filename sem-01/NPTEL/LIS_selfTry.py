# Longest Increasing Sequence

# n = int(input())
L = list(map(int, input().split()))
n = len(L)

LIS = [1]*n

for i in range(n):
    k = -1
    c=1
    for j in range(i):
        if L[j]<L[i]:
            if k==-1:
                k = j
                c+=1
                continue
            if L[j]>L[k]:
                k = j
                c+=1
    LIS[i] = max(LIS[i], c)

print(LIS)
print(max(LIS))