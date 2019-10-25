#Tree implement by python 3.
#Time for pre-order() function is O(n).
#Time for in-order() function is O(n).
#Time for post-order() function is O(n).


class TreeNode:
    def __init__(self, data):
        self.data   = data
        self.parent = None
        self.left   = None
        self.right  = None

    def __repr__(self):
        return repr(self.data)
    
    def add_left(self, node):
        self.left = node
        if node is not None:
            node.parent = self

    def add_right(self, node):
        self.right = node
        if node is not None:
            node.parent = self

'''
     _2_
    /   \
   7     9
  / \     \
 1   6     8
    / \   / \
   5  10 3   4

'''
def create_tree():
    two    = TreeNode(2)
    seven  = TreeNode(7)
    nine   = TreeNode(9)
    two.add_left(seven)
    two.add_right(nine)
    one    = TreeNode(1)
    six    = TreeNode(6)
    seven.add_left(one)
    seven.add_right(six)
    five   = TreeNode(5)
    ten    = TreeNode(10)
    six.add_left(five)
    six.add_right(ten)
    eight  = TreeNode(8)
    nine.add_right(eight)
    three  = TreeNode(3)
    four   = TreeNode(4)
    eight.add_left(three)
    eight.add_right(four)

    #return root node
    return  two

#Tree traverse to pre-order.
def pre_order(node):
    print(node)

    if node.left:
        pre_order(node.left)
    if node.right:
        pre_order(node.right)

#Tree traverse to post-order.
def post_order(node):

    if node.left:
        post_order(node.left)
    if node.right:
        post_order(node.right)
    print(node)

#Tree traverse to in-order.
def In_order(node):

    if node.left:
        In_order(node.left)

    print(node)
    if node.right:
        In_order(node.right)


if __name__ == "__main__":
    root = create_tree()
    print("______________pre_order_____________________")
    pre_order(root)
    print("______________post_order_____________________")
    post_order(root)
    print("______________in_order_____________________")
    In_order(root)
