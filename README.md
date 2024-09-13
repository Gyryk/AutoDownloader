# AutoDownloader
Download shows automatically automatically to enjoy over the weekend

To set up, first enable developer mode on Safari and allow remote automation in developer settings. <br>
Then, enable remote access in Transmission <br>

Then run these commands (replacing paths with your own):

`chmod +x /Users/gyryk/Documents/Projects/AutoDownloader/main.py` which makes the script executable and `chmod +r /Users/gyryk/Documents/Projects/AutoDownloader/main.py` which makes it readable. <br>
Then run `crontab -e` which opens the processes scheduled in vim. Add your choice of scheduling code there: <br>

```0 0 * * * /usr/bin/python3 /Users/gyryk/Documents/Projects/AutoDownloader/main.py >> /Users/gyryk/Documents/Projects/AutoDownloader/auto_downloader.log 2>&1``` <br>
This makes it run every midnight


```12 0 * * 5 /usr/bin/python3 /Users/gyryk/Documents/Projects/AutoDownloader/main.py >> /Users/gyryk/Documents/Projects/AutoDownloader/auto_downloader.log 2>&1``` <br>
This makes it run every friday noon
