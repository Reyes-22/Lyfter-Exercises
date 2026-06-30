class BankAccount:
    balance = 0

    def deposit(self, amount):
        if amount > 0:
            print(f"Depositing {amount} to the account.")
            self.balance += amount

    def withdraw(self, amount):
        result = self.balance - amount

        if result > self.minimum_balance:
            print(f"Withdrawing {amount} from the account.")
            self.balance -= amount
        else:
            print(
                f"Cannot withdraw {amount}. Minimum balance requirement not met.")


class SavingsAccount(BankAccount):
    def __init__(self, minimum_balance):
        self.minimum_balance = minimum_balance


my_account = SavingsAccount(100)
my_account.withdraw(50)
