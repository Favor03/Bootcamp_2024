import datetime
class BankAccount:

    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
        self.transactions = []

    def view_balance(self):
        self.transactions.append("View Balance")
        print(f"Balance for account {self.account_number}: {self.balance}")

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid amount")
        elif amount < 100:
            print("Minimum deposit is 100")
        else:
            self.balance += amount
            self.transactions.append(f"\nDeposit: {amount} day: {datetime.date.today()} hour: {datetime.datetime.now()}\n")
            print("Deposit Succcessful")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Funds")
        else:
            self.balance -= amount
            self.transactions.append(f"\nWithdraw: {amount} day: {datetime.date.today()} hour: {datetime.datetime.now()}\n")
            print("Withdraw Approved")
            return amount

    def view_transactions(self):
        print("Transactions:")
        print("-------------")
        for transaction in self.transactions:
            print(transaction)


my_account = BankAccount(123656, 1000)

my_account.deposit(80000)
my_account.view_balance()
my_account.withdraw(55000)
my_account.view_balance()

my_account.view_transactions()
