class BankAccount:
    def __init__(self, account_holder, initial_balance = 0):
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Uang Masuk Rp{amount}. Saldo Baru: Rp{self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Saldo Tidak Cukup")
        else:
            self.balance -= amount
            print(f"{amount}. Sisa Saldo: Rp{self.balance}")

    def check_balance(self):
        print(f"Account holder: {self.account_holder}")
        print(f"Current balance: ${self.balance}")
