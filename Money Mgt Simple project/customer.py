from account import Account

# defining customer class

class Customer(Account):
    """"This class inherits from the account class. The difference between the customer account
    and the business account is that in the customer account transactions require some transaction
    fees while for the business class all transactions are free."""

    pass

    # defining transfer method

    def c_transfer(self, amount, password):
        """In this method the user is going to transfer money to another account
         :return= the amount you transferred and the remaining balance"""

        amount2 = amount * 0.03
        amount3 = amount + amount2
        if amount3 > self.balance:
            return 0
        else:
            if password == self.password:
                self.balance -= amount3
                return self.balance
            else:
                return ""

    # defining withdraw

    def c_withdraw(self, amount, password):
        """"In this method the user inputs the amount of money they want to withdraw and then the password
         and the money is deducted from their balance plus the transaction fee.

         :return= It returns the amount withdrawn from your account and the
         remaining balance"""

        amount2 = amount * 0.05
        amount3 = amount + amount2
        if amount3 > self.balance:
            return 0
        else:
            if password == self.password:
                self.balance -= amount3
                return self.balance
            else:
                return ""

    # defining payment method

    def c_payment(self, amount, password):
        """"In this method, the user is asked to input the code of the business they want the money to,
         then the password and the money are reduced from their account.
         :return= the amount of money paid and the remaining balance"""

        if amount > self.balance:
            return 0
        else:
            if password == self.password:
                self.balance -= amount
                return self.balance
            else:
                return ""
