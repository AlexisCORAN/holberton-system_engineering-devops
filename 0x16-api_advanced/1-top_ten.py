#!/usr/bin/python3
"""
This module contains the top_ten function
"""
import requests


def top_ten(subreddit):
    limit = "10"

    url = "https://www.reddit.com/r/{}/hot.json?limit={}".format(subreddit,
                                                                 limit)

    user_agent = {"User-Agent": "Python"}

    response = requests.get(url, headers=user_agent, allow_redirects=False)

    if response.status_code >= 300:
        return None
    else:
        for elem in response.json().get("data").get("children"):
            print(elem.get("data").get("title"))
