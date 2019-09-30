'''
    Complixity of push() function:- O(1)
    Complicity of pop() function:- 0(1)
'''

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        #pop_value =  self.items[-1]
        #self.items = self.items[:-1]
        #return pop_value
        return self.items.pop()

    def is_empty(self):
        if self.items == []:
            return True
        return False

if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)

    while not s.is_empty():
        item = s.pop()
        print(item)
