#!/usr/bin/python3
"""
2-recurse
"""
import requests


def recurse(subreddit, after="", count=0, hot_list=[]):
    """
    A reursice fucntion tha queries the Reddit API and returns a list
    containing the titles of all hot articles for a given subreddit
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/Ousman_Busari)"
    }
    params = {
        "limit": 100,
        "after": after,
        "count": count
    }
    res = requests.get(url, headers=headers,
                       params=params, allow_redirects=False)

    if res.status_code == 404:
        return None

    res = res.json().get("data")
    after = res.get("after")
    count += res.get("dist")
    for c in res.get("children"):
        hot_list.append(c.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, after, count, hot_list)
    return hot_list
