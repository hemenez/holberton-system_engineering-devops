# 0x15. API

## Synopsis
This project covers:
* What is an API and what is a REST API
* What are microservices
* What is the CSV format
* What is the JSON format

## Requirements
* Allowed editors: `vi`, `vim`, `emacs`
* All files will be interpreted/compiled on Ubuntu 14.04 LTS using `python3` (version 3.4.3)
* The first line of all files should be exactly `#!/usr/bin/python3`
* Libraries imported in your Python files must be organized in alphabetical order
* All files should end with a new line
* A `README.md` at the root of the folder of the project is mandatory
* Code should use the `PEP 8` style guide
* All files must be executalbe
* All modules should have documentation
* Code should not be executed when imported
* Must use `get` to access the dictionary value by key

## Environment
The project was tested and used on `Ubuntu 14.04 (trusty64)` via Vagrant run through VirtualBox.

## File Descriptions
This repository contains the following files. Listed are the parameters of each task:

### 0-gather_data_from_an_API.py

Write a Python script that, using this [REST API](https://jsonplaceholder.typicode.com/), for a given employee ID, returns information about his/her TODO list progress.

* You must use `urllib` or `requests` module
* The script must accept an integer as a parameter, which is the employee ID
* The script must display on the standard output the employee TODO list progress in this exact format:
  * First line: `Employee EMPLOYEE_NAME is done with tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):`
    * `EMPLOYEE_NAME`: name of the employee
    * `NUMBER_OF_DONE_TASKS`: number of completed tasks
    * `TOTAL_NUMBER_OF_TASKS`: total number of tasks, which is the sum of completed and non-completed tasks
  * Second and N next lines display the title of completed tasks: Tab `TASK_TITLE` (with 1 tabulation + 1 space before)

### 1-export_to_CSV.py

Using the previous file, extend your Python script to export data in the CSV format.

* Records all tasks that are owned by this employee
* Format must be: `"USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"`
* File name must be: `USER_ID.csv`

### 2-export_to_JSON.py

Using the first file, extend your Python script to export data in the JSON format.

* Records all tasks that are owned by this employee
* Format must be: `{ "USER_ID": [ {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}}, {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}}, ... ]}`
* File name must be: `USER_ID.json`

### 3-dictionary_of_list_of_dictionaries.py

Using the first file, extend your Python script to export data in the JSON format.

* Records all tasks from all employees
* Format must be: `{ "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ], "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ]}`
* File name must be: `todo_all_employees.json`