import unittest

from customer import Customer

# initializing the customer account information


class Testcustomer(unittest.TestCase):

    # testing if the function c_transfer returns the right things when the password is not right
    # or when the amount inputted is greater than the balance

    def test_c_transfer(self):

        account1 = Customer("christian", "199290877464727", "780987122", 2000, 1234)

        amount = 50000
        self.assertGreater(amount, account1.balance)

        testamount = account1.c_transfer(50000, 1234)
        self.assertEqual(testamount, 0)

        testpassword = account1.c_transfer(1000, 2134)
        self.assertEqual(testpassword, "")

    # testing if c_withdraw function returns the right new balance if all conditions are met

    def test_c_withdraw(self):

        account1 = Customer("christian", "199290877464727", "780987122", 2000, 1234)

        testNewbalance = account1.c_withdraw(500, 1234)
        self.assertEqual(testNewbalance, 1475.0)

    # testing if c_payment returns the right balance when the password is right

    def test_c_payment(self):

        account1 = Customer("christian", "199290877464727", "780987122", 2000, 1234)

        testamount = account1.c_payment(1000, 1234)
        self.assertEqual(testamount, 1000)


if __name__ == '__main__':
    unittest.main()
