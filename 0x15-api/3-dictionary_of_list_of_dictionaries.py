#!/usr/bin/python3
"""
Script with Rest API
"""
import json
import requests
import sys

if __name__ == '__main__':

    api_url = 'https://jsonplaceholder.typicode.com'
    users_url = '{}/users'.format(api_url)
    todos_url = '{}/todos'.format(api_url)

    response_user = requests.get(users_url).json()

    response_final = requests.get(todos_url).json()

    users_tasks = {}
    tasks = []
    temp = {}

    for user in response_user:
        user_id = user.get('id')
        username = user.get('username')
        for task in response_final:
            temp['username'] = username
            temp['task'] = task['title']
            temp['completed'] = task['completed']
            tasks.append(temp)

        users_tasks[user_id] = tasks

    with open('todo_all_employees.json', 'w', encoding='utf-8') as json_file:
        json.dump(users_tasks, json_file)
