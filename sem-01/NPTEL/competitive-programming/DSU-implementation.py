# DSU
class DisjointSet:
    
    def __init__(self, n):
        # We are using 1-based indexing
        self.n = n
        self.rank = [0]*(self.n+1) # Basically stores the depth (or height) of each node
        self.parent = [i for i in range(self.n+1)]
    
    
    def findSet(self,node):
        if parent[node]==node:
            return node
        return findSet(parent[node])
    
    def findUPar(self, node):
        if node == self.parent[node]:
            return node
        
        # Path Compression
        # self.parent[node] = self.findUPar(self.parent[node])
        # return self.parent[node]
        
        # Without path Compression
        return self.findUPar(self.parent[node])
        
        
        # Updated concept is: the process of returning the ultimate parent is path compression
        # As it is not returning the preceding parent node, it is reaching the root.
    
    def unionByRank(self, u,v):
        ulp_u = self.findUPar(u)
        ulp_v = self.findUPar(v)
        
        if ulp_v==ulp_u:
            return
        elif self.rank[ulp_u] < self.rank[ulp_v]:
            self.parent[ulp_u] = ulp_v
            # There is no change in rank, as shorter length gets attached to larger length
        elif self.rank[ulp_v] < self.rank[ulp_u]:
            self.parent[ulp_v] = ulp_u
        else:
            self.parent[ulp_v] = ulp_u
            self.rank[ulp_u]+=self.rank[ulp_v]
            # There is a increase in the rank of ulp_u as including ulp_u, the entire ulp_v children set
            # gets added to the children-set of ulp_u




# ds = DisjointSet(5)
# ds.unionByRank(1,2)
# ds.unionByRank(2,3)
# ds.unionByRank(4,5)
# ds.unionByRank(6,7)
# ds.unionByRank(5,6)

# ds.unionByRank(0,3)
# ds.unionByRank(1,3)
# ds.unionByRank(2,5)
# ds.unionByRank(1,4)


n = int(input())
q = int(input())
ds = DisjointSet(n)

for i in range(q):
    print(f'{i+1}th iteration:-')
    x,y = map(int, input().split())
    print('\tInitial parents :',ds.parent)
    ds.unionByRank(x,y)
    print('\tFinal parents :',ds.parent)
    

# ds.unionByRank(1,2)
# ds.unionByRank(3,4)
# ds.unionByRank(2,4)
# ds.unionByRank(1,4)

# print(ds.parent)

# if 3 and 7 are in the same component
# if ds.findUPar(3) == ds.findUPar(7):
#     print('Yes, 3 and 7 are in the same component')
# else:
#     print('3 and 7 are not in the same component')


# ds.unionByRank(3,7)

# # if 3 and 7 are in the same component
# if ds.findUPar(3) == ds.findUPar(7):
#     print('Yes, 3 and 7 are in the same component')
# else:
#     print('3 and 7 are not in the same component')

















