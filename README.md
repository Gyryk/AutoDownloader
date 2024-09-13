# AutoDownloader
Download shows automatically automatically to enjoy over the weekend

To set up, first enable developer mode on Safari and allow remote automation in developer settings. <br>
Then, enable remote access in Transmission <br>

Then run these commands (replacing paths with your own):

`chmod +x /Users/gyryk/Documents/Projects/AutoDownloader/main.py` Which makes the script executable, then `crontab -e` which opens vim. Insert the following code there: <br>

```0 0 * * * /usr/bin/python3 /Users/gyryk/Documents/Projects/AutoDownloader/main.py >> /Users/gyryk/Documents/Projects/AutoDownloader/auto_downloader.log 2>&1``` <br>
This makes it run every midnight


```12 0 * * 5 /usr/bin/python3 /Users/gyryk/Documents/Projects/AutoDownloader/main.py >> /Users/gyryk/Documents/Projects/AutoDownloader/auto_downloader.log 2>&1``` <br>
This makes it run every friday noon
