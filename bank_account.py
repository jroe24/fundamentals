# class User:
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email
#         self.account_balance = 0

#     def make_deposit(self, amount):
#         self.account_balance += amount
#         return self
    
#     def make_withdraw(self, amount):
#         self.account_balance -= amount
#         return self
#     def display_user_balance(self):
#         print(f"Hello {self.name}, your account balance is {self.account_balance}.")
#         return self

class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self,amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        print(f"Hello user, your account balance is ${self.balance}.")
        return self

    def yield_interest(self, int_rate):
        if self.balance > 0:
            interest_amount = self.balance * int_rate
            self.balance += interest_amount
            return self

jacob1 = BankAccount(.03, 0)
kyle1 = BankAccount(.03, 0)
alena1 = BankAccount(.03, 0)

jacob1.deposit(100).deposit(100).deposit(100).withdraw(50).yield_interest(.03).display_account_info()
kyle1.deposit(1000).deposit(1000).withdraw(50).withdraw(50).withdraw(75).withdraw(50).yield_interest(.03).display_account_info()