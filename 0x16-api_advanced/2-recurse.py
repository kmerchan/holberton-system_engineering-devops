#!/usr/bin/python3
"""
defines recursive function to query the Reddit API
for all hot articles of a given subreddit
"""


def recurse(subreddit, hot_list=[], count=0, after=None):
    """
    queries the Reddit API
    returns list of titles of hot posts for subreddit
    """
    import json
    import requests
    if count is 0:
        sub_URL= 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    else:
        sub_URL = 'https://www.reddit.com/r/{}/hot.json?count={}&after=={}'.\
        format(subreddit, count, after)
    subreddit_info = requests.get(sub_URL,
                                  headers={"user-agent": "user"},
                                  allow_redirects=False).json()
    if "data" not in subreddit_info and count is 0:
        return None
    elif "data" not in subreddit_info:
        return hot_list
    children = subreddit_info.get("data").get("children")
    for child in children:
        hot_list.append(child.get("data").get("title"))
        count += 1
        after = subreddit_info.get("after")
        print(count)
    return (recurse(subreddit, hot_list, count, after))
