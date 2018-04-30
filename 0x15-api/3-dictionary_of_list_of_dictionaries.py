#!/usr/bin/python3
'''module uses api and handles employee information with it
by exporting info into a json file'''
import json
import requests


if __name__ == "__main__":
    my_user_url = 'https://jsonplaceholder.typicode.com/users'
#    todo = 'https://jsonplaceholder.typicode.com/todos/'
#    todo = 'https://jsonplaceholder.typicode.com/todos?userId='
    employee_response = requests.get(my_user_url)
    employee_data = employee_response.json()
#    print(len(employee_data))
#    employee_data = dict(employee_data)
#    name = employee_data.get('username')
#    print(todo_data)
    final_dict = {}
#    for l in employee_data:

#    for g in range(1, len(employee_data) + 1):
    my_dict = {}
    for g in employee_data:
        todo = 'https://jsonplaceholder.typicode.com/todos?userId='
        todo = todo + str(g.get('id'))
        todo_response = requests.get(todo)
        todo_data = todo_response.json()
        the_list = []
        for i in todo_data:
            my_dict = {}
            if i['userId'] == g.get('id'):
                my_dict['task'] = i.get('title')
                my_dict['completed'] = i.get('completed')
                my_dict['username'] = g.get('username')
                the_list.append(my_dict)
                final_dict[g.get('id')] = the_list
    my_file = 'todo_all_employees.json'
    with open(my_file, 'w') as f:
        json_obj = json.dumps(final_dict)
        f.write(json_obj)
#            for k, v in i.items():
#                if k != 'userId' and k != 'id':
#                    my_dict[k] = v
#            the_list.append(my_dict)
#        final_dict[g] = the_list
#        print(final_dict)

#            my_dict = i
#            the_list.append(my_dict)
#        final_dict[g] = the_list
#        print(final_dict)
#            my_dict = {}
#            for j in employee_data:
#                val = j['id']
#                if val == i.get('userId'):
#                    my_dict['task'] = i.get('title')
#                    my_dict['completed'] = i.get('completed')
#                    the_list.append(my_dict)
#    print(the_list)
#    total_dict = {}
#    linds_dict = {}
#    new_dict = {}
#    for a in todo_data:
#        print(a.get('userId'))
#        final_list = []
#        for b in employee_data:
#            if a.get('userId') == b.get('id'):
#                new_dict['task'] = a.get('title')
#                new_dict['username'] = b.get('username')
#                new_dict['completed'] = a.get('completed')
#        final_list.append(new_dict)
#    count = 0
#    for index in the_list:
#        for beeb in index:
#            print(index[beeb])
#        print(count)
#        count += 1
#    print(the_list)
#                    the_list.append(my_dict)
#        print(l['id'])
#    for me in the_list:
#        print(me)
#        final_dict[l['id']] = the_list
#    print(final_dict)
#    print()
#    print(final_dict)
#    print(i.get('userId'))
#        final_dict[i.get('userId')] = the_list
#    print(final_dict)
#    print()
#        print(i)
#        print()
#            my_dict['username'] = j.get('username')
#            the_list.append(my_dict)
#        print(the_list)
#        print(the_list)
#        final_dict[val] = the_list
#        print(final_dict)
