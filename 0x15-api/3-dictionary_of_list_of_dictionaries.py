#!/usr/bin/python3
"""exporting json format with api calling"""
import json
import requests

if __name__ == "__main__":
    base_link = "https://jsonplaceholder.typicode.com/"
    u = requests.get(base_link + "users").json()

    with open("todo_all_employees.json", "w") as javasonf:
        json.dump({
            u.get("id"): [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": u.get("username")
            } for t in requests.get(base_link + "todos",
                                    params={"userId": u.get("id")}).json()]
            for u in u}, javasonf)
