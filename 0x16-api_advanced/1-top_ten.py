#!/usr/bin/python3
import requests


def top_ten(subreddit):
    url = 'https://www.reddit.com/r/' + subreddit + '/hot.json'
    UA_string = 'Mozilla/5.0 (Windows NT 6.1) '
    UA_string += 'AppleWebKit/537.36 (KHTML, like Gecko) '
    UA_string += 'Chrome/41.0.2228.0 Safari/537.36'
    headers = {'User-Agent': UA_string}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(None)
        return
    json_data = response.json()
    data_dict = json_data.get('data')
    count = 0
    while count < 10:
        print(data_dict['children'][count]['data']['title'])
        count += 1
