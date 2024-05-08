import requests

def number_of_subscribers(subreddit):
  """
  Returns the number of subscribers for a given subreddit using Reddit's API.

  Args:
      subreddit: The name of the subreddit (string).

  Returns:
      The number of subscribers (integer) or 0 if the subreddit is invalid.
  """

  if subreddit is None or type(subreddit) is not str:
    return 0

  # Construct the URL without following redirects (important for invalid subreddits)
  url = f'https://www.reddit.com/r/{subreddit}/about.json'

  # Set a custom User-Agent header for identification and potential rate limit handling
  headers = {'User-Agent': 'your_app_name v1.0.0 (by /u/your_username)'}

  try:
    response = requests.get(url, headers=headers, allow_redirects=False)
    response.raise_for_status()  # Raise an exception for non-200 status codes

    data = response.json()
    return data.get("data", {}).get("subscribers", 0)

  except requests.exceptions.RequestException as e:
    # Handle potential exceptions like network errors, timeouts, etc.
    print(f"Error fetching subscriber count: {e}")
    return 0
