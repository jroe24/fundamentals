class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
    
    def make_withdraw(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print(f"Hello {self.name}, your account balance is {self.account_balance}.")

jacob1 = User("Jacob", "jroenavy24@gmail.com")
kyle1 = User("Kyle", "kyle@gmail.com")
alena1 = User("Alena", "alena@gmail.com")

jacob1.make_deposit(1000)
jacob1.make_deposit(1000)
jacob1.make_deposit(1000)
jacob1.make_withdraw(50)
jacob1.display_user_balance()

kyle1.make_deposit(1000)
kyle1.make_deposit(1000)
kyle1.make_withdraw(50)
kyle1.make_withdraw(100)
kyle1.display_user_balance()

alena1.make_deposit(1500)
alena1.make_withdraw(150)
alena1.make_withdraw(200)
alena1.make_withdraw(300)
alena1.display_user_balance()
