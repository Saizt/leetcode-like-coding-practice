import heapq
class BankingSystem:

    def __init__(self):
        self.account = {}
        self.transaction_value = {}
        self.scheduled_payments = []
        self.pending_payments = {}
        self.canceled_payments = set()
        self.global_PID = 0


    def _process_payments(self, timestamp: int):
        while self.scheduled_payments and self.scheduled_payments[0][0] <= timestamp:
            execution_time, creation_order, payment_id, account_id, amount \
                = heapq.heappop(self.scheduled_payments)

            if payment_id in self.canceled_payments:
                self.canceled_payments.remove(payment_id)
                self.pending_payments.pop(payment_id, None)
                continue

            if payment_id not in self.pending_payments:
                continue

            account_id = self.pending_payments[payment_id]
            del self.pending_payments[payment_id]

            if self.account[account_id] >= amount:
                self.account[account_id] -= amount
                self.transaction_value[account_id] += amount


    def create_account(self, account_id: str) -> bool:
        if account_id in self.account:
            return False

        self.account[account_id] = 0
        self.transaction_value[account_id] = 0
        return True


    def deposit(self, account_id: str, amount: int, timestamp: int):
        self._process_payments(timestamp)

        if account_id not in self.account:
            return None

        self.account[account_id] += amount
        self.transaction_value[account_id] += amount

        return self.account[account_id]


    def transfer(self, 
                source_account_id: str, 
                target_account_id: str, 
                amount: int, 
                timestamp: int):
        self._process_payments(timestamp)

        if (source_account_id not in self.account
            or target_account_id not in self.account
            or source_account_id == target_account_id
            or self.account[source_account_id] < amount):
            return None

        self.account[source_account_id] -= amount
        self.account[target_account_id] += amount

        self.transaction_value[source_account_id] += amount
        self.transaction_value[target_account_id] += amount

        return self.account[source_account_id]


    def top_activity(self, n: int):
        return [
            account_id
            for account_id, activity in sorted(
                self.transaction_value.items(),
                key=lambda x: (-x[1], x[0]),
            )[:n]
        ]

    def schedule_payment(self,
                        timestamp: int,
                        account_id: str,
                        amount: int,
                        delay: int):
        self._process_payments(timestamp)

        if account_id not in self.account:
            return None

        self.global_PID += 1
        payment_id = f"payment{self.global_PID}"

        execution_time = timestamp + delay

        heapq.heappush(
            self.scheduled_payments,
            (
                execution_time,
                self.global_PID,
                payment_id,
                account_id,
                amount,
            ),
        )

        self.pending_payments[payment_id] = account_id
        return payment_id


    def cancel_payment(self,
                        timestamp: int,
                        account_id: str,
                        payment_id: str):
        self._process_payments(timestamp)

        if (
            payment_id not in self.pending_payments
            or self.pending_payments[payment_id] != account_id
        ):
            return False

        self.canceled_payments.add(payment_id)
        del self.pending_payments[payment_id]

        return True


    def merge_accounts(self,
                       timestamp: int, 
                       target_account_id: str, 
                       source_account_id: str):
        self._process_payments(timestamp)

        if source_account_id in self.account and \
            target_account_id in self.account and \
            source_account_id != target_account_id:
            self.account[target_account_id] += self.account[source_account_id]
            self.transaction_value[target_account_id] += self.transaction_value[source_account_id]
            for payment_id, account_id in self.pending_payments.items():
                if account_id == source_account_id:
                    self.pending_payments[payment_id] = target_account_id

            del self.account[source_account_id]
            del self.transaction_value[source_account_id]
            return True
        else:
            return False