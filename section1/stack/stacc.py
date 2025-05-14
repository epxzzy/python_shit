class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)  # O(1) time

    def pop(self):
        if not self.is_empty():
            return self.items.pop()  # O(1) time
        raise Exception("Stack Underflow")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


s = Stack()
s.push(10)
s.push(20)
print(s.pop())  # 20
print(s.peek())  # 10