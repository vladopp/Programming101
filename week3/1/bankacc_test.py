import unittest
from bankacc import BankAccount


class BankAccountTest(unittest.TestCase):

    def setUp(self):
        self.bankacc = BankAccount("vlado", 100, "$")

    def test_parameter_constructor_working_properly(self):
        self.assertEqual(self.bankacc.getname(), 'vlado')
        self.assertEqual(self.bankacc.getamount(), 100)
        self.assertEqual(self.bankacc.getcurrency(), '$')

    def test_initializing_with_negative_balance(self):
        with self.assertRaises(ValueError):
            self.bankacc = BankAccount("vlado", -100, "$")

    def test_deposit_method(self):
        self.bankacc.deposit(20)
        self.assertEqual(self.bankacc.getamount(), 120)

    def test_deposit_with_negative_number(self):
        with self.assertRaises(ValueError):
            self.bankacc.deposit(-20)

    def test_balance_method(self):
        self.assertEqual(self.bankacc.balance(), 100)

    def test_withdraw_method_less_than_balance(self):
        self.assertTrue(self.bankacc.withdraw(80))
        self.assertEqual(self.bankacc.getamount(), 20)

    def test_withdraw_method_more_than_balance(self):
        self.assertFalse(self.bankacc.withdraw(120))

    def test_withdraw_method_with_negative_number(self):
        with self.assertRaises(ValueError):
            self.bankacc.withdraw(-20)

    def test_str_dundur(self):
        self.assertEqual(str(self.bankacc), "Bank account for {} with balance of {}{}".format(self.bankacc.getname(), self.bankacc.getamount(), self.bankacc.getcurrency()))

    def test_init__dundur(self):
        self.assertEqual(int(self.bankacc), self.bankacc.getamount())

    def test_transfer_true_case(self):
        self.bankacc2 = BankAccount("ivan", 50, "$")
        self.assertTrue(self.bankacc.transfer_to(self.bankacc2, 20))

    def test_transfer_false_case(self):
        self.bankacc2 = BankAccount("ivan", 50, "bitcoin")
        self.assertFalse(self.bankacc.transfer_to(self.bankacc2, 20))

    def test_transfer_to_with_negative_number(self):
        self.bankacc2 = BankAccount("ivan", 50, "$")
        with self.assertRaises(ValueError):
            self.bankacc.transfer_to(self.bankacc2, -20)

    def test_initial_history(self):
        self.assertEqual(self.bankacc.history(), ['Account was created'])

    def test_history_with_deposit(self):
        x = 500
        self.bankacc.deposit(x)
        self.assertEqual(self.bankacc.history(), ['Account was created', 'Deposited {}{}'.format(x, self.bankacc.getcurrency())])

    def test_history_with_balance_check(self):
        self.bankacc.balance()
        self.assertEqual(self.bankacc.history(), ['Account was created', 'Balance check -> {}{}'.format(self.bankacc.getamount(), self.bankacc.getcurrency())])

    def test_history_with_int_balance_check(self):
        int(self.bankacc)
        self.assertEqual(self.bankacc.history(), ['Account was created', '__int__ check -> {}{}'.format(self.bankacc.getamount(), self.bankacc.getcurrency())])

    def test_history_with_successful_withdraw(self):
        x = 20
        self.bankacc.withdraw(x)
        self.assertEqual(self.bankacc.history(), ['Account was created', '{}{} was withdrawed'.format(x, self.bankacc.getcurrency())])

    def test_history_with_unsuccessful_withdraw(self):
        x = 220
        self.bankacc.withdraw(x)
        self.assertEqual(self.bankacc.history(), ['Account was created', 'Withdraw for {}{} failed'.format(x, self.bankacc.getcurrency())])

    def test_history_with_successful_transfer(self):
        self.bankacc2 = BankAccount("ivan", 50, "$")
        x = 20
        self.bankacc.transfer_to(self.bankacc2, x)
        self.assertEqual(self.bankacc.history(), ['Account was created', 'Transfer to {} for {}{}'.format(self.bankacc2.getname(), x, self.bankacc.getcurrency())])
        self.assertEqual(self.bankacc2.history(), ['Account was created', 'Transfer from {} for {}{}'.format(self.bankacc.getname(), x, self.bankacc.getcurrency())])

if __name__ == '__main__':
    unittest.main()
