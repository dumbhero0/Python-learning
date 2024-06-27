#Write a python program to create a class representing a stack data structure. Include methods for pushing and popping elements.
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from empty stack")

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def size(self):
        return len(self.items)
stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)



print("Current stack:", stack.items)
print("Popped item:", stack.pop())
print("Popped item:", stack.pop())

print("Current stack:", stack.items)
