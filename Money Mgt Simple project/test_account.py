import unittest
from account import Account


# initializing the business account information
account1 = Account("Christian", "199290877464727", "0780987122", 2000, 1234)


class MyTestCase(unittest.TestCase):

    # testing if the functions in Account returns the right things when the password is right
    # or when the amount inputted is greater than the balance

    def test_enquiry(self):
        self.assertEqual(account1.balance, 2000)

    def test_deposit(self):
        amount = 1000
        self.assertEqual(account1.balance+amount, 3000)

    def test_buy(self):
        amount = 1000
        self.assertEqual(account1.balance-amount, 1000)

    def test_password(self):
        self.assertEqual(account1.password, 1234)

    def test_name(self):
        self.assertEqual(account1.name, "Christian")


if __name__ == '__main__':
    unittest.main()