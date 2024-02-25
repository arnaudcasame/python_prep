from typing import List

def canTraverseAllPairs(nums: List[int]) -> bool:
    uf = UnionFind(len(nums))
    factor_index = {}
    for i, n in enumerate(nums):
        f = 2
        while f * f <= n:
            if n % f == 0:
                if f in factor_index:
                    uf.union(i, factor_index[f])
                else:
                    factor_index[f] = i
                while n%f == 0:
                    n = n // f
            f += 1
        if n > 1:
            if n in factor_index:
                uf.union(i, factor_index[n])
            else:
                factor_index[n] = i
    return uf.count == 1


class UnionFind():
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n
        self.count  =  n
        
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
            self.rank[py] += self.rank[px]
        else:
            self.parent[py] = px
            self.rank[px] += self.rank[py]
        self.count -= 1
        
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]