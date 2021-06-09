import unittest

from business import Business

# initializing the business account information

account2 = Business("kenny", "19920010877490827", "788978742", 25000, 4321)


class Testbusiness(unittest.TestCase):

    # testing if the function b_transfer returns the right things when the password is not right
    # or when the amount inputted is greater than the balance

    def test_b_transfer(self):

        account2 = Business("kenny", "19920010877490827", "788978742", 25000, 4321)

        amount = 30000
        self.assertGreater(amount, account2.balance)

        testamount = account2.b_transfer(30000, 4321)
        self.assertEqual(testamount, 0)

        testpassword = account2.b_transfer(4000, 9087)
        self.assertEqual(testpassword, "")

    # testing if the function b_withdraw return the right New balance when all conditions are met

    def test_b_withdraw(self):

        account2 = Business("kenny", "19920010877490827", "788978742", 25000, 4321)

        testNewbalance = account2.b_withdraw(2000, 4321)
        self.assertEqual(testNewbalance, 23000)


if __name__ == '__main__':
    unittest.main()
