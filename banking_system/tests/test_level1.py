# run this from inside ./banking_system/ with
# python -m unittest tests.test_level1 -v
import unittest
from banking_system import BankingSystem


class BankingSystemLevel1Test(unittest.TestCase):

    def setUp(self):
        self.bank = BankingSystem()

    def test_create_account(self):
        self.assertTrue(self.bank.create_account("alice"))
        self.assertFalse(self.bank.create_account("alice"))

    def test_deposit(self):
        self.bank.create_account("alice")
        self.assertEqual(self.bank.deposit("alice", 100), 100)
        self.assertEqual(self.bank.deposit("alice", 50), 150)

    def test_deposit_nonexistent_account(self):
        self.assertIsNone(self.bank.deposit("ghost", 100))

    def test_transfer(self):
        self.bank.create_account("alice")
        self.bank.create_account("bob")
        self.bank.deposit("alice", 100)
        self.assertEqual(self.bank.transfer("alice", "bob", 40), 60)

    def test_transfer_insufficient_funds(self):
        self.bank.create_account("alice")
        self.bank.create_account("bob")
        self.bank.deposit("alice", 30)
        self.assertIsNone(self.bank.transfer("alice", "bob", 50))
        self.assertEqual(self.bank.account['alice'], 30)
        self.assertEqual(self.bank.account['bob'], 0)

    def test_transfer_missing_account(self):
        self.bank.create_account("alice")
        self.bank.deposit("alice", 100)
        self.assertIsNone(self.bank.transfer("alice", "bob", 40))

    def test_transfer_to_same_account(self):
        self.bank.create_account("alice")
        self.bank.deposit("alice", 100)
        self.assertIsNone(self.bank.transfer("alice", "alice", 40))


if __name__ == "__main__":
    unittest.main()