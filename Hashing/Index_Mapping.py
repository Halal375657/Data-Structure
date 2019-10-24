#Index Mapping (or Trivial Hashing) with negatives allowed.
#Time for search method is O(1).
#Time for insert method is O(1).

class Hashing(object):
    def search(x):

        #Search for Possitive Number at 0 index of the has list.
        if x >= 0:
            if has[x][0] == 1:
                return True
            else:
                return False

        #Search for Negetive Number at 1 index of the has list.
        x = abs(x)
        if has[x][1] == 1:
            return True
        return False
            

    def insert(a, n):

        for i in range(0, n):
            #Insert a possitive Number at 0 index to currect sublist.
            if a[i] >= 0:
                has[a[i]][0] = 1
            #Insert a Negative Number at 1 index to currect sublist.
            else:
                has[abs(a[i])][1] = 1
            

if __name__ == "__main__":

    a = [-1, 9, -5, -8, -5, -2]
    n = len(a)

    MAX = 1000

    #Since array is global, it is initialized as 0.
    has = [[0 for _ in range(2)] for j in range(MAX + 1)]
    Hashing.insert(a, n)

    x = -8
    if Hashing.search(x) == True:
        print(x, 'is present to has')
    else:
        print(x, 'is not present to has')
        
