Banking System

Implement a simple in-memory banking system.

The problem is divided into multiple levels. 
Do not assume functionality that has not yet been specified.

⸻

Level 1

The banking system should support creating accounts, depositing money, and transferring money between accounts.

Operations

create_account(account_id: str) -> bool

Creates a new account with the given account_id.

* A newly created account has a balance of 0.
* If the account does not already exist, create it and return True.
* If an account with the same ID already exists, make no changes and return False.

deposit(account_id: str, amount: int) -> int | None

Deposits amount into the specified account.

* If the account exists, increase its balance and return the new balance.
* If the account does not exist, return None.

transfer(source_account_id: str, target_account_id: str, amount: int) -> int | None

Transfers amount from the source account to the target account.

The transfer succeeds only if:

* both accounts exist
* the source and target accounts are different
* the source account has at least amount available

If the transfer succeeds:

* subtract amount from the source account
* add amount to the target account
* return the source account’s new balance

If the transfer cannot be completed, make no changes and return None.

Notes

You only need to implement the behavior described in Level 1.
Do not design functionality for hypothetical later levels.






⸻

Level 2

The banking system should now support ranking accounts by their total transaction activity.

All functionality from previous levels must continue to work.

Transaction Activity

Each account has a transaction value, defined as the total amount of money involved in its successful transactions.

The following operations contribute to transaction value:

* A successful deposit increases the receiving account’s transaction value by the deposited amount.
* A successful transfer increases the transaction value of both the source and target accounts by the transferred amount.

Creating an account does not contribute to transaction value.

Failed operations must not affect transaction values.

New Operation

top_activity(n: int) -> list[str]

Returns the IDs of up to n accounts with the highest transaction values.

Accounts should be ordered by:

1. Transaction value in descending order.
2. Account ID in ascending lexicographical order when transaction values are equal.

Accounts with zero transaction activity should still be included if needed to return up to n accounts.

If fewer than n accounts exist, return all existing accounts.

Requirements

* All Level 1 functionality must continue to behave as previously specified.
* Transaction activity must be updated only after successful operations.
* Account balances and transaction values represent separate concepts and must be maintained accordingly.





⸻

Level 3

The banking system should now support scheduled payments.

All functionality from previous levels must continue to work.

Scheduled Payments

A scheduled payment represents a future withdrawal from an account.

Scheduled payments must be processed in chronological order. If multiple payments have the same scheduled execution time, they must be processed in the order in which they were created.

New Operations

schedule_payment(timestamp: int, account_id: str, amount: int, delay: int) -> str | None

Schedules a payment from the specified account.

The payment must be scheduled for execution at timestamp + delay.

If the account does not exist, return None.

Otherwise, return a unique payment ID in the form paymentN, where N represents the global order in which scheduled payments were successfully created.

Scheduling a payment must not immediately modify the account balance or transaction activity.

cancel_payment(timestamp: int, account_id: str, payment_id: str) -> bool

Attempts to cancel a scheduled payment.

The cancellation succeeds only if the payment exists, belongs to the specified account, and has not already been processed or canceled.

Return True if the payment was successfully canceled. Otherwise, return False.

Payment Processing

Before performing any operation associated with a given timestamp, all scheduled payments with an execution time less than or equal to that timestamp must first be processed.

When a scheduled payment is processed:

* If the account has sufficient funds, subtract the payment amount from its balance and increase its transaction value by the payment amount.
* If the account has insufficient funds, do not modify its balance or transaction value.
* In either case, the payment is considered processed and must not be attempted again.

Canceled payments must not be processed.

Requirements

* All functionality from Levels 1 and 2 must continue to work.
* Scheduled payments must be processed before the operation occurring at the current timestamp.
* Payments scheduled for the same execution time must be processed in creation order.
* Only successfully executed payments contribute to transaction activity.
* A payment that has already been processed or canceled cannot be canceled.





⸻

Level 4

The banking system should now support merging accounts while preserving their balances, transaction activity, and scheduled payments.

All functionality from previous levels must continue to work.

Account Merging

Two existing accounts can be merged into a single account.

After a successful merge, the source account is removed from the banking system and its state is transferred to the target account.

New Operation

merge_accounts(timestamp: int, target_account_id: str, source_account_id: str) -> bool

Attempts to merge source_account_id into target_account_id.

Before performing the merge, all scheduled payments due at or before timestamp must be processed.

The merge succeeds only if:

* both accounts exist
* the target and source accounts are different

If either condition is not satisfied, return False and make no changes.

If the merge succeeds:

* Add the source account’s current balance to the target account’s balance.
* Add the source account’s transaction value to the target account’s transaction value.
* Remove the source account from the banking system.
* Return True.

Scheduled Payments

Pending scheduled payments associated with the source account must remain valid after the merge.

Such payments must become associated with the target account and execute against the target account’s balance at their originally scheduled execution times.

Their payment IDs and execution order must remain unchanged.

Pending scheduled payments already associated with the target account must also remain unchanged.

Canceled and already processed payments must not be restored or otherwise affected by the merge.

Account Identity

After a successful merge:

* The source account must no longer be considered an existing account.
* Operations using the removed source account ID must behave as they would for any other nonexistent account.
* The target account continues to use its original account ID.

Requirements

* All functionality from Levels 1–3 must continue to work.
* Due scheduled payments must be processed before the merge.
* Account balances and transaction values must be combined correctly.
* Pending scheduled payments must follow the merged account.
* Payment IDs and scheduled execution order must not change.
* A failed merge must not modify any banking-system state.