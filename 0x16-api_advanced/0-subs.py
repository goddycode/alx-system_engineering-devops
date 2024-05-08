"
    Return the total number of subscribers on a given subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise exception for non-200 status codes
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return 0
