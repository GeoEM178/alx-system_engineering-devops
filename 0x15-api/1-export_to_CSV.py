#!/usr/bin/python3
"""exportiing a xl file frrom api calling"""
import sys
import requests
import csv

if __name__ == "__main__":
    u_unique_id = sys.argv[1]
    base_link = "https://jsonplaceholder.typicode.com/"
    u = requests.get(base_link + "users/{}".format(u_unique_id)).json()
    taskss = requests.get(base_link + "todos", params={"userId": u_unique_id}).json()
    u_name = u.get("username")
    with open("{}.csv".format(u_unique_id), "w", newline="") as xlfle:
        writer = csv.writer(xlfle, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [u_unique_id, u_name, t.get("completed"), t.get("title")]
         ) for t in taskss]
