#!/usr/bin/python3
"""
Method which queries the Reddit API
and returns the number of subscribers
"""
import requests

def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.
    :param subreddit: The name of the subreddit as a string.
    :return: The number of subscribers (int). Returns 0 if subreddit is invalid or an error occurs.
    """
    if not isinstance(subreddit, str):
        return 0
    
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'safari:holberton/0.1.0'}
    
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        return 0
    
    try:
        data = response.json()
        return data['data']['subscribers']
    except (KeyError, ValueError):
        return 0

