def troubleSort(L):
    done = False
    while not done:
        done = True
        for i in range(len(L)-2):
            if L[i]>L[i+2]:
                L[i]=L[i]+L[i+2]
                L[i+2]=L[i]-L[i+2]
                L[i]=L[i]-L[i+2]
    
    return L


print(troubleSort([5,2,1,7,3,4,8,6]))