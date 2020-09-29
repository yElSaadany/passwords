from PasswordFile import PasswordFile
import pickle


def open_password_file(password_file: PasswordFile = None):
    # TODO: manipulate password file after asking for master_key
    if password_file is None:
        path = input("Path to password file: ")
        with open(path, "rb") as file:
            password_file = pickle.load(file)

    password_file.menu()


def create_password_file():
    master_key = input("Choose a master key (leave empty to generate one): ")
    open_password_file(PasswordFile(master_key))
    print(master_key)


def menu():
    print("Welcome to Passwords, a utility to store your passwords safely.")
    print("1. Open Password File")
    print("2. Create New Password File")
    print("3. Exit")
    choice = int(input("Your choice: "))

    if choice == 1:
        # TODO: open a password file
        open_password_file()
        pass
    elif choice == 2:
        # TODO: create a password file
        create_password_file()
        pass
    elif choice == 3:
        print("Safely yours,")
        return False

    return True


def main():
    running = True
    while running:
        running = menu()


if __name__ == "__main__":
    main()
