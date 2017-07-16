import requests, json, codecs

from setting import settings
import appTokenManager as App
import myNewsFeed

nextUrl = myNewsFeed.getFeed( App.Setting.Token )['previous']
print(nextUrl)
n = 0

"""
while True:
    n += 1
    print(n,"  |  ", nextUrl)
    nextUrl = myNewsFeed.getFeed(App.Setting.Token)['previous'].split("&")[3].replace("until=","")
"""