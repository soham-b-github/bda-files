# Pancake Flipping

T = int(input())

for _ in range(T):
    X = input().split()
    S = X[0]+' '
    K = int(X[1])
    
    c,j = 0,0
    cont = []
    
    for i in S:
        if i=='-':
            c+=1
        else:
            cont+=[c]
            c=0
    
    flips = sum([i!=0 for i in cont])
    
    flag = 1 if not sum([i%K for i in cont]) else 0
    
    if flag:
        print(f"Case#{_+1}: {flips} many FLIP(s) possible!")
    else:
        print(f"Case#{_+1}: Impossible!")