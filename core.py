def create_password_file():
    master_key = input("Choose a master key (leave empty to generate one): ")
    print(master_key)


def menu():
    print("Welcome to Passwords, a utility to store your passwords safely.")
    print("1. Open Password File")
    print("2. Create New Password File")
    print("3. Exit")
    choice = int(input("Your choice: "))

    if choice == 1:
        # TODO: open a password file
        print("Choice 1")
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
