from Account import Account
from crypto import encrypt_file, load_key
import pickle


class PasswordFile:
    def __init__(self, master_key):
        self.master_key = master_key
        self.accounts = {}

    def get_accounts(self):
        return self.accounts.keys()

    def get_account_details(self, account_key):
        if account_key in self.accounts:
            return (account_key, self.accounts[account_key].details)

        raise ValueError("This service does not exist.")

    def add_account(self, key):
        self.accounts[key] = Account(key)

    def remove_account(self, key):
        self.accounts.pop(key)

    def save_to_file(self, file_name="password_file.pswd"):
        with open(file_name, "wb") as file:
            pickle.dump(self, file)

        encrypt_file(file_name, load_key(self.master_key))

    def menu(self):
        running = True

        while running:
            print("Welcome to your Password File")
            print("1. Get credentials")
            print("2. Add an account")
            print("3. Remove an account")
            print("4. Exit")
            choice = int(input("Your choice: "))

            if choice == 1:
                account = self.get_account_details(input("Service: "))
                print(account)

            elif choice == 2:
                self.add_account(input("Service: "))

            elif choice == 3:
                self.remove_account(input("Service: "))

            elif choice == 4:
                self.save_to_file()
                running = False

            else:
                print("Please choose a valid option.")

            self.save_to_file()
