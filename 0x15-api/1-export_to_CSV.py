#!/usr/bin/python3
"""
uses REST API to gather data for employee to-do list
and exports information in CSV format to new file
"""
if __name__ == "__main__":
    import requests
    from sys import argv

    user_URL = 'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])
    employee = requests.get(user_URL).json()
    employ_username = employee.get('username')

    tasks_URL = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(
        argv[1])
    all_tasks = requests.get(tasks_URL).json()

    filename = "{}.csv".format(argv[1])
    with open(filename, 'w') as f:
        f.write("")
    for task in all_tasks:
        with open(filename, 'a', newline='') as f:
            f.write('"{}", "{}", "{}", "{}"\n'.format(
                argv[1], employ_username, task.get('completed'),
                task.get('title')))
