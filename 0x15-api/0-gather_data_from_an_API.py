#!/usr/bin/python3
"""gets api"""
import requests # for making http requests to get data from the internet
from sys import argv # for getting command line arguments


def todo(userid):
    """doc stringed"""
    name = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(
            userid)).json().get('name')
    tasks = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/todos'.format(
            userid)).json()
    tasksDone = ['\t {}\n'.format(dic.get('title')) for dic in tasks
                 if dic.get('completed')]
    if name and tasks:
        print("Employee {} is done with tasks({}/{}):".format
              (name, len(tasksDone), len(tasks)))
        print(''.join(tasksDone), end='')


if __name__ == "__main__":
    if len(argv) == 2:
        todo(int(argv[1]))
