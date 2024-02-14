#!/usr/bin/python3
"""
Method which queries the Reddit API
and returns the number of subscribers
"""


import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns
    the number of subscribers for a given subreddit.
    :param subreddit: The name of the subreddit.
    :return: The number of subscribers (int).
    Returns 0 if the subreddit is invalid or
    an error occurs.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Custom User-Agent'}  # Provide a custom User-Agent to avoid errors
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0
