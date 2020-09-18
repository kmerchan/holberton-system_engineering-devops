#!/usr/bin/python3
"""
defines function to query the Reddit API for number of subscribers
"""
def number_of_subscribers(subreddit):
    """
    queries the Reddit API
    returns the number of subscribers for a given reddit
    """
    import requests
    import json
    subreddit_URL = 'https://www.reddit.com/r/{}/about/.json'.format(
        subreddit)
    subreddit_info = requests.get(subreddit_URL,
                                  headers={"user-agent": "user"},
                                  allow_redirects=False).json()
    if "data" not in subreddit_info:
        return 0
    subscribers = subreddit_info.get("data").get("subscribers")
    return subscribers
