def search(L, left, right, x):
    if left > right:
        return -1
    mid = (left + right) // 2

    if L[mid] == x:
        return mid
    
    if L[mid] > x:
        return search(L, left, mid-1, x)
    
    if L[mid] < x:
        return search(L, mid+1, right, x)

if __name__ == "__main__":
    L = [1,2,3,4,5,6,7,8,9]
    left, right = 0, len(L) - 1
    
    for x in range(1,11):
        position = search(L, left, right, x)

        if position == -1:
            if x in L:
                print(x, "is in L, but function returned -1")
            else:
                print(x, "not in list")
        else:
            if L[position] == x:
                print(x, "found in currect position.")
            else:
                print("binary search returned", position, "for", x, "which is not currect")
    print("progrma terminated")
