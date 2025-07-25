import json


def filter_users_by_name(name):
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["name"].lower() == name.lower()]

    for user in filtered_users:
        print(user)


def filter_users_by_age(age: int):
    with open("users.json", "r") as file:
        users = json.load(file)
    filtered_users = [user for user in users if user.get("age") == age]

    if filtered_users:
        print(f"Benutzer mit dem Alter {age}:")
        for user in filtered_users:
            print(user)
    else:
        print(f"Keine Benutzer mit dem Alter {age} gefunden.")


if __name__ == "__main__":
    filter_option = input("What would you like to filter by?: ").strip().lower()

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filter_users_by_name(name_to_search)
    elif filter_option == "age":
        age_to_search = int(input("Enter an age to filter users: "))
        filter_users_by_age(age_to_search)
    else:
        print("Filtering by that option is not yet supported.")
