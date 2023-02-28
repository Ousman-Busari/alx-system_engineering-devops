#!/usr/bin/python3
import requests

url = "https://www.reddit.com/r/{}/hot.json".format("not_valid")
headers = {
    "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/Ousman_Busari)"
}
params = {
    "limit": 100,
    # "after": after,
    # "count": count
}
res = requests.get(url, headers=headers, params=params,
                    allow_redirects=False)

print(res.status_code)