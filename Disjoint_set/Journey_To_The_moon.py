# Problem Link:- https://www.hackerrank.com/challenges/journey-to-the-moon/problem


class Disjoint:
    def __init__(self, n):
        self.parent = [None] * n
        self.n = n
        self.count = 0
        
        for i in range(n):
            self.makeset(i)


    def makeset(self, n):
        self.parent[n] = n

    def find(self, r):
        if self.parent[r] != r:
            self.parent[r] = self.find(self.parent[r])

        return self.parent[r]

    def union(self, a, b):
        u, v = self.find(a), self.find(b)
        if u != v:
            self.parent[v] = u # Or self.parent[v] = u

    def result(self):
        res = [0] * self.n

        for i in range(self.n):
            res[self.find(i)] += 1

        sum_ = 0
        for i in res:
            sum_ += i * (n - i)

        print(sum_ // 2)

        
if __name__=="__main__":

    n, p = map(int, input().split())
    dis = Disjoint(n)
    for i in range(p):
        u, v = map(int, input().split())
        dis.union(u, v)
        
    dis.result()       
