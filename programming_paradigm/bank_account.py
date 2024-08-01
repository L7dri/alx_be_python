# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        self._account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self._account_balance += amount
            return True
        return False

    def withdraw(self, amount):
        if amount > 0 and amount <= self._account_balance:
            self._account_balance -= amount
            return True
        return False

    def display_balance(self):
        return f"Current balance: ${self._account_balance:.2f}"

def main():
    parser = argparse.ArgumentParser(description="Bank Account Operations")
    
    parser.add_argument("--balance", type=float, default=0, help="Initial balance for the account")
    parser.add_argument("operation", choices=["deposit", "withdraw", "display"], help="Operation to perform")
    parser.add_argument("amount", nargs="?", type=float, help="Amount for the operation")
    
    args = parser.parse_args()
    
    account = BankAccount(args.balance)

    if args.operation == "deposit":
        if args.amount is not None and account.deposit(args.amount):
            print(f"Deposited: ${args.amount:.2f}")
        else:
            print("Deposit amount must be positive.")
    
    elif args.operation == "withdraw":
        if args.amount is not None and account.withdraw(args.amount):
            print(f"Withdrew: ${args.amount:.2f}")
        else:
            print("Insufficient funds or invalid withdraw amount.")
    
    elif args.operation == "display":
        print(account.display_balance())

if __name__ == "__main__":
    main()

