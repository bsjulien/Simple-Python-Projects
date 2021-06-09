# Implementing dequeue algorithm


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.last = None

    def enqueue(self, data):
        if self.last is None:
            self.head = Node(data)
            self.last = self.head
        else:
            self.last.next = Node(data)
            self.last = self.last.next

    def dequeue(self):
        if self.head is None:
            return None
        else:
            to_return = self.head.data
            self.head = self.head.next
            return to_return

    def print_all(self):
        el = []
        while self.head.next != None:
            self.head = self.head.next
            el.append(self.head.data)
        print(el)

a_queue = Queue()

a_queue.enqueue(1)
a_queue.enqueue(2)
a_queue.enqueue(3)

print(a_queue.print_all())
a_queue.dequeue()
# print(a_queue.print_all())