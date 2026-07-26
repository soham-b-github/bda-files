# reversort

def reverse(L):
    return L[::-1]

def reversort(L):
    
    l = len(L)
    
    for i in range(l-1):
        # print(f"Iteration#{i}")
        
        x = min(L[i:])
        ind = L.index(x)
        rev = reverse(L[i:ind+1])
        # print(f"\ti={i} and ind={ind}")
        # print("\tRev = ",rev)
        L = L[:i]+rev+L[ind+1:]
        # print("\tL = ",L)
    
    return L



L = [3,5,6,1,9,2,4]
print(f"Sorted List is = {reversort(L)}")