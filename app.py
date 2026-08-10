def add_member():
    name = input("Enter member name: ")
    phone = input("Enter phone number: ")

    with open("data/members.txt", "a") as file:
        file.write(f"{name} | {phone}\n")

    print("Member added successfully.")


def list_members():
    try:
        with open("data/members.txt", "r") as file:
            members = file.readlines()

        if not members:
            print("No members found.")
            return

        print("\n=== Members ===")

        for number, member in enumerate(members, start=1):
            print(f"{number}. {member.strip()}")

    except FileNotFoundError:
        print("No members found.")


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
elif choice == "2":
    list_members()
elif choice == "3":
    print("Member search coming soon.")
elif choice == "5":
        print("Goodbye!")
    else:
        print("That feature is not available yet.")


if __name__ == "__main__":
    main()