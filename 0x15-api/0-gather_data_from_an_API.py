#!/usr/bin/python3
"""Get all todo list with with api request"""
import requests
import sys

if __name__ == "__main__":
    base_link = "https://jsonplaceholder.typicode.com/"
    u = requests.get(base_link + "users/{}".format(sys.argv[1])).json()
    taskss = requests.get(base_link + "todos", params={"userId": sys.argv[1]}).json()
    finished = [t.get("title") for t in taskss if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        u.get("name"), len(finished), len(taskss)))
    [print("\t {}".format(c)) for c in finished]
