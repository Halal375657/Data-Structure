# makeset() Time: O(1)
# union() Time: O(1)
# find() Time: O(n)-worst case.


class Disjoin(object):
    def __init__(self, n):
        self.parent = [None] * (n+1)

        for i in range(1, n+1):
            self.makeset(i)
            
    def makeset(self, n):
        self.parent[n] = n # Assaign n as a parent of the n.

    # Path compression
    def find(self, r):
        if self.parent[r] != r:
            self.parent[r] = self.find(self.parent[r])
        return self.parent[r]

    def union(self, a, b):
        u = self.find(a)
        v = self.find(b)

        if u != v:
            self.parent[v] = u

            
            
if __name__ == "__main__":
    edges = ((1, 4),
             (1, 2),
             (1, 5),
             (2, 3),
             (2, 6),
             (8, 9),
             (9, 10)
             )

    disjoin = Disjoin(10)
    for tpl in edges:
        disjoin.union(tpl[0], tpl[1])
    print(disjoin.parent[1:])

