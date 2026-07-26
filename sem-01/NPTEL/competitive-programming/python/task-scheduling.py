n = int(input())

A = []

for _ in range(n):
    A+=[tuple(map(int, input().split()))]


Tasks = sorted(A, key=lambda x: x[1])
print(Tasks)


current_time = 0
L = [0]*n
M_l = 0
i=0

for t,d in Tasks:
    current_time+=t
    if current_time>d:
        L[i] = current_time-d
    
    print(L)
    
    i+=1


M_l = max(L)
print(f"Maximum lateness = {M_l}")