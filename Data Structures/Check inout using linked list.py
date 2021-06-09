#This is a program that allows students to check in and check out at the campus using linked lists
from tabulate import tabulate


n = "yes"


class Node:
    def __init__(self, ID, name, email, time, date):
        self.ID = ID
        self.name = name
        self.email = email
        self.time = time
        self.date = date
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def search(self, ID):
        current = self.head
        while current is not None:
            if current.ID == ID:
                print(str(current.ID) + "   " + str(current.name) + "   " + str(current.email) + "   " + str(current.time)
                    + "   " + str(current.date))

            current = current.next
        return False

    def delete(self, ID):
        current = self.head
        if current is not None:
            if current.ID == ID:
                self.head = current.next
                curreht = None
                return

        while current is not None:
            if current.ID == ID:
                break
            prev = current
            current = current.next

        if current is None:
            return
        prev.next = current.next
        current = None

    def insert(self, ID, name, email, time, date):
        new_node = Node(ID, name, email, time, date)
        new_node.next = self.head
        self.head = new_node
        print("There is a new check in!/\n")

    def show(self):
        current =self.head
        while current:
            data = [[str(current.ID), str(current.name), str(current.email), str(current.time), str(current.date)]]
            print(tabulate(data, headers=["ID", "Name", "Email", "Time", "Date"]))
            current = current.next


llist = LinkedList()
first_node = Node(1, "Gihozo Lando", "g.lando@alustudent.com", "10:54", "3/3/2021")
llist.head = first_node
second_node = Node(2, "Barezi Julien", "b.julien@alustudent.com", "12:59", "3/4/2021")
first_node.next = second_node
third_node = Node(3, "Diane Niyibaruta", "d.niyibarut@alustudent.com", "11:32", "04/03/2021")
second_node.next = third_node



#running the program
while n != "no":
    print("\n\n**********************Welcome to ALU student check in program**********************\n\n")
    print("press 1 if you want to add a student")
    print("press 2 if you want to delete a student")
    print("press 3 if you want to search for a student")
    print("press 4 if you want to look at all the students in the system currently")
    print("press 5 if you want to exit!")
    # try:
    choice = input("Please enter your choice here!\n\n")
    # except:
    #     print("wrong choice")
    #     choice = input("Please enter your choice here!")

    if choice == "1":
        ID = input("enter student ID\n")
        name = input("enter student name\n")
        email = input("enter student email\n")
        time = input("enter the check in time\n")
        date = input("enter the check in date\n")
        llist.insert( ID, name, email, time, date)
        llist.show()
        n = input("Do you want to continue?\n"
                  "yes or no\n").lower()

    elif choice == "2":
        try:
            ID = int(input("Enter the student ID"))
            llist.delete(ID)
            llist.show()
        except:
            print("Enter another input")
            ID = int(input("Enter the student ID"))
            llist.delete(ID)
            llist.show()
        n = input("Do you want to continue?\n"
                  "yes or no\n").lower()

    elif choice == "3":
        try:
            ID = int(input("Enter the student ID"))
            llist.search(ID)
        except:
            print("Wrong input, try again")
            ID = int(input("Enter the student ID"))
            llist.search(ID)
        n = input("Do you want to continue?\n"
                  "yes or no\n").lower()

    elif choice == "4":
        llist.show()
        n = input("Do you want to continue?\n"
                  "yes or no\n").lower()

    elif choice == "5":
        print("Thank you for using us!")
        break