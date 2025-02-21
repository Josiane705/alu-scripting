#!/usr/bin/python3
"""
Module to fetch and display the top ten hot posts from a given subreddit using the Reddit API.

This module contains a function `top_ten` that retrieves and prints the titles
of the first 10 hot posts for a given subreddit using Reddit's public API.

Usage:
    Run the script with a subreddit name as an argument:
    $ python3 script.py subreddit_name

If the subreddit is invalid or not found, the function will print `None`.
"""

import requests
import sys

def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    for a given subreddit.
    
    Args:
        subreddit (str): The name of the subreddit to query.
    
    Returns:
        None
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'limit': 10}
    
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    
    if response.status_code == 200:
        data = response.json()
        posts = data.get("data", {}).get("children", [])
        if posts:
            for post in posts:
                print(post["data"].get("title"))
        else:
            print(None)
    else:
        print(None)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
