#!/usr/bin/python3
"""
defines recursive function to query the Reddit API
to parse title of all hot article and print sorted count
"""


def count_words(subreddit, word_list):
    """
    queries the Reddit API
    parses title of all hot articles
    prints sorted count of given keywords
    """
    import json
    import requests
    if after is None:
        sub_URL = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    else:
        sub_URL = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(
            subreddit, after)
    subreddit_info = requests.get(sub_URL,
                                  headers={"user-agent": "user"},
                                  allow_redirects=False).json()
    if "data" not in subreddit_info and hot_list == []:
        return None
    children = subreddit_info.get("data").get("children")
    for child in children:
        hot_list.append(child.get("data").get("title"))
        count += 1
    after = subreddit_info.get("data").get("after")
    if after is None:
        return hot_list
    return (recurse(subreddit, hot_list, after, count))
