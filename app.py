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


def search_member():
    search_name = input("Enter member name to search: ").strip().lower()

    try:
        with open("data/members.txt", "r") as file:
            members = file.readlines()

        found = False

        print("\n=== Search Results ===")

        for member in members:
            if search_name in member.lower():
                print(member.strip())
                found = True

        if not found:
            print("No member found.")

    except FileNotFoundError:
        print("No members found.")


def record_contribution():
    name = input("Enter member name: ")
    amount = input("Enter contribution amount: ")

    with open("data/contributions.txt", "a") as file:
        file.write(f"{name} | {amount}\n")

    print("Contribution recorded successfully.")


def view_contributions():
    try:
        with open("data/contributions.txt", "r") as file:
            contributions = file.readlines()

        if not contributions:
            print("No contributions found.")
            return

        print("\n=== Contributions ===")

        total = 0

        for number, contribution in enumerate(contributions, start=1):
            print(f"{number}. {contribution.strip()}")

            parts = contribution.strip().split("|")
            amount = float(parts[1].strip())
            total += amount

        print(f"\nTotal contributions: {total:.2f}")

    except FileNotFoundError:
        print("No contributions found.")


def show_menu():
    print("\n=== ChamaFlow ===")
    print("1. Add member")
    print("2. List members")
    print("3. Member search")
    print("4. Record contribution")
    print("5. View contributions")
    print("6. Exit")


def main():
    show_menu()

    choice = input("Choose an option: ")

    if choice == "1":
        add_member()
    elif choice == "2":
        list_members()
    elif choice == "3":
        search_member()
    elif choice == "4":
        record_contribution()
    elif choice == "5":
        view_contributions()
    elif choice == "6":
        print("Goodbye!")
    else:
        print("That feature is not available yet.")


if __name__ == "__main__":
    main()
