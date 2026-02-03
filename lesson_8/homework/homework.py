#part1
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

    def walk(self):
        print(f"{self.name} is walking.")


class Cow(Animal):
    def make_sound(self):
        print(f"{self.name} says Moo!")

    def produce(self):
        print(f"{self.name} produces milk.")


class Chicken(Animal):
    def make_sound(self):
        print(f"{self.name} says Cluck!")

    def produce(self):
        print(f"{self.name} lays eggs.")


class Horse(Animal):
    def make_sound(self):
        print(f"{self.name} says Neigh!")

    def run(self):
        print(f"{self.name} is running fast!")


# ---- Testing the farm ----
cow = Cow("Bessie", 5)
chicken = Chicken("Lola", 2)
horse = Horse("Spirit", 7)

animals = [cow, chicken, horse]

for animal in animals:
    animal.eat()
    animal.sleep()
    animal.walk()
    animal.make_sound()
    print("-" * 30)

cow.produce()
chicken.produce()
horse.run()
#part2
import os

class Account:
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance


class Bank:
    def __init__(self):
        self.accounts = {}
        self.load_from_file()

    def create_account(self, name, initial_deposit):
        account_number = len(self.accounts) + 1001
        account = Account(account_number, name, initial_deposit)
        self.accounts[account_number] = account
        self.save_to_file()
        print(f"Account created successfully! Account Number: {account_number}")

    def view_account(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            print(f"Account Number: {account.account_number}")
            print(f"Name: {account.name}")
            print(f"Balance: {account.balance}")
        else:
            print("Account not found.")

    def deposit(self, account_number, amount):
        if amount <= 0:
            print("Invalid deposit amount.")
            return
        account = self.accounts.get(account_number)
        if account:
            account.balance += amount
            self.save_to_file()
            print("Deposit successful.")
        else:
            print("Account not found.")

    def withdraw(self, account_number, amount):
        account = self.accounts.get(account_number)
        if not account:
            print("Account not found.")
            return
        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif amount > account.balance:
            print("Insufficient balance.")
        else:
            account.balance -= amount
            self.save_to_file()
            print("Withdrawal successful.")

    def save_to_file(self):
        with open("accounts.txt", "w") as file:
            for acc in self.accounts.values():
                file.write(f"{acc.account_number},{acc.name},{acc.balance}\n")

    def load_from_file(self):
        if not os.path.exists("accounts.txt"):
            return
        with open("accounts.txt", "r") as file:
            for line in file:
                acc_no, name, balance = line.strip().split(",")
                self.accounts[int(acc_no)] = Account(int(acc_no), name, float(balance))


# ---- CLI Menu ----
bank = Bank()

while True:
    print("\n1. Create Account")
    print("2. View Account")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter name: ")
        deposit = float(input("Initial deposit: "))
        bank.create_account(name, deposit)

    elif choice == "2":
        acc_no = int(input("Account number: "))
        bank.view_account(acc_no)

    elif choice == "3":
        acc_no = int(input("Account number: "))
        amount = float(input("Deposit amount: "))
        bank.deposit(acc_no, amount)

    elif choice == "4":
        acc_no = int(input("Account number: "))
        amount = float(input("Withdraw amount: "))
        bank.withdraw(acc_no, amount)

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
