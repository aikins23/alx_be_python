class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if (amount <= 0):
            print(f"inavlid withdraw amount check your input")
            return False
        if (amount > self.account_balance):
            print(f"insufficient withdraw amount check your input")
        return False
        self.account_balance -= amount
        print(f"{amount} Withdrawn")
        return True

    def display_balance(self):
        print(f"Account Balance: {self.account_balance}")
