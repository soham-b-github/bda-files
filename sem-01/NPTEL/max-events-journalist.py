n = int(input())

A = []

for _ in range(n):
    A+=[tuple(map(int, input().split()))]


Events = sorted(A, key=lambda x: x[1])
print(Events)

i=0
count=0
l = len(Events)
count = 1

while i<l:
    j = i+1
    current = Events[i]
    
    while j<l:
        if Events[j][0]>=current[1]:
            i=j-1
            count+=1
            break
        j+=1
    
    i+=1
    
print(f"Maximum number of events a journalist can attend = {count}")