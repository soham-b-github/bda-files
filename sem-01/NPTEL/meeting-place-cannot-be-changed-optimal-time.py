n=int(input())
x = list(map(int, input().split()))
v = list(map(int, input().split()))
seconds = 1

L=[]
R=[]

print(v)
length = len(x)

flag = False

threshold = 10

while(True and seconds<=threshold):
    
    v = [i*seconds for i in v]
    L,R = [],[]
    for i in range(length):
        L+=[x[i]-v[i]]
        R+=[x[i]+v[i]]

    # print(L)
    # print(R)

    if(max(L)<=min(R)):
        print(f'YES. {seconds} seconds is the least time required by the people to meet at a common place!')
        flag = True
        break
    else:
        print(f'Not yet for {seconds} seconds')
        
    seconds+=1


if not flag:
    print(f'Perhaps for {threshold} seconds, it is not possible to have a common meeting place!')