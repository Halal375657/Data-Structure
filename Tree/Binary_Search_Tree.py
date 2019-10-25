#Binary search tree.


class TreeNode:
    def __init__(self, data):
        self.data           = data
        self.parent        = None
        self.left             = None
        self.right           = None

    def __repr__(self):
        return repr(self.data)

    def add_left(self, node):
        self.left   = node
        if node:
            node.parent = self

    def add_right(self, node):
        self.right = node
        if node:
            node.parent = self

def bst_insert(root, node):
    if root is None:
        root = node
        return root
    
    last_node = None
    current_node = root
    while current_node:
        last_node = current_node
        if node.data < current_node.data:
            current_node = current_node.left
        else:
            current_node = current_node.right

    if node.data < last_node.data:
        last_node.add_left(node)
    else:
        last_node.add_right(node)

    return root

def bst_create():
    root = TreeNode(10)

    for data in [5, 17,  3, 7, 12, 19, 1, 4]:
        node = TreeNode(data)
        root = bst_insert(root, node)

    return root

def in_order(node):
    if node.left:
        in_order(node.left)
    print(node)
    if node.right:
        in_order(node.right)

def bst_minimum(root):
    while root.left:
        root = root.left
    return root

def bst_maximum(root):
    while root.right:
        right = root.right
    return right

def bst_transplant(root, current_node, new_node):
    if current_node.parent is None:
        root = new_node
    elif current_node.parent.left == current_node:
        current_node.parent.add_left(new_node)
    else:
        current_node.parent.add_right(new_node)
    return root

def bst_delete(root, node):
    if node.left is None:
        root = bst_transplant(root, node, node.right)
    elif node.right is None:
        root = bst_transplant(root, node, node.left)
    else:
        min_node = bst_minimum(node.right)
        if min_node.parent != node:
            root = bst_transplant(root, min_node, min_node.right)
            min_node.add_right(node.right)
        root = bst_transplant(root, node, min_node)
        min_node.add_left(node.left)

    return root

def bst_search(root, key):
    while root is not None:
        if root.data == key:
            return root
        if key < root.data:
            root = root.left
        else:
            root = root.right
    return  root


if __name__=="__main__":
    root = bst_create()
    print('BST:')
    in_order(root)

    for key in [1, 5, 10]:
        node = bst_search(root, key)
        print('will delete', node)
        if node:
            root = bst_delete(root, node)
        print("BST:")
        in_order(root)
