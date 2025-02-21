# week 11 assignment q1
# shows sequence

n = int(input())
# S = list(map(int, input().split()))
next_ = list(map(int, input().split()))

watch = [0]*(n+1)

for i in range(n,0,-1):
    if i==n:
        watch[i]=1
    elif next_[i]==-1:
        watch[i]=watch[i+1]
    else:
        watch[i] = max(1+watch[next_[i]], watch[i+1])

print(watch[1:])
print(max(watch),' is the maximum number of shows one can watch!')