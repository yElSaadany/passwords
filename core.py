from PasswordFile import PasswordFile
from crypto import decrypt_file, load_key, write_key
import pickle


def open_password_file(password_file: str = None, key_path: str = None) -> None:
    """Open a Password File if the right key file is given.

    Args:
        password_file (str): Path to Password File
        key_path (str): Path to Key file

    """
    if password_file is None:
        password_file = input("Path to password file: ")

    if key_path is None:
        key_path = input("Path to key file: ")

    decrypt_file(password_file, load_key(key_path))

    with open(password_file, "rb") as file:
        password_object = pickle.load(file)

    password_object.menu()


def create_password_file():
    """Creates a Password File by asking for a key."""
    print("-----------------------")
    print("1. Generate new key")
    print("2. Use existing key")
    choice = int(input("Choose an option: "))

    if choice == 1:
        key = input("Choose a name for your key: ")
        key = write_key(key)

    elif choice == 2:
        key = input("Path to key file: ")

    else:
        print("Please choose a valid option.")

    password_file = PasswordFile(key)
    password_file.save_to_file()
    open_password_file("password_file.pswd", key)


def menu():
    """Main CLI menu."""
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
    """Main loop."""
    running = True
    while running:
        running = menu()


if __name__ == "__main__":
    main()
