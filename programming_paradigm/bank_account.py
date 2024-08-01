class BankAccount:
    def __init__(self, balance_account=0):
        self.balance_account = balance_account

    def deposit(self, amount):
        if amount > 0:
            self.balance_account += amount
            print(f"Deposited: ${amount}")
            return True
        return False

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance_account:
            self.balance_account -= amount
            print(f"Withdrew: ${amount}")
            return True
        else:
            print("Insufficient funds.")
            return False

    def display_balance(self):
        print(f"Current Balance: ${self.balance_account:.2f}")
