#!/usr/bin/python3
"""
1-top_ten
"""
import requests


def top_ten(subreddit):
    """
    Queries reddit API and prints the 10 hot posts listed in subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/Ousman_Busari)"
    }

    params = {
        "limit": 10
    }
    res = requests.get(url, headers=headers,
                       params=params, allow_redirects=False)
    if res.status_code == 404:
        print(None)
        return 0
    ret = res.json().get("data").get("children")
    [print(c.get("data").get("title")) for c in ret]
