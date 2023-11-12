#!/usr/bin/python3
# get subs
from requests import get
from sys import argv

def number_of_subscribers(subreddit):
    """ get number of subscribers """
    head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    count = get('https://www.reddit.com/r/{}/about.json'.format(
        subreddit),headers=head).json()
    try:
        return count['data']['subscribers']
    except:
        return 0

if __name__ == "__main__":
    number_of_subscribers(argv[1])
