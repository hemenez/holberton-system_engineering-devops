#!/usr/bin/python3
import requests


def number_of_subscribers(subreddit):
    url = 'https://www.reddit.com/r/' + subreddit + '/about/.json'
    UA_string = 'Mozilla/5.0 (Windows NT 6.1) '
    UA_string += 'AppleWebKit/537.36 (KHTML, like Gecko) '
    UA_string += 'Chrome/41.0.2228.0 Safari/537.36'
    headers = {'User-Agent': UA_string}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return 0
    json_data = response.json()
    data_dict = json_data.get('data')
    for k, v in data_dict.items():
        if k == 'subscribers':
            return v
