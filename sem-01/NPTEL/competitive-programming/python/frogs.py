# frog DP-implementation
# DP = recursion + memoization

# Frog can jump from i to i+1 or i to i+2
# To find the cost to reach the Nth stone from stone 1

N = int(input())
h = list(map(int, input().split()))

cost = [0]*N
cost[0] = 0
cost[1] = abs(h[1]-h[0])

for i in range(2,N):
    p1 = abs(h[i]-h[i-1])+cost[i-1]
    p2 = abs(h[i]-h[i-2])+cost[i-2]
    cost[i] = min(p1,p2)


print(cost)
print(cost[-1])