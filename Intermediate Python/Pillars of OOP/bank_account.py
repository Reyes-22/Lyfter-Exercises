class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        if amount > 0:
            print(f"Depositing {amount} to the account.")
            self.balance += amount

    def withdraw(self, amount):
        result = self.balance - amount

        if result >= 0:
            print(f"Withdrawing {amount} from the account.")
            self.balance -= amount
        else:
            print(f"Cannot withdraw {amount}. Insufficient balance.")


class SavingsAccount(BankAccount):
    def __init__(self, balance, min_balance):
        super().__init__()
        self.balance = balance
        self.min_balance = min_balance

    def withdraw(self, amount):
        result = self.balance - amount

        if result >= self.min_balance:
            super().withdraw(amount)
        else:
            print(
                f"Cannot withdraw {amount}. Minimum balance requirement not met.")


my_account = SavingsAccount(100, 50)
my_account.withdraw(70)
