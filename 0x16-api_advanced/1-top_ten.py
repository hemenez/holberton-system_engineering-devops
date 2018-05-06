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
        return 0
    json_data = response.json()
    data_dict = json_data.get('data')
    print(data_dict['children'][0]['data']['title'])
    after_val = data_dict['after']
    after_url = 'https://www.reddit.com/r/' + subreddit + '/hot.json?after='
    after_url += after_val
    after_r = requests.get(after_url, headers=headers)
    after_json = after_r.json()
    after_dict = after_json.get('data')
    print(after_dict['children'][0]['data']['title'])
    count = 1
    while count < 9:
        after_val = after_dict['after']
        after_url = 'https://www.reddit.com/r/' + subreddit
        after_url += '/hot.json?after=' + after_val
        after_r = requests.get(after_url, headers=headers)
        after_json = after_r.json()
        after_dict = after_json.get('data')
        print(after_dict['children'][0]['data']['title'])
        count += 1
