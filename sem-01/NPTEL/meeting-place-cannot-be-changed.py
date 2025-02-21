n=int(input())
x = list(map(int, input().split()))
v = list(map(int, input().split()))
seconds = int(input())

L=[]
R=[]
v = [i*seconds for i in v]
print(v)
length = len(x)
for i in range(length):
    L+=[x[i]-v[i]]
    R+=[x[i]+v[i]]

print(L)
print(R)

if(max(L)<=min(R)):
    print('YES')
else:
    print('NO')