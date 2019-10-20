#prepend()-> {Time:O(1), Space:O(1)}
#append() -> {Time:O(n), Space:O(1)}
#insert() -> {Time:{Worst:O(n), Average:O(n/2), Best:O(1)}, Space:O(1)}
#remove() -> {Time:O(n), Space:O(1)}
#search() -> {Time:O(n), Space:O(1)}

#Node create.
class Node:
    def __init__(self, data=None, next=None):
        self.data, self.next = data, next

    def __repr__(self):
        return repr(self.data)

class LinkList:
    def __init__(self):
        self.head = Node()

    def __repr__(self):
        current_node = self.head.next
        nodes = []

        while current_node:
            nodes.append(repr(current_node))
            current_node = current_node.next

        return '.'.join(nodes)

    #Add a data as the firt item.
    def prepend(self, data):
        node = Node(data, self.head.next)
        self.head.next = node

    #Add a data as tail of the Linked list.
    def append(self, data):
        node = Node(data)
        if self.head.next == None:
            self.head.next = node
            return

        current_node = self.head.next
        while current_node.next:
            current_node = current_node.next

        current_node.next = node

    #Add a new data at a spacific position of Linked list.
    def insert(self, data, new_data):
        current_node = self.head.next

        while current_node:
            if current_node.data == data:
                node = Node(new_data, current_node.next)
                current_node.next = node
                break
            current_node = current_node.next

    #Remove the item from linked list.
    def remove(self, item):
        previous_node = self.head
        current_node = self.head.next

        while current_node:
            if current_node.data == item:
                break
            previous_node = current_node
            current_node = current_node.next

        if current_node is None:
            return
        if previous_node == self.head:
            previous_node.next = current_node.next
        else:
            previous_node.next= current_node.next

    #Search item to Linked list.
    def search(self, item):
        current_node = self.head.next

        while current_node:
            if current_node.data == item:
                return current_node
            current_node = current_node.next
        return None




if __name__ == '__main__':
    o = LinkList()
    o.append('A')
    o.append('B')
    o.prepend('a')
    print(o)
    o.insert('A', 'L')
    print(o)
    o.remove('B')
    print(o)
    print(o.search('a'))
