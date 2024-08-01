class BankAccount:
  def __init__(self, balance_account):
    initial_account = 0
    self.balance_account = initial_account
    return
  def deposit(self, amount):
    if amount > 0 :
      self.balance_account += amount 
    print(f"Deposited: ${args.amount:.2f}")
    else ValueError :
    print(" Invalid amount ")
  def withdraw(self, amount):
    if amount <= self.balance_account and amount >0:
      self.balance_account -= amount 
      print(f"Withdrew: ${args.amount:.2f}")
    else 
      print("Insufficient funds.")
  def display_balance(self):
    print("Current balance: $" self.balance_account)
    return 
      
    

  
