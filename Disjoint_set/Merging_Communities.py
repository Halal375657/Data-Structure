
#
# Merging Communities
# 1.Initialization persons list.
# 2.I Connect with J
# 3.Count Result persons
#


class Network:
    def __init__(self, n):
        self.n = n
        self.persons = [None] * n

        for i in range(self.n):
            self.make_set(i)
            
    def make_set(self, n):
        self.persons[n] = n

    def findRip(self, r):
        root = r
        while self.persons[root] != root:
            root = self.persons[root]

        while self.persons[root] != r:
            temp = self.persons[r]
            self.persons[r] = root
            r = self.persons[temp]

        return root

    def union(self, a, b):
        u, v = self.findRip(a), self.findRip(b)
        self.persons[v] = u

    def query(self, p):
        for i in range(self.n):
            self.findRip(i)
        res = self.persons.count(self.persons[p])
        print(res)



if __name__ == "__main__":
    
    n, q = map(int, input().split())
    sol = Network(n)
    
    for _ in range(q):
        query = input().split()
        if query[0] == "M":
            sol.union(int(query[1])-1, int(query[2])-1)
        else:
            sol.query(int(query[1])-1)
