# calling the file with the customer account information

from accounts_def import account1


# Function that calls the transfer method in customer

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

    # calling the c_transfer method from customer class
    test_amount = account1.c_transfer(amount, 0)

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

    # calling the c_transfer method from the customer class
    result = account1.c_transfer(amount, password)

    if result != "":
        print("\nYou have successfully transferred money")
        print("Your new balance is: ", result, "RWF")
    else:
        print("Invalid Password")


# Function that calls the withdraw method in customer

def withdraw(f):
    print("\nYou are about to withdraw money ------")

    try:
        amount = int(input("\nAmount: "))
    except:
        print("\n please enter a valid input!")
        amount = int(input("\nAmount: "))
    trans_fee = amount * 0.05

    # writing in the file
    f.write("The user enters the amount they want to transfer: " + str(amount) + "\n")

    # calling the c_withdraw method from customer class
    test_amount = account1.c_withdraw(amount, 0)

    if test_amount == 0:
        print("Insufficient balance")
        exit()

    print("\nYou are withdrawing", amount, "RWF")
    print("The transaction fee is: ", trans_fee)

    try:
        password = int(input("\nEnter the password to confirm: "))
    except:
        print('please enter a valid input')
        password = int(input("\nEnter the password to confirm: "))

    # writing in the file
    f.write("The user enters their password: " + str(password) + "\n")

    # calling the c_withdraw method from customer class
    result = account1.c_withdraw(amount, password)

    if result != "":
        print("\nYou have successfully withdrawn money")
        print("Your new balance is: ", result, "RWF")
    else:
        print("Invalid Password")


# Function that calls the payment method in customer

def payment(f):
    print("You are about to make a payment -----")

    payment_reason = input("\nReason for Payment: ")

    try:
        code = int(input("Code of the business: "))
    except:
        print("\n please enter a valid input")
        code = int(input("Code of the business: "))
    try:
        amount = int(input("\nAmount: "))
    except:
        print("\n please enter a valid input!")
        amount = int(input("\nAmount: "))

    # writing in the file

    f.write("The user enters the reason for payment: " + payment_reason + "\n")
    f.write("The user enters the business code they want to pay: " + str(code) + "\n")
    f.write("The user enters the amount they want to transfer: " + str(amount) + "\n")

    # calling the c_withdraw method from customer class

    test_amount = account1.c_withdraw(amount, 0)

    if test_amount == 0:
        print("\nInsufficient balance")
        exit()

    print("\nYou are paying", amount, "RWF to", code, "(Business code) for", payment_reason)

    password = int(input("\nEnter the password to confirm: "))

    # writing in the file

    f.write("The user enters their password: " + str(password) + "\n")

    # calling the c_payment method in customer class

    result = account1.c_payment(amount, password)

    if result != "":
        print("\nYou have successfully paid for", payment_reason)
        print("Your new balance is: ", result, "RWF")
    else:
        print("Invalid Password")


