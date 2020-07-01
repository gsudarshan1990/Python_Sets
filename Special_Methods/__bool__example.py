class SavingsAccount:
    def __init__(self, owner, account_name):
        self.owner = owner
        self.account_name = account_name
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def __bool__(self):
        return self.balance >0

s1=SavingsAccount("John","23233")
s1.deposit(500)
print(bool(s1))
s1.withdraw(1000)
print(bool(s1))