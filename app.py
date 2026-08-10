print("=== ChamaFlow ===")
print("1. Add member")
print("2. List members")
print("3. Record contribution")
print("4. View contributions")
print("5. Exit")
def show_menu():
    print("\n=== ChamaFlow ===")
    print("1. Add member")
    print("2. List members")
    print("3. Record contribution")
    print("4. View contributions")
    print("5. Exit")


def main():
    show_menu()


if __name__ == "__main__":
    main()
def add_member():
    name = input("Enter member name: ")
    phone = input("Enter phone number: ")

    with open("data/members.txt", "a") as file:
        file.write(f"{name} | {phone}\n")

    print("Member added successfully.")


def show_menu():
    print("\n=== ChamaFlow ===")
    print("1. Add member")
    print("2. List members")
    print("3. Record contribution")
    print("4. View contributions")
    print("5. Exit")


def main():
    show_menu()

    choice = input("Choose an option: ")

    if choice == "1":
        add_member()
    elif choice == "5":
        print("Goodbye!")
    else:
        print("That feature is not available yet.")


if __name__ == "__main__":
    main()