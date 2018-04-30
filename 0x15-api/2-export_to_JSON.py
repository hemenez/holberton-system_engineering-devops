#!/usr/bin/python3
'''module uses api and handles employee information with it
by exporting info into a json file'''
import json
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]
    my_user_url = 'https://jsonplaceholder.typicode.com/users/' + employee_id
    todo = 'https://jsonplaceholder.typicode.com/todos?userId=' + employee_id
    employee_response = requests.get(my_user_url)
    employee_data = employee_response.json()
    employee_data = dict(employee_data)
    name = employee_data.get('username')
    todo_response = requests.get(todo)
    todo_data = todo_response.json()
    the_list = []
    final_dict = {}
    for i in todo_data:
        my_dict = {}
        for k, v in i.items():
            if k != 'userId' and k != 'id':
                my_dict[k] = v
                my_dict['name'] = name
                the_list.append(my_dict)
    final_dict[employee_id] = the_list
    my_file = employee_id + '.json'
    with open(my_file, 'w') as f:
        json_obj = json.dumps(final_dict)
        f.write(json_obj)
