class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount()

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self
    
    def make_withdraw(self, amount):
        self.account.deposit(amount)
        return self
    
    def display_user_balance(self):
        print(f"Hello {self.name}, your account balance is {self.account.balance}.")
        return self

    def interest_yield(self):
        self.account.yield_interest()


class BankAccount:
    def __init__(self, int_rate = .03, balance = 0):
        self.int_rate = int_rate
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self,amount):
        self.balance -= amount
        return self

    def yield_interest(self):
        if self.balance > 0:
            interest_amount = self.balance * self.int_rate
            self.balance += interest_amount
            return self

jacob1 = User("Jacob", "Jacob@gmail.com")
kyle1 = User("Kyle", "Kyle@gmail.com")
alena1 = User("Alena", "Alena@gmail.com")

jacob1.make_deposit(500)
jacob1.display_user_balance()
jacob1.interest_yield()
jacob1.display_user_balance()
