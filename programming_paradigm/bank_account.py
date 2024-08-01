class BankAccount:
  def __init__(self, balance_account):
    initial_account = 0
    self.balance_account = initial_account
    return
  def deposit(self, amount):
    if amount > 0 :
      self.balance_account += amount 
    print("Deposited: $"amount);
    else ValueError :
    print(" Invalid amount ");
  def withdraw(self, amount):
    if amount <= self.balance_account and amount >0:
      self.balance_account -= amount 
      print("Withdrew: $" amount)
    else 
      print("Insufficient funds.")
  def display_balance(self):
    print("Current Balance: $" self.balance_account)
    return 
    

  
