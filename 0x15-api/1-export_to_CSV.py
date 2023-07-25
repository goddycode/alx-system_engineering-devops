#!/usr/bin/python3
"""Script to export data in the CSV format"""
import csv
import requests

def get_user_data(user_id):
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception if the request fails
    return response.json()

def get_user_todos(user_id):
    url = "https://jsonplaceholder.typicode.com/todos"
    params = {"userId": user_id}
    response = requests.get(url, params=params)
    response.raise_for_status()  # Raise an exception if the request fails
    return response.json()

def export_to_csv(user_id, user_data, todos):
    filename = f"{user_id}.csv"
    with open(filename, "w", newline="") as csvfile:
        fieldnames = ["user_id", "username", "completed", "title"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, quoting=csv.QUOTE_MINIMAL)

        writer.writeheader()
        for todo in todos:
            writer.writerow({
                "user_id": user_id,
                "username": user_data["username"],
                "completed": todo["completed"],
                "title": todo["title"]
            })

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <user_id>")
        sys.exit(1)

    user_id = sys.argv[1]

    try:
        user_data = get_user_data(user_id)
        todos = get_user_todos(user_id)
        export_to_csv(user_id, user_data, todos)
        print(f"Data exported to {user_id}.csv successfully.")
    except requests.RequestException as e:
        print(f"Error: Unable to fetch data - {e}")
        sys.exit(1)

