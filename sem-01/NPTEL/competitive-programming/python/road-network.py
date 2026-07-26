# road network

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
    all_len+=w


edges = sorted(edges, key=lambda x: x[2])

print(edges)

vertices_visited = []

len_mcst = 0
edges_mcst=[]

for edge in edges:
    v1 = edge[0]
    v2 = edge[1]
    w = edge[2]
    
    C1 = v1 in vertices_visited and v2 not in vertices_visited
    C2 = v2 in vertices_visited and v1 not in vertices_visited
    C3 = v1 not in vertices_visited and v2 not in vertices_visited
    if C1 or C2 or C3:
        edges_mcst += [(v1,v2)]
        len_mcst+=w
        if C1:
            vertices_visited+=[v2]
        elif C2:
            vertices_visited+=[v1]
        else:
            vertices_visited+=[v1,v2]


print(f"Length of minimum spanning tree = {len_mcst}")

print(f"Length of the edges that are removed = {all_len - len_mcst}")

print(edges_mcst)