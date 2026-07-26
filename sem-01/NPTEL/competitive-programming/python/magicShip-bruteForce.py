x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())

direction = input()

x,y = x1,y1

for i in direction:
    if i=='U':
        y+=1
    elif i=='D':
        y-=1
    elif i=='L':
        x-=1
    else:
        x+=1
    
    print(f'({x},{y})')
    if(x==x2 and y==y2):
        print('Yes, it reaches its required destination!')
        break