'''

    ComplixitY:- O(n^2)

'''

def linear_search_recursive(li, item):
    n = len(li)-1
    if li[n] == item:
        return 1
    n = n - 1
    if n == 0:
        return -1
    
    return linear_search_recursive(li[:n], item)

#test linear_search_recursive function
def test_linear_search_recursive():
    li = [1, 5, 2, 7, 20, 10]
    item = 3
    linear_search_recursive(li, item) == -1
    item = 2
    linear_search_recursive(li, item) == 1
    item = 10
    linear_search_recursive(li, item) == 1
    item = 1
    linear_search_recursive(li, item) == 1


if __name__ == "__main__":
    li = [1, 5, 2, 7, 20, 10]
    item = 3
    index = linear_search_recursive(li, item)
    print(index)

