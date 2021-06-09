# Implementing a linked list

class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class linked_list:
    def __init__(self):
        self.head = node()

    def append(self, data):
        new_node = node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    def length(self):
        cur = self.head
        total = 0

        while cur.next != None:
            total += 1
            cur = cur.next

        return total

    def display(self):
        el = []
        cur = self.head

        while cur.next != None:
            cur = cur.next
            el.append(cur.data)
        print(el)

    def remove(self, data):
        cur = self.head
        while True:
            lastnode = cur
            cur = cur.next
            if cur.data == data:
                lastnode.next = cur.next
                return 


mylist = linked_list()

# Appending in the integer

mylist.append(1)
mylist.append(2)
mylist.append(3)
mylist.append(4)

# displaying the list
mylist.display()
mylist.remove(4)
mylist.display()
