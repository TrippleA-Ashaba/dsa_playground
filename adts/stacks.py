class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.items:
            return self.items.pop()
        return "Stack empty"

    def is_empty(self):
        return len(self.items) == 0

    def print_items(self):
        return [i for i in self.items]

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


if __name__ == "__main__":
    a = Stack()
    a.push("RED")
    a.push("ORANGE")
    a.push("YELLOW")
    a.push("GREEN")

    # a.pop()
    # a.pop()
    # a.pop()
    # a.pop()
    # print(a.pop())

    print(a.print_items())

    print(a.is_empty())
    print(a.peek())
    print(a.size())
