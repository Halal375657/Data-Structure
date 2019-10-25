#Doubly Linked List.
#Time for Result() method is O(n).
#Time for append() method is O(n).
#Time for prepend() method is O(1).
#Time for search() method is O(n).But it's for wrost case.
#Time for remove() method is O(n).But it's for wrost case.


class Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data, self.prev, self.next = data, prev, next

    def __repr__(self):
        return repr(self.data)

class DoublyLinkList:
    def __init__(self):
        self.head = Node()

    def Result(self):
        nodes = []
        current_node = self.head.next

        while current_node:
            nodes.append(current_node.data)
            current_node = current_node.next
        return nodes


    def append(self, data):
        node = Node(data)
        
        if self.head.next is None:
            self.head.next = node
            return

        current_node = self.head.next

        while current_node.next:
            current_node = current_node.next

        current_node.next = node
        node.prev = current_node

    def prepend(self, data):
        first_node = self.head.next
        new_node = Node(data, None, first_node)
        self.head.next = new_node

        if first_node:
            first_node.prev = new_node

    def Search(self, item):
        current_node = self.head.next

        while current_node.next:
            if current_node.data == item:
                return current_node
            current_node = current_node.next

        if current_node.data == item:
            return current_node
        else:
            return None

    def remove(self, item):
        previous_node = self.head
        current_node = previous_node.next

        while current_node.next:
            if current_node.data == item:
                break
            previous_node = current_node
            current_node = current_node.next

        previous_node.next = current_node.next
        #if, The current_node is not last node than do the assainment operation.
        if previous_node.next != None:
            previous_node.next.prev = previous_node

if __name__ == "__main__":
    o = DoublyLinkList()
    li = list(map(int, input().split()))
    for item in li:
        o.append(item)
    l = o.Result()
    print(l)
    o.prepend(10)
    l = o.Result()
    print(l)
    o.remove(10)
    l = o.Result()
    print(l)
