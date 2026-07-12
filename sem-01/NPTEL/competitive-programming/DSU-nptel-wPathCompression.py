# DSU with path compression
class DisjointSet:
    
    def __init__(self, n):
        # We are using 0-based indexing
        self.n = n
        self.rank = [0]*(self.n) # Basically stores the depth (or height) of each node
        self.parent = [i for i in range(self.n)]
    
    
    def findSet(self,u):
        if(self.parent[u] == u):
	        return u
        self.parent[u] = self.findSet(self.parent[u])
        return self.parent[u]


    def unionSet(self,u, v):
        x = self.findSet(u)
        y = self.findSet(v)
        print(f"\tx={x}(Ultimate parent of {u}) and y={y}(Ultimate parent of {v})")
        if(x != y):
	        self.parent[y] = x



dsu = DisjointSet(6)

queries = [(0,3),(1,3),(2,5),(1,4)]
length = len(queries)

for _ in range(length):
    x,y = queries[_][0],queries[_][1]
    print(f'{_+1}th Iteration:\n\t',dsu.parent)
    dsu.unionSet(x,y)
    print('\t',dsu.parent)