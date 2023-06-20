class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0

    def get_size(self):
        return len(self.queue)

    def peek(self):
        return self.queue[0]


if __name__ == "__main__":
    a = Queue()

    a.enqueue(10)
    a.enqueue(20)
    a.enqueue(30)

    print(a.peek())
    a.dequeue()
    print(a.peek())
    print(a.get_size())
