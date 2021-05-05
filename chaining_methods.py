class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    
    def make_withdraw(self, amount):
        self.account_balance -= amount
        return self
    def display_user_balance(self):
        print(f"Hello {self.name}, your account balance is {self.account_balance}.")
        return self

jacob1 = User("Jacob", "jroenavy24@gmail.com")
kyle1 = User("Kyle", "kyle@gmail.com")
alena1 = User("Alena", "alena@gmail.com")

jacob1.make_deposit(1000).make_deposit(1000).make_deposit(1000).make_withdraw(50).display_user_balance()

kyle1.make_deposit(1000).make_deposit(1000).make_withdraw(50).make_withdraw(100).display_user_balance()

alena1.make_deposit(1500).make_withdraw(150).make_withdraw(200).make_withdraw(300).display_user_balance()
