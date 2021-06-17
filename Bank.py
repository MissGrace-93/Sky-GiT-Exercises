class Bank_account:
    bank = "barclays" # class variable
    def __init__(self, type, number, name, balance, overdraft):
        self.type = type
        self.number = number
        self.name = name
        self.balance = balance
        self.overdraft = overdraft

    def get_balance(self):
        return f"Your balance is £{self.balance}"

    def withdraw_cash(self, withdrawal):
        current_balance = int(self.balance - withdrawal)
        return f"You've withdrawn: £{withdrawal}. Your current balance is £{current_balance}."


account_1 = Bank_account("current", "123456", "Marina", 10000, 0)
print(account_1.get_balance())
print(account_1.withdraw_cash(100))

account_2 = Bank_account("Savings", "123477", "Grace", 5050, 200)
print(account_2.get_balance())
print(account_2.withdraw_cash(100))

account_3 = Bank_account("ISA", "123499", "Mike", 7856, 600)
print(account_3.get_balance())
print(account_3.withdraw_cash(100))

account_3.balance = 0