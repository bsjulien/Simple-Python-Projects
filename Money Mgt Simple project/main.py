# importing the accounts from accounts_def file
from pip._vendor.distlib.compat import raw_input

from accounts_def import account1
from accounts_def import account2

# importing the customer and business functions

import customer_func
import business_func

cont = "y"

# Welcoming message

print("\nWelcome to the Mobile Money service ---- Enjoy!!")

# starting a loop so that the user can be allowed to do more than one operation

while cont != "n":

    # Asking the user which account they have because there are two different types and each has its functions
    print("\n Please enter a name from an existing account")
    Username = raw_input("\n Your name: ").lower()

    # If they choose one we call methods from customer

    if Username == account1.name:

        # Creating the file with the username
        f = open(Username + ".txt", "a+")

        # writing in the file
        f.write("The user enters their name" + Username + "\n")

        # Message that indicates the choices the user can make

        print("\nWelcome Christian ---- customer account")
        print("\nSelect the operation you want to make:")
        print("\n1: Deposit Money")
        print("2: Withdraw Money")
        print("3: Check Balance")
        print("4: Transfer Money")
        print("5: Buy Electricity or Airtime")
        print("6: Pay a Business")
        try:
            query = int(input("\nYour choice: "))
        except:
            print("Please enter a valid input!")
            query = int(input("\nYour choice: "))

        # writing in the file
        f.write("The user typed what query they want to use: " + str(query) + "\n")

        # If condition to call functions based on the query input

        if query == 1:

            account1.deposit(f)

            cont = input("Do you want to do another operation?\n"
                         "y: yes\n"
                         "n: no\n")

            # writing in the file
            f.write("The user said if they want to continue or not: " + cont + "\n")

        elif query == 2:
            customer_func.withdraw(f)
            cont = input("Do you want to do another operation?\n"
                         "y: yes\n"
                         "n: no\n")

            # writing in the file
            f.write("The user said if they want to continue or not: " + cont + "\n")

        elif query == 3:
            account1.enquiry(f)
            cont = input("Do you want to do another operation?\n"
                         "y: yes\n"
                         "n: no\n")
            # writing in the file
            f.write("The user said if they want to continue or not: " + cont + "\n")

        elif query == 4:
            customer_func.transfer(f)
            cont = input("Do you want to do another operation?\n"
                         "y: yes\n"
                         "n: no\n")

            # writing in the file
            f.write("The user said if they want to continue or not: " + cont + "\n")

        elif query == 5:
            account1.buy(f)
            cont = input("Do you want to do another operation?\n"
                         "y: yes\n"
                         "n: no\n")

            # writing in the file
            f.write("The user said if they want to continue or not: " + cont + "\n")

        elif query == 6:
            customer_func.payment(f)
            cont = input("Do you want to do another operation?\n"
                         "y: yes\n"
                         "n: no\n")
            # writing in the file
            f.write("The user said if they want to continue or not: " + cont + "\n")

        else:
            print("Wrong choice!!!")

    # If they choose 2 we use methods from the business class

    elif Username == account2.name:

        # Creating the file with the username
        f = open(Username + ".txt", "a+")

        # writing in the file
        f.write("The user enters their name: " + Username + "\n")

        print("\nWelcome Kenny ---- Business account")
        print("\nSelect the operation you want to make:")
        print("\n1: Deposit Money")
        print("2: Withdraw Money")
        print("3: Check Balance")
        print("4: Transfer Money")
        print("5: Buy Electricity or Airtime")
        try:
            query = int(input("\nYour choice: "))
        except:
            print("Please enter a valid input!")
            query = int(input("\nYour choice: "))

        # writing in the file
        f.write("The user typed what query they want to use: " + str(query) + "\n")

        if query == 1:
            account2.deposit(f)
            cont = input("Do you want to do another operation?\n"
                         "y: yes\n"
                         "n: no\n")
            # writing in the file
            f.write("The user said if they want to continue or not: " + cont + "\n")

        elif query == 2:
            try:
                business_func.withdraw(f)
            except:
                business_func.withdraw(f)
            cont = input("Do you want to do another operation?\n"
                         "y: yes\n"
                         "n: no\n")
            # writing in the file
            f.write("The user said if they want to continue or not: " + cont + "\n")

        elif query == 3:
            account2.enquiry()
            cont = input("Do you want to do another operation?\n"
                         "y: yes\n"
                         "n: no\n")
            # writing in the file
            f.write("The user said if they want to continue or not: " + cont + "\n")

        elif query == 4:
            try:
                business_func.transfer(f)
            except:
                print("wrong input, try again!")
                business_func.transfer(f)
            cont = input("Do you want to do another operation?\n"
                         "y: yes\n"
                         "n: no\n")
            # writing in the file
            f.write("The user said if they want to continue or not: " + cont + "\n")

        elif query == 5:
            account2.buy(f)
            cont = input("Do you want to do another operation?\n"
                         "y: yes\n"
                         "n: no\n")
            # writing in the file
            f.write("The user said if they want to continue or not: " + cont + "\n")

        else:
            print("Wrong choice!!!")

    # else:
    #     print("Sorry that account doesn't exist!")
    #     exit()
