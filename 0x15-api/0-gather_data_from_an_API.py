#!/usr/bin/python3
'''module uses api and handles employee information with it'''
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]
    my_user_url = 'https://jsonplaceholder.typicode.com/users/' + employee_id
    todo = 'https://jsonplaceholder.typicode.com/todos?userId=' + employee_id
    employee_response = requests.get(my_user_url)
    employee_data = employee_response.json()
    employee_data = dict(employee_data)
    name = employee_data.get('name')
    todo_response = requests.get(todo)
    todo_data = todo_response.json()
    my_dict = {}
    count = 0
    for item in todo_data:
        my_dict[count] = item
        count += 1
    completion_count = 0
    total_count = 0
    my_text = []
    for key, val in my_dict.items():
        if val.get('completed') is True:
            my_text.append(val.get('title'))
            completion_count += 1
        total_count += 1
    print('Employee {} is done with tasks ({}/{}):'.format(name,
                                                           completion_count,
                                                           total_count))
    for i in my_text:
        print('\t {}'.format(i))
