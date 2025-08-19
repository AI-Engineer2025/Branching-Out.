import json
from typing import List, Dict, Any


def load_users() -> List[Dict[str, Any]]:
    """Lädt alle Benutzer aus der JSON-Datei."""
    with open("users.json", "r", encoding="utf-8") as file:
        return json.load(file)


def filter_users_by_name(name: str) -> None:
    """Filtern nach Name"""
    users = load_users()
    filtered_users = [user for user in users if user.get("name", "").lower() == name.lower()]

    if filtered_users:
        print(f"Benutzer mit dem Namen '{name}':")
        for user in filtered_users:
            print(user)
    else:
        print(f"Keine Benutzer mit dem Namen '{name}' gefunden.")


def filter_users_by_age(age: int) -> None:
    """Filtern nach Alter"""
    users = load_users()
    filtered_users = [user for user in users if user.get("age") == age]

    if filtered_users:
        print(f"Benutzer mit dem Alter {age}:")
        for user in filtered_users:
            print(user)
    else:
        print(f"Keine Benutzer mit dem Alter {age} gefunden.")


def filter_users_by_email(email: str) -> None:
    """Filtern nach Email"""
    users = load_users()
    filtered_users = [user for user in users if user.get("email", "").lower() == email.lower()]

    if filtered_users:
        print(f"Benutzer mit der Email '{email}':")
        for user in filtered_users:
            print(user)
    else:
        print(f"Keine Benutzer mit der Email '{email}' gefunden.")


def main() -> None:
    """Main Funktion"""
    filter_option = input("What would you like to filter by? (name/age/email): ").strip().lower()

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filter_users_by_name(name_to_search)
    elif filter_option == "age":
        try:
            age_to_search = int(input("Enter an age to filter users: ").strip())
            filter_users_by_age(age_to_search)
        except ValueError:
            print("Bitte gib eine gültige Zahl für das Alter ein.")
    elif filter_option == "email":
        email_to_search = input("Enter an email to filter users: ").strip()
        filter_users_by_email(email_to_search)
    else:
        print("Filtering by that option is not yet supported.")


if __name__ == "__main__":
    main()
