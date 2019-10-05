class Queue:
    def __init__(self, size):
        self.size   = size
        self.q      = [0]*self.size
        self.tail, self.head  = 0, 0

    def enqueue(self, new_item):
        if self.tail == self.size:
            print("Queue is already full!")
        else:
            self.q[self.tail] = new_item
            self.tail = self.tail + 1

    def dequeue(self):
        if self.head == self.tail:
            item = "Item is not available"
        else:
            item = self.q[self.head]
            self.head = self.head + 1
        return item

if __name__=="__main__":
    size    = int(input("Enter Queue size:"))
    object  = Queue(size)
    object.enqueue("halal")
    object.enqueue("uddin")
    object.enqueue("rabbi")
    object.enqueue("halal")
    object.enqueue("uddin")
    object.enqueue("rabbi")
    while object.head != object.tail:
        item = object.dequeue()
        print(item)
