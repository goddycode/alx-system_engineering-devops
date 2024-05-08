import requests


def get_number_of_subscribers(subreddit_name):
  """
  Fetches the number of subscribers for a given subreddit using Reddit's API.

  Args:
      subreddit_name: The name of the subreddit (string).

  Returns:
      The number of subscribers (integer) or 0 if an error occurs.
  """

  url = f'https://www.reddit.com/r/{subreddit_name}/about.json'
 
  headers = {'User-Agent': 'your_app_name v1.0.0 (by /u/your_username)'}

  try:
    response = requests.get(url, headers=headers, allow_redirects=False)
    response.raise_for_status()

    return data.get("data", {}).get("subscribers", 0)

  except requests.exceptions.RequestException as e:
  
    print(f"Error fetching subscriber count: {e}")
    return 0
