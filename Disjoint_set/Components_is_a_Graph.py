

#
# Problem link:- https://www.hackerrank.com/challenges/components-in-graph/problem
#
#


from collections import defaultdict
from sys import maxsize


class Graph:
    def __init__(self, n):
        self.n = 2*n
        self.parent = [None] * self.n

        for i in range(self.n):
            self.make_set(i)

    def make_set(self, n):
        self.parent[n] = n

    def find_parent(self, r):
        root = r
        while self.parent[root] != root:
            root = self.parent[root]

        while self.parent[r] != root:
            temp = self.parent[r]
            self.parent[r] = root
            r = self.parent[temp]

        return root
    
    def union(self, a, b):
        u = self.find_parent(a)
        v = self.find_parent(b)

        if u != v:
            self.parent[v] = u


    def match(self):
        for i in range(self.n):
            self.find_parent(i)
        
    """def result(self):
        self.match()
        small, largest = maxsize, -1
        count = Counter(self.parent)
        for key in count:
            if (count[key] != 1):
                largest, small = max(largest, count[key]), min(count[key], small)
        print(small, largest)"""

    def result(self):
        self.match()
        d = defaultdict(int)
        s, l = maxsize, -1
                
        for i in range(self.n-1, -1, -1):
            d[self.parent[i]] += 1
            self.parent.pop()

        for key in d:
            if d[key] != 1:
                l, s = max(l, d[key]), min(d[key], s)
                
        print(s, l)
            

if __name__=="__main__":
    n = int(input().strip())
    g = Graph(n)

    for _ in range(n):
        u, v = map(int, input().split())
        g.union(u-1, v-1)

    g.result()
