# Implementing a doubly linked list

class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList():
    def __init__(self):
        self.head = node()

    def append(self, data):
        new_node = node(data)
        cur = self.head

        while cur.next is not None:
            cur = cur.next

        cur.next = new_node
        new_node.prev = cur
        new_node.next = None

    def insert(self, data, key):
        cur = self.head
        while cur:
            if cur.next is None and cur.data == key:
                self.append(data)
                return
            elif cur.data == key:
                new_node = node(data)
                nxt = cur.next
                cur.next = new_node
                new_node.next = nxt
                new_node.prev = cur
                nxt.prev = new_node
            cur = cur.next

    def delete(self, data):
        cur = self.head
        while cur:
            if cur.data == data and cur == self.head:
                if not cur.next:
                    cur = None
                    self.head = None
                else:
                    nxt = cur.next
                    cur.next = None
                    nxt.prev = None
                    cur = None
                    self.head = nxt
                    return
            elif cur.data == data:
                if cur.next:
                    nxt = cur.next
                    prev = cur.prev
                    prev.next = nxt
                    nxt.prev = prev
                    cur.next = None
                    cur.prev = None
                    cur = None
                    return
                else:
                    prev = cur.prev
                    prev.next = None
                    cur.prev = None
                    cur = None
                    return

            cur = cur.next

    def display(self):
        el = []
        cur = self.head
        while cur.next != None:
            cur = cur.next
            el.append(cur.data)
        print(el)


mylist = DoublyLinkedList()

mylist.append(1)
mylist.append(2)
mylist.append(3)
mylist.append(4)

mylist.display()

mylist.insert(8, 2)

mylist.display()

mylist.delete(4)

mylist.display()
