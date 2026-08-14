import unittest
from banking_system import BankingSystem


class BankingSystemLevel4Test(unittest.TestCase):

    def setUp(self):
        self.bank = BankingSystem()
        self.bank.create_account("alice")
        self.bank.create_account("bob")
        self.bank.create_account("charlie")
        self.bank.deposit("alice", 500, timestamp=1)
        self.bank.deposit("bob", 300, timestamp=2)
        self.bank.deposit("charlie", 200, timestamp=3)

    def test_merge_accounts(self):
        result = self.bank.merge_accounts(
            timestamp=10,
            target_account_id="alice",
            source_account_id="bob",
        )
        self.assertTrue(result)
        self.assertEqual(self.bank.account["alice"], 800)
        self.assertNotIn("bob", self.bank.account)

    def test_merge_combines_transaction_activity(self):
        self.bank.transfer("alice", "bob", 100, timestamp=5)
        self.bank.merge_accounts(
            timestamp=10,
            target_account_id="alice",
            source_account_id="bob",
        )
        self.assertEqual(self.bank.transaction_value["alice"], 1000)
        self.assertNotIn("bob", self.bank.transaction_value)

    def test_cannot_merge_account_with_itself(self):
        result = self.bank.merge_accounts(
            timestamp=10,
            target_account_id="alice",
            source_account_id="alice",
        )
        self.assertFalse(result)
        self.assertEqual(self.bank.account["alice"], 500)

    def test_cannot_merge_missing_source(self):
        result = self.bank.merge_accounts(
            timestamp=10,
            target_account_id="alice",
            source_account_id="ghost",
        )
        self.assertFalse(result)

    def test_cannot_merge_missing_target(self):
        result = self.bank.merge_accounts(
            timestamp=10,
            target_account_id="ghost",
            source_account_id="alice",
        )
        self.assertFalse(result)

    def test_source_account_no_longer_exists(self):
        self.bank.merge_accounts(
            timestamp=10,
            target_account_id="alice",
            source_account_id="bob",
        )
        self.assertIsNone(
            self.bank.deposit("bob", 100, timestamp=11)
        )

    def test_pending_payment_follows_merged_account(self):
        self.bank.schedule_payment(
            timestamp=5,
            account_id="bob",
            amount=200,
            delay=20,
        )
        self.bank.merge_accounts(
            timestamp=10,
            target_account_id="alice",
            source_account_id="bob",
        )
        self.bank.deposit("charlie", 1, timestamp=25)
        self.assertEqual(self.bank.account["alice"], 600)

    def test_pending_payment_keeps_same_id_after_merge(self):
        payment_id = self.bank.schedule_payment(
            timestamp=5,
            account_id="bob",
            amount=100,
            delay=30,
        )
        self.bank.merge_accounts(
            timestamp=10,
            target_account_id="alice",
            source_account_id="bob",
        )
        result = self.bank.cancel_payment(
            timestamp=15,
            account_id="alice",
            payment_id=payment_id,
        )
        self.assertTrue(result)

    def test_old_account_cannot_cancel_migrated_payment(self):
        payment_id = self.bank.schedule_payment(
            timestamp=5,
            account_id="bob",
            amount=100,
            delay=30,
        )
        self.bank.merge_accounts(
            timestamp=10,
            target_account_id="alice",
            source_account_id="bob",
        )
        result = self.bank.cancel_payment(
            timestamp=15,
            account_id="bob",
            payment_id=payment_id,
        )
        self.assertFalse(result)

    def test_due_payment_processed_before_merge(self):
        self.bank.schedule_payment(
            timestamp=5,
            account_id="bob",
            amount=100,
            delay=5,
        )
        self.bank.merge_accounts(
            timestamp=10,
            target_account_id="alice",
            source_account_id="bob",
        )
        self.assertEqual(self.bank.account["alice"], 700)

    def test_canceled_payment_not_restored_by_merge(self):
        payment_id = self.bank.schedule_payment(
            timestamp=5,
            account_id="bob",
            amount=100,
            delay=20,
        )
        self.assertTrue(
            self.bank.cancel_payment(
                timestamp=10,
                account_id="bob",
                payment_id=payment_id,
            )
        )
        self.bank.merge_accounts(
            timestamp=15,
            target_account_id="alice",
            source_account_id="bob",
        )
        self.bank.deposit("charlie", 1, timestamp=30)
        self.assertEqual(self.bank.account["alice"], 800)

    def test_target_and_source_pending_payments_both_survive(self):
        self.bank.schedule_payment(
            timestamp=5,
            account_id="alice",
            amount=100,
            delay=20,
        )
        self.bank.schedule_payment(
            timestamp=6,
            account_id="bob",
            amount=200,
            delay=19,
        )
        self.bank.merge_accounts(
            timestamp=10,
            target_account_id="alice",
            source_account_id="bob",
        )
        self.bank.deposit("charlie", 1, timestamp=25)
        self.assertEqual(self.bank.account["alice"], 500)


if __name__ == "__main__":
    unittest.main()