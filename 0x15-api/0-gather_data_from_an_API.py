#!/usr/bin/python3
"""
Gather data from an API, and for a given employee ID,
returns his/her TODO list
"""

import requests
import sys


def gather_data():
    id = sys.argv[1]
    employee = requests.get("https://jsonplaceholder.typicode.com/users/"
                            + id).json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos",
                         params={"userId": int(id)}).json()

    completed = [t for t in todos if t["completed"] is True]

    print("Employee {} is done with tasks({}/{}):".format(
        employee.get("name"), len(completed), len(todos)))
    [print("\t {}".format(c.get("title"))) for c in completed]


if __name__ == "__main__":
    gather_data()
