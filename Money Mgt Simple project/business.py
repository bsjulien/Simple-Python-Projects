from account import Account


# defining Business class

class Business(Account):
    """This class is a child class that inherits the characteristics from the main clas
    s account. the difference is that
    in this account all the transactions are free"""

    pass

    # defining transfer method

    def b_transfer(self, amount, password):
        """" In this method the user inputs the amount of money they want to withdraw and then
        the password and the money is reduced from their balance and does not remove the transaction fee.

        :return= amount transferred, account transferred too and the new balance"""

        if amount > self.balance:
            return 0
        else:
            if password == self.password:
                self.balance -= amount
                return self.balance
            else:
                return ""

    # defining withdraw

    def b_withdraw(self, amount, password):
        """" In this method, the program asks the user to input the phone number of the recipient of the cash,
         input the amount(by also checking if the amount doesn’t exceed what they have in the account),
         confirm the transfer by input the password and finally getting
         the confirmation message that the money has been transferred detailing the remaining amount
         and this is done for free.

         :return= the amount withdrawn and the remaining balance"""

        if amount > self.balance:
            return 0
        else:

            if password == self.password:
                self.balance -= amount
                return self.balance
            else:
                return ""
