# shortest circular route

n, m = map(int, input().split())
edges = []
all_len = 0
only_edges=[]

for _ in range(m):
    i,j,w = map(int, input().split())
    mi = min(i,j)
    ma = max(i,j)
    edges+=[(mi,ma,w)]
    only_edges+=[(mi, ma)]
    all_len+= w


s = int(input())

edges = sorted(edges, key=lambda x: x[0])
print(edges)

min_path_len = all_len

for i in range(m):
    e = edges[i]
    if e[0]!=s:
        continue
    
    v1,v2 = e[0],e[1]
    
    curr_v1, curr_v2 = e[0], e[1]
    
    visited = [(v1,v2)]
    path_len = e[2]
    
    for j in range(i+1,m):
        
        e1 = edges[j]
        
        u1 = e1[0]
        u2 = e1[1]
        
        if (u1,u2) in visited:
            continue
        elif u1==curr_v2:
            path_len+=e1[2]
            visited+=[(u1,u2)]
            curr_v1=u1
            curr_v2=u2
            
            if (v1,u2) in only_edges:
                path_len+=edges[only_edges.index((v1,u2))][2]
                break # received a circular route
    
    
    min_path_len = min(min_path_len, path_len)


print(min_path_len)