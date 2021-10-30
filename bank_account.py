class BankAccount:
    accounts = []
    def __init__(self, balance, interest_rate):
        self.balance = balance
        self.interest_rate = interest_rate
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        if(self.balance - amount) > 0:
            self.balance -= amount
        else: 
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self
    
    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self
    
    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.interest_rate)
        return self

Account1 = BankAccount(10000, .03)
Account1.deposit(20).deposit(25).deposit(20).withdraw(50).display_account_info().yield_interest()
Account2 = BankAccount(12000, .03)
Account2.deposit(10).deposit(60).withdraw(50).withdraw(20).withdraw(30).withdraw(100).display_account_info().yield_interest()