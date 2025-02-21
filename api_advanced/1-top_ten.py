#!/usr/bin/python3
"""Script that fetches 10 hot posts for a given subreddit."""
import requests


def top_ten(subreddit):
    """
    Print the titles of the top 10 hot posts for a given subreddit.

    If the subreddit is invalid or has no posts, print None.
    """
    headers = {'User-Agent': 'MyRedditBot/1.0 (by /u/yourusername)'}
    subreddit_url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {'limit': 10}  # Ensure we only get 10 posts
    response = requests.get(subreddit_url, headers=headers, params=params, allow_redirects=False)

    if response.status_code == 200:
        json_data = response.json()
        posts = json_data.get('data', {}).get('children', [])

        if not posts:
            print(None)
            return

        for post in posts:
            print(post.get('data', {}).get('title', ''))
    else:
        print(None)
