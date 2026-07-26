# friendships
n = int(input())
L = []

for _ in range(n+1):
    i,j = map(int, input().split())
    L+=[(min(i,j),max(i,j))]

print(L)
L = sorted(L)
# print(L)
l = len(L)

i=0
cycles = 0
already=[]

while i<l:
    j=i+1
    f1,f2 = L[i][0], L[i][1]
    while j<l:
        s1,s2 = L[j][0], L[j][1]
        if f1!=s1:
            break
        m = max(f2,s2)
        mi = min(f2,s2)
        if (mi,m) in L[j:]:
            if (mi,m) not in already:
                already+=[(mi,m)]
                cycles+=1
                # print(f"(f1,f2)=({f1},{f2})\t(s1,s2)=({s1},{s2})\t(mi,m)=({mi},{m})")
        j+=1
    i+=1

print(cycles)