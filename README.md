# Python RSS Feed File Downloader

As of May 3, 2019, this seems to be the simplest way to pull files from a feed without getting duplicate files.  It's obviously not going to be the most optimal because of all the file I/O.  If I were really going to run this on a regular basis, I suppose we could store the filenames in a lightweight database, but this was mostly just scratching an itch for me and I only need to run it once on a couple of feeds with a long history.  The SGU (the URL I used in the committed code) has been around since 2005, so they have well over 700 episodes.

If something is borked, or has been deprecated, let me know and I may code.

## Purpose

Downloads all files from an RSS feed.  Also includes a progress bar for each file

## Notes

For testing purposes, this only grabs the first three items to save on the feed's bandwidth (the costs add up FAST).  If you have a feed where you want to grab all items, replace the for-range loop with the commented-out line `for post in feed.entries:`

This will store the processed filenames in a text file to prevent duplicate downloads.  If the file does not already exist, it will create it.