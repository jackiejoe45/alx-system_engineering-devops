#!/usr/bin/python3
"""
This module contains the function top_ten.
"""

import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'python:subreddit.top.ten:v1.0 (by /u/yourusername)'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        # Check if the response is successful and has content
        if response.status_code == 200 and response.headers.get('content-type') == 'application/json':
            try:
                data = response.json()
                posts = data['data']['children']
                for post in posts:
                    print(post['data']['title'])
            except (ValueError, KeyError):
                print("None")
        else:
            print("None")
    except requests.RequestException:
        print("None")
