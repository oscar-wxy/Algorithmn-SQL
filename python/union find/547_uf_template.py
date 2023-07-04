"""
Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2

Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
"""

"""
my thought:
union find

parents = [0,1,2]

def union(a,b):
    pick small index
    union(0,1): [0,1,2] => [0,0,2]

len(set(parents))
"""
class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        uf = UF(len(isConnected))
        for i in range(len(isConnected)):
            for j in range(i+1, len(isConnected), 1):
                print("{},{}".format(str(i), str(j)))
                if(isConnected[i][j] == 1):
                    uf.union(i,j)

        return len(set([uf.find(i) for i in range(len(isConnected))]))

class UF:
    def __init__(self, size):
        # point to themselves
        self.parent = list(range(size))
        self.rank = [0 for i in range(size)]
    
    # wrote it wrong
    """
    How I was wrong:
        def union(self, a,b):
            pa, pb = self.find(a), self.find(b)
            if self.rank[a] > self.rank[b]:
                self.parent[b] = pa
            elif self.rank[a] < self.rank[b]:
                self.parent[a] = pb
            else:
                self.parent[b] = pa
                self.rank[a] = self.rank[a] + 1
    """
    def union(self, a,b):
        pa, pb = self.find(a), self.find(b)
        if self.rank[pa] > self.rank[pb]:
            self.parent[pb] = pa
        elif self.rank[pa] < self.rank[pb]:
            self.parent[pa] = pb
        else:
            self.parent[pb] = pa
            self.rank[pa] = self.rank[pa] + 1
    def find(self, a):
        # revursive, and reshape/ path compress at the same time
        if self.parent[a] != a:
            self.parent[a] = self.find(self.parent[a])

        return self.parent[a]
