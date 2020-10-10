from Account import Account
from crypto import encrypt_file, load_key
import pickle


class PasswordFile:
    """Class representation of a Password File.

    Attributes:
        master_key (str): Path to Key file used to open the Password File.
        accounts (dict): Holds all accounts.

    Note:
        An account is a object, check Account class.

    """

    def __init__(self, master_key):
        self.master_key = master_key
        self.accounts = {}

    def get_accounts(self):
        """Returns names of every service in the file."""
        return list(self.accounts.keys())

    def get_account_details(self, account_key):
        """Returns the details of a specific account.

        Args:
            account_key (str): Name of the service.
        
        Returns:
            A tuple with the name of the service and its details.

        """
        if account_key in self.accounts:
            return (account_key, self.accounts[account_key].details)

        raise ValueError("This service does not exist.")

    def add_account(self, key):
        self.accounts[key] = Account(key)

    def remove_account(self, key):
        self.accounts.pop(key)

    def save_to_file(self, file_name="password_file.pswd"):
        """Save the file to disk after encrypting it.

        Args:
            file_name (str): path to created file
        """
        with open(file_name, "wb") as file:
            pickle.dump(self, file)

        encrypt_file(file_name, load_key(self.master_key))

    def menu(self):
        """CLI menu to interact with the file."""
        running = True

        while running:
            print("Welcome to your Password File")
            print("1. Get credentials")
            print("2. Add an account")
            print("3. Remove an account")
            print("4. Exit")
            choice = int(input("Your choice: "))

            if choice == 1:
                c = 1
                accounts = self.get_accounts()
                print("-------------------------")
                for account in accounts:
                    print(f"{c}. {account}")
                    c += 1
                print("0. Exit")
                print("-------------------------")
                service = input("Service: ")
                if service != "0":
                    if service.isdigit():
                        try:
                            service = accounts[int(service) - 1]
                            account = self.get_account_details(service)
                            print(account)
                        except IndexError:
                            print("The number you entered is not on the list.")
                    else:
                        try:
                            account = self.get_account_details(service)
                            print(account)
                        except ValueError:
                            print("The service you entered is not on the list.")

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
