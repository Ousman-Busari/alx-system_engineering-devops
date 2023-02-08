#!/usr/bin/python3
"""
Gather data from an API, and for a given employee ID,
returns his/her TODO list
"""

import json
import requests
import sys


def export_to_json():
    id = sys.argv[1]
    employee = requests.get("https://jsonplaceholder.typicode.com/users/" +
                            id).json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos",
                         params={"userId": int(id)}).json()

    json_text = {}
    tasks = [{"task": t.get("title"), "completed": t.get("completed"),
              "username": employee.get("username")} for t in todos]
    json_text[id] = tasks

    with open("{}.json".format(id), "w") as json_file:
        json.dump(json_text, json_file)


if __name__ == "__main__":
    export_to_json()
