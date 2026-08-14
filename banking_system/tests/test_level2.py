import unittest
from banking_system import BankingSystem


class BankingSystemLevel2Test(unittest.TestCase):

    def setUp(self):
        self.bank = BankingSystem()
        self.bank.create_account("alice")
        self.bank.create_account("bob")
        self.bank.create_account("charlie")

    def test_activity_from_deposits(self):
        self.bank.deposit("alice", 100)
        self.bank.deposit("bob", 150)
        self.bank.deposit("charlie", 100)
        self.assertEqual(self.bank.top_activity(3),
                         ["bob", "alice", "charlie"])

    def test_transfer_counts_for_both_accounts(self):
        self.bank.deposit("alice", 100)
        self.bank.deposit("bob", 150)
        self.bank.transfer("bob", "alice", 50)
        self.assertEqual(self.bank.top_activity(3),
                         ["bob", "alice", "charlie"])

    def test_limit_results(self):
        self.bank.deposit("alice", 100)
        self.bank.deposit("bob", 200)
        self.bank.deposit("charlie", 300)
        self.assertEqual(self.bank.top_activity(2),
                         ["charlie", "bob"])

    def test_failed_transfer_does_not_count(self):
        self.bank.deposit("alice", 30)
        self.bank.transfer("alice", "bob", 100)
        self.assertEqual(self.bank.top_activity(3),
                         ["alice", "bob", "charlie"])

    def test_accounts_with_zero_activity(self):
        self.assertEqual(self.bank.top_activity(3), 
                         ["alice", "bob", "charlie"])


if __name__ == "__main__":
    unittest.main()