#!/usr/bin/python3
"""
100-count
"""
import requests


def count_words(subreddit, word_list, count=0, after="", hot_list=[]):
    """
    A recursive fucntion that queries the Reddit API, parses
    the title of all hot article, and prints a sorted count of
    given keywords(case insensitive and delimited by space)
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
    res = requests.get(url, headers=headers, params=params,
                       allow_redirects=False)

    if res.status_code != 200:
        return

    res = res.json().get("data")
    after = res.get("after")
    count += res.get("dist")

    for art in res.get("children"):
        hot_list += [x.lower() for x in art.get("data")
                     .get("title").split(" ")]
    if after is not None:
        count_words(subreddit, word_list, count, after, hot_list)
    else:
        search_count = {}
        for search in [x.lower() for x in word_list]:
            count = 0
            for word in hot_list:
                if search == word:
                    count += 1
            if search_count.get(search) is not None:
                search_count[search] += count
            else:
                search_count[search] = count

        search_count = sorted(search_count.items(),
                              key=lambda x: (-x[1], x[0]))
        [print("{}: {}".format(s[0], s[1])) for s in search_count if s[1] != 0]
        return
