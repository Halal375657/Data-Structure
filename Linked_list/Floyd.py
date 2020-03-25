
#
# Find first node of Cycle In A Linked List.
# Floyd's Algortithm,also called Har and Turtle Aglorithm.
# Time and Space both are  not O(n) complexity
# Here, Space complexity is O(1).
# Here, Time complixity is O(n).
#


# Create node
class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = Node()

    # Appending data in linked list
    def prepend(self, data):
        node  = Node(data)
        node.next = self.head
        self.head = node

    def makeCycle(self):
        llist.head.next.next.next.next.next = llist.head.next.next.next

    def getFirstNodeOfCycle(self):

        H = T1 = self.head

        while H.next.next:
            H = H.next.next
            T1 = T1.next

            # meeting point of H and T1
            if H == T1:
                break

        T2 = self.head
        while T2:
            # detected point first element
            if T1 == T2:
                return T1.data
            T2 = T2.next
            T1 = T1.next

    # print all nodes
    def printItems(self):
        temp = self.head
        
        while temp:
            print(temp.data, end = " ")
            temp = temp.next

if __name__=="__main__":
    llist = LinkedList()
    llist.prepend(1)
    llist.prepend(2)
    llist.prepend(3)
    llist.prepend(4)
    llist.prepend(5)
    llist.prepend(6)
    
    # Make cycle in this llist
    llist.makeCycle()
    res = llist.getFirstNodeOfCycle()
    print("First node is:", res) # 3

    
