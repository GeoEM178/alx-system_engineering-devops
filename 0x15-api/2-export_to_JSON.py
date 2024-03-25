#!/usr/bin/python3
"""Exporting todos for user with api calling"""
import json
import sys
import requests

if __name__ == "__main__":
    u_unique_id = sys.argv[1]
    base_link = "https://jsonplaceholder.typicode.com/"
    u = requests.get(base_link + "users/{}".format(u_unique_id)).json()
    taskss = requests.get(base_link + "todos", params={"userId": u_unique_id}).json()
    u_name = u.get("username")
    with open("{}.json".format(u_unique_id), "w") as javasonf:
        json.dump({u_unique_id: [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": u_name
            } for t in taskss]}, javasonf)
