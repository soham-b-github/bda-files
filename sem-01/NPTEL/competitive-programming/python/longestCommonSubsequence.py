# Longest Common Subsequence

S1 = input()
S2 = input()

m,n = len(S1), len(S2)

LCS = [[0] * n for _ in range(m)]
# print(LCS)

M=-1
c=0

for i in range(m):
    for j in range(n):
        if i==0 or j==0:
            LCS[i][j]=0
        elif S1[i]==S2[j]:
            LCS[i][j]=1+LCS[i-1][j-1]
        else:
            LCS[i][j]=max(LCS[i-1][j],LCS[i][j-1])
        M = max(M, LCS[i][j])


for i in LCS:
    print(i)
    c+=i.count(M)
    
print(f'Length of Longest Common Subsequence = {M}')
print(f'Number of LCS possible = {c}')
