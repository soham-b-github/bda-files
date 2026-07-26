def compatible(meeting, A):
    if A==[]:
        return True
    else:
        return meeting[0]>=A[-1][1]


def min_no_rooms(meetings):
    
    l = len(meetings)
    
    M = sorted(meetings, key = lambda x: x[1])
    print(M)
    
    rooms = 0
    while(M!=[]):
        
        l = len(M)
        A = []
        
        for i in range(l):
            
            if compatible(M[i],A):
                A+=[M[i]]
        
        M = [x for x in M if x not in A]
        rooms+=1
    
    return rooms



meetings = [(1, 4), (6, 12), (2, 8), (11, 15), (3, 7), (5, 10), (9, 14), (13, 16)]
print(f"Minimum number of rooms required = {min_no_rooms(meetings)}")