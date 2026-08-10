from datetime import date


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
    contribution_date = date.today().isoformat()

    with open("data/contributions.txt", "a") as file:
        file.write(f"{name} | {amount} | {contribution_date}\n")

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

            if len(parts) >= 2:
                amount = float(parts[1].strip())
                total += amount

        print(f"\nTotal contributions: {total:.2f}")

    except FileNotFoundError:
        print("No contributions found.")


def contribution_history():
    search_name = input("Enter member name: ").strip().lower()

    try:
        with open("data/contributions.txt", "r") as file:
            contributions = file.readlines()

        found = False
        total = 0

        print("\n=== Member Contribution History ===")

        for contribution in contributions:
            parts = contribution.strip().split("|")

            if len(parts) < 2:
                continue

            name = parts[0].strip()
            amount = float(parts[1].strip())
            contribution_date = parts[2].strip() if len(parts) >= 3 else "Date unavailable"

            if search_name in name.lower():
                print(f"{name} | {amount:.2f} | {contribution_date}")
                total += amount
                found = True

        if found:
            print(f"\nTotal contributed: {total:.2f}")
        else:
            print("No contributions found for this member.")

    except FileNotFoundError:
        print("No contributions found.")


def dashboard():
    try:
        with open("data/members.txt", "r") as file:
            members = [member for member in file.readlines() if member.strip()]
        member_count = len(members)
    except FileNotFoundError:
        member_count = 0

    try:
        with open("data/contributions.txt", "r") as file:
            contributions = file.readlines()

        total = 0

        for contribution in contributions:
            parts = contribution.strip().split("|")

            if len(parts) >= 2:
                total += float(parts[1].strip())

    except FileNotFoundError:
        total = 0

    print("\n=== ChamaFlow Dashboard ===")
    print(f"Members: {member_count}")
    print(f"Total contributions: {total:.2f}")


def monthly_summary():
    month = input("Enter month (YYYY-MM): ").strip()

    try:
        with open("data/contributions.txt", "r") as file:
            contributions = file.readlines()

        found = False
        total = 0

        print(f"\n=== Monthly Contribution Summary: {month} ===")

        for contribution in contributions:
            parts = contribution.strip().split("|")

            if len(parts) < 3:
                continue

            name = parts[0].strip()
            amount = float(parts[1].strip())
            contribution_date = parts[2].strip()

            if contribution_date.startswith(month):
                print(f"{name} | {amount:.2f} | {contribution_date}")
                total += amount
                found = True

        if found:
            print(f"\nTotal for {month}: {total:.2f}")
        else:
            print("No contributions found for this month.")

    except FileNotFoundError:
        print("No contributions found.")


def show_menu():
    print("\n=== ChamaFlow ===")
    print("1. Add member")
    print("2. List members")
    print("3. Member search")
    print("4. Record contribution")
    print("5. View contributions")
    print("6. Member contribution history")
    print("7. Dashboard")
    print("8. Monthly contribution summary")
    print("9. Exit")


def main():
    dashboard()
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
        contribution_history()
    elif choice == "7":
        dashboard()
    elif choice == "8":
        monthly_summary()
    elif choice == "9":
        print("Goodbye!")
    else:
        print("That feature is not available yet.")


if __name__ == "__main__":
    main()
