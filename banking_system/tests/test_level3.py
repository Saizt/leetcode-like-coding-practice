import unittest

from banking_system import BankingSystem


class BankingSystemLevel3Test(unittest.TestCase):

    def setUp(self):
        self.bank = BankingSystem()

        self.bank.create_account("alice")
        self.bank.create_account("bob")

        self.bank.deposit("alice", 500, timestamp=1)
        self.bank.deposit("bob", 300, timestamp=2)

    def test_schedule_payment(self):
        payment_id = self.bank.schedule_payment(
            timestamp=10,
            account_id="alice",
            amount=100,
            delay=20,
        )

        self.assertEqual(payment_id, "payment1")

    def test_schedule_payment_missing_account(self):
        payment_id = self.bank.schedule_payment(
            timestamp=10,
            account_id="ghost",
            amount=100,
            delay=20,
        )

        self.assertIsNone(payment_id)

    def test_payment_ids_are_global_and_sequential(self):
        payment1 = self.bank.schedule_payment(
            timestamp=10,
            account_id="alice",
            amount=100,
            delay=20,
        )

        payment2 = self.bank.schedule_payment(
            timestamp=15,
            account_id="bob",
            amount=50,
            delay=10,
        )

        self.assertEqual(payment1, "payment1")
        self.assertEqual(payment2, "payment2")

    def test_cancel_payment(self):
        payment_id = self.bank.schedule_payment(
            timestamp=10,
            account_id="alice",
            amount=100,
            delay=20,
        )

        result = self.bank.cancel_payment(
            timestamp=15,
            account_id="alice",
            payment_id=payment_id,
        )

        self.assertTrue(result)

    def test_cannot_cancel_payment_from_wrong_account(self):
        payment_id = self.bank.schedule_payment(
            timestamp=10,
            account_id="alice",
            amount=100,
            delay=20,
        )

        result = self.bank.cancel_payment(
            timestamp=15,
            account_id="bob",
            payment_id=payment_id,
        )

        self.assertFalse(result)

    def test_cannot_cancel_missing_payment(self):
        result = self.bank.cancel_payment(
            timestamp=10,
            account_id="alice",
            payment_id="payment999",
        )

        self.assertFalse(result)

    def test_cannot_cancel_payment_twice(self):
        payment_id = self.bank.schedule_payment(
            timestamp=10,
            account_id="alice",
            amount=100,
            delay=20,
        )

        self.assertTrue(
            self.bank.cancel_payment(
                timestamp=15,
                account_id="alice",
                payment_id=payment_id,
            )
        )

        self.assertFalse(
            self.bank.cancel_payment(
                timestamp=16,
                account_id="alice",
                payment_id=payment_id,
            )
        )

    def test_scheduled_payment_executes_before_current_operation(self):
        self.bank.schedule_payment(
            timestamp=10,
            account_id="alice",
            amount=100,
            delay=20,
        )

        result = self.bank.deposit(
            "alice",
            50,
            timestamp=30,
        )

        self.assertEqual(result, 450)

    def test_successful_payment_contributes_to_activity(self):
        self.bank.schedule_payment(
            timestamp=10,
            account_id="alice",
            amount=100,
            delay=20,
        )

        self.bank.deposit(
            "bob",
            10,
            timestamp=30,
        )

        self.assertEqual(
            self.bank.top_activity(2),
            ["alice", "bob"],
        )

    def test_failed_payment_does_not_change_balance(self):
        self.bank.schedule_payment(
            timestamp=10,
            account_id="alice",
            amount=1000,
            delay=20,
        )

        result = self.bank.deposit(
            "alice",
            50,
            timestamp=30,
        )

        self.assertEqual(result, 550)

    def test_failed_payment_does_not_contribute_to_activity(self):
        self.bank.schedule_payment(
            timestamp=10,
            account_id="alice",
            amount=1000,
            delay=20,
        )

        self.bank.deposit(
            "bob",
            10,
            timestamp=30,
        )

        self.assertEqual(
            self.bank.top_activity(2),
            ["alice", "bob"],
        )

    def test_same_timestamp_payments_use_creation_order(self):
        self.bank.deposit(
            "alice",
            100,
            timestamp=5,
        )

        self.bank.schedule_payment(
            timestamp=10,
            account_id="alice",
            amount=400,
            delay=20,
        )

        self.bank.schedule_payment(
            timestamp=15,
            account_id="alice",
            amount=250,
            delay=15,
        )

        self.bank.deposit(
            "bob",
            1,
            timestamp=30,
        )

        self.assertEqual(
            self.bank.account["alice"],
            200,
        )

    def test_payment_does_not_execute_early(self):
        self.bank.schedule_payment(
            timestamp=10,
            account_id="alice",
            amount=100,
            delay=20,
        )

        result = self.bank.deposit(
            "alice",
            50,
            timestamp=29,
        )

        self.assertEqual(result, 550)

    def test_processed_payment_cannot_be_canceled(self):
        payment_id = self.bank.schedule_payment(
            timestamp=10,
            account_id="alice",
            amount=100,
            delay=20,
        )

        self.bank.deposit(
            "bob",
            1,
            timestamp=30,
        )

        result = self.bank.cancel_payment(
            timestamp=31,
            account_id="alice",
            payment_id=payment_id,
        )

        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()