# python_rss_downloader
Downloads all files from an RSS feed.  Also includes a progress bar

For testing purposes, this only grabs the first three items to save on the feed's bandwidth (the costs add up FAST).  If you have a feed where you want to grab all items, replace the for-range loop with the commented-out line `for post in feed.entries:`

