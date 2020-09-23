#!/usr/bin/python3
"""
defines recursive function to query the Reddit API
to parse title of all hot article and print sorted count
"""


def count_words(subreddit, word_list, after=None, count={}):
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
    for word in word_list:
        word = word.lower()
        if word not in count.keys():
            count[word] = 0
    if "data" not in subreddit_info:
        return None
    children = subreddit_info.get("data").get("children")
    for child in children:
        title = (child.get("data").get("title"))
        title = title.split(' ')
        for word in title:
            word = word.lower()
            if word in word_list:
                count[word] += 1;
    after = subreddit_info.get("data").get("after")
    if after is None:
        result = []
        for k in count.keys():
            if result == []:
                result.append("{}: {}".format(k, count[k]))
            else:
                for i in range(len(result)):
                    if count[k] > int(result[i].split(' ')[1]):
                        result = result[:i] + \
                                 ["{}: {}".format(k, count[k])] + \
                                 result[i:]
                        break;
                    else:
                        continue
                else:
                    result.append("{}: {}".format(k, count[k]))
        for printing in result:
            if int(printing.split(' ')[1]) != 0:
                print(printing)
        return
    return (count_words(subreddit, word_list, after, count))
