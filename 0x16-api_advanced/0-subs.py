#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    url = 'https://www.reddit.com/r/' + subreddit + '/about/.json'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}
    response = requests.get(url, headers=headers)
    if response.status_code is not '200':
        return 0
    json_data = response.json()
    data_dict = json_data.get('data')
    for k, v in data_dict.items():
        if k == 'subscribers':
            return v
