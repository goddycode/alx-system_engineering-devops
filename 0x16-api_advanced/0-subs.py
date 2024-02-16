#!/usr/bin/python3
"""
Module: 0-subs

Contains the number_of_subscribers function
"""

import requests

def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.
    """
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    url = f"http://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': '0x16-api_advanced:project:v1.0.0 (by /u/firdaus_cartoon_jr)'}
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for 4XX and 5XX status codes
        data = response.json()
        subs = data.get("data", {}).get("subscribers", 0)
        return subs
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
        return 0
