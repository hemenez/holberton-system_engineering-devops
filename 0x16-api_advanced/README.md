# 0x15. API

## Synopsis
This project covers:
* How to read API documentation to find the endpoints you’re looking for
* How to use an API with pagination
* How to parse JSON results from an API
* How to make a recursive API call
* How to sort a dictionary by value

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
* You must use the Requests module for sending HTTP requests to the Reddit API

## Environment
The project was tested and used on `Ubuntu 14.04 (trusty64)` via Vagrant run through VirtualBox.

## File Descriptions
This repository contains the following files. Listed are the parameters of each task:

### 0-subs.py

Write a function that queries the [Reddit API](https://www.reddit.com/dev/api/) and returns the number of subscribers (not active users, total subscribers) for a given subreddit. If an invalid subreddit is given, the function should return 0.

Hint: No authentication is necessary for most features of the Reddit API. If you’re getting errors related to Too Many Requests, ensure you’re setting a custom User-Agent.

* Prototype: `def number_of_subscribers(subreddit)`
* If not a valid subreddit, return 0.
* NOTE: Invalid subreddits may return a redirect to search results. Ensure that you are not following redirects.

### 1-top_ten.py

Write a function that queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit.

* Prototype: `def top_ten(subreddit)`
* If not a valid subreddit, print None.
* NOTE: Invalid subreddits may return a redirect to search results. Ensure that you are not following redirects.

### 2-recurse.py

Write a recursive function that queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit. If no results are found for the given subreddit, the function should return None.

Hint: The Reddit API uses pagination for separating pages of responses.

* Prototype: `def recurse(subreddit, hot_list=[])`
* Note: You may change the prototype, but it must be able to be called with just a subreddit supplied. AKA you can add a counter, but it must work without supplying a starting value in the main.
* If not a valid subreddit, return None.
* NOTE: Invalid subreddits may return a redirect to search results. Ensure that you are not following redirects.