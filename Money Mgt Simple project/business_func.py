# calling the file with the business account information

from accounts_def import account2


# Function that calls the transfer method in business

def transfer(f):
    print("\nYou are about to transfer money ------")
    try:
        phonenbr = int(input("\nPhone number: "))
    except:
        print('\n please enter a valid input!')
        phonenbr = int(input("\nPhone number: "))

    try:
        amount = int(input("Amount: "))
    except:
        print('\n please enter a valid input!')
        amount = int(input("Amount: "))
    # writing in the file
    f.write("The user enters the phone number they want to transfer money to: " + str(phonenbr) + "\n")
    f.write("The user enters the amount they want to transfer: " + str(amount) + "\n")

    # calling the b_transfer method from business class
    test_amount = account2.b_transfer(amount, 0)

    if test_amount == 0:
        print("Insufficient balance")
        exit()

    print("\nYou are transferring", amount, "RWF to", phonenbr)

    try:
        password = int(input("\nEnter the password to confirm: "))
    except:
        print("\n please enter a valid input")
        password = int(input("\nEnter the password to confirm: "))
    # writing in the file
    f.write("The user enters their password: " + str(password) + "\n")

    # calling the b_transfer method from the business class
    result = account2.b_transfer(amount, password)

    if result != "":
        print("\nYou have successfully transferred money")
        print("Your new balance is: ", result, "RWF")
    else:
        print("Invalid Password")


# Function that calls the withdraw method in business

def withdraw(f):
    print("\nYou are about to withdraw money ------")
    try:
        amount = int(input("\nAmount: "))
    except:
        print("\n please enter a valid input!")
        amount = int(input("\nAmount: "))

    # writing in the file
    f.write("The user enters the amount they want to transfer: " + str(amount) + "\n")

    # calling the b_withdraw method from business class
    test_amount = account2.b_withdraw(amount, 0)

    if test_amount == 0:
        print("Insufficient balance")
        exit()

    print("\nYou are withdrawing", amount, "RWF")
    try:
        password = int(input("\nEnter the password to confirm: "))
    except:
        print('please enter a valid input')
        password = int(input("\nEnter the password to confirm: "))
    # writing in the file
    f.write("The user enters their password: " + str(password) + "\n")

    # calling the b_withdraw method from business class
    result = account2.b_withdraw(amount, password)

    if result != "":
        print("\nYou have successfully withdrawn money")
        print("Your new balance is: ", result, "RWF")
    else:
        print("Invalid Password")



