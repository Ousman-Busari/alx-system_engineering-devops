#!/usr/bin/python3
"""
Gather data from an API, and for a given employee ID,
returns his/her TODO list
"""

import csv
import requests
import sys


def export_to_csv():
    id = sys.argv[1]
    employee = requests.get("https://jsonplaceholder.typicode.com/users/" +
                            id).json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos",
                         params={"userId": int(id)}).json()

    with open("{}.csv".format(id), "w") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [employee.get("id"), employee.get("username"),
             t.get("completed"), t.get("title")]) for t in todos
         ]


if __name__ == "__main__":
    export_to_csv()
