# Longest Increasing Sequence

# n = int(input())
L = list(map(int, input().split()))
n = len(L)

LIS = [1]*n

for i in range(n):
    for j in range(i):
        if L[i]>L[j]:
            LIS[i] = max(LIS[i],LIS[j]+1)

print(LIS)
print(max(LIS))