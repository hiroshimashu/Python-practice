class Stack:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def pop(self):
        return self.items.pop()
    def push(self, item):
        return self.items.append(item)
    def peek(self):
        return self.items[len(self.items) - 1]
    def size(self):
        return len(self.items)

def main():
    s = Stack()
    print(s.isEmpty())
    s.push(4)
    s.push('dog')
    print(s.peek())
    s.push("hiroshi")
    print(s.size())
    print(s.pop())
    print(s.pop())

main()