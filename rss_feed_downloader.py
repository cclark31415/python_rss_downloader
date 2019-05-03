import feedparser
import sys
import requests
from clint.textui import progress

url = 'http://feed.theskepticsguide.org/feed'

feed = feedparser.parse(url)

#for post in feed.entries:

# For testing, let's only grab the first 3 to save their bandwidth.  
# Otherwise, use the for statement above
for i in range(3):
    post = feed.entries[i]
    url = post.links[0].href
    file_name = url.split('/')[-1]
    f = open(file_name, 'wb')

    r = requests.get(url, stream=True)

    with open(file_name, "wb") as file:
        total_length = int(r.headers.get('content-length'))
        for ch in progress.bar(r.iter_content(chunk_size = 2391975), expected_size=(total_length/1024) + 1):
            if ch:
                file.write(ch)
