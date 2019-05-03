import feedparser
import sys
import requests
from clint.textui import progress

url = 'http://feed.theskepticsguide.org/feed'
processed_file='processed_files.txt'

processed_list = {}

processed_data=open(processed_file, "a+")

feed = feedparser.parse(url)

#for post in feed.entries:

# For testing, let's only grab the first 3 to save their bandwidth.  
# Otherwise, use the for statement above
for i in range(3):

    #Make sure we have the latest list to avoid duplicates
    processed_data=open(processed_file, "r")
    if(processed_data is not None):
        processed_list = set(map(str.strip, processed_data))
    processed_data.close()

    post = feed.entries[i]
    url = post.links[0].href
    file_name = url.split('/')[-1]
    if(file_name in processed_list):
        continue

    f = open(file_name, 'wb')

    r = requests.get(url, stream=True)

    with open(file_name, "wb") as file:
        total_length = int(r.headers.get('content-length'))
        for ch in progress.bar(r.iter_content(chunk_size = 2391975), expected_size=(total_length/1024) + 1):
            if ch:
                file.write(ch)
    
    processed_data=open(processed_file, "a+")
    processed_data.write(file_name)
    processed_data.write('\n')
    processed_data.close()
