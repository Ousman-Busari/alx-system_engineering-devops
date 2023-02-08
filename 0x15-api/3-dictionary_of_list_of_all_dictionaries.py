#!/usr/bin/python3
"""
Gather data from an API, and for a given employee ID,
returns his/her TODO list
"""

import json
import requests
import sys


def export_to_json():

    employees = requests.get("https://jsonplaceholder.typicode.com/users/")
    employees = employees.json()

    all_dict = {}
    for employee in employees:
        todos = requests.get("https://jsonplaceholder.typicode.com/todos",
                             params={"userId": int(employee.get("id"))}).json()

        tasks = [{"username": employee.get("username"), "task": t.get("title"),
                  "completed": t.get("completed")} for t in todos]

        all_dict[employee.get("id")] = tasks

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(all_dict, json_file)


if __name__ == "__main__":
    export_to_json()
