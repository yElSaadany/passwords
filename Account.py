class Account:
    def __init__(self, key):
        self.key = key

        print("Create new account")
        print("1. ID/Password (most common)")
        print("2. Password only")
        print("3. Custom (Word in Progress)")
        choice = int(input("Your choice: "))

        if choice == 1:
            id = input("ID (email, nickname, ...): ")
            password = input("Password: ")

            self.details = {"ID": id, "Password": password}

        elif choice == 2:
            password = input("Password: ")
            self.details = {"Password": password}

        elif choice == 3:
            print("Custom login detail is in development.")

        else:
            print("Please choose a valid way of storing your credentials.")

    def get_key(self):
        return self.key

    def get_details(self):
        return self.details

    def set_key(self, key):
        self.key = key

    def set_one_detail(self, field, value):
        self.details[field] = value
