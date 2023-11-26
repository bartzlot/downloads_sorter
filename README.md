## Python Downloads Folder Sorter

* creates folders specified in .env file
* sorts them according to extensions assigned to folder in .env file
* you can determine the time of refreshing script (checking for new files in your downloads folder)

## How to make this script run on start-up on MacOS

# Firstly intall all requirements required for this script to run properly

```bash
pip install -r requirements.txt
```
* NOTE: You have to be in script folder
# Secondly you have to create a .plist file in ~/Library/LaunchAgents/ 

```bash 
echo '<?xml version="1.0" encoding="UTF-8"?>\n<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">\n<plist version="1.0">\n<dict>\n    <key>Label</key>\n    <string>com.user.yourscript</string>\n    <key>ProgramArguments</key>\n    <array>\n        <string>/usr/bin/python3</string>\n        <string>/path/to/your/script.py</string>\n    </array>\n    <key>RunAtLoad</key>\n    <true/>\n</dict>\n</plist>' > ~/Library/LaunchAgents/com.user.downloads_filter.plist 
```
* You have to repalce the '/path/to/your/script.py' and '/usr/bin/python3' (if you're not using default python version)
* Then accept any permissions popup's

## How set-up the script for yourself's preferences
# All preferences and settings are stored in .env file and you can change them to fulfill your needs

* **DOWNLOADS_PATH** - path to the folder you want to sort
* **REFRESH_TIME_SPAN** - time [in minutes] for another refresh to occur
* **FOLDER_NAMES** - folder names that you want to create/operate for sorting (they must be separated with ',' -> ! without spaces)
* **FILTER_EXTENSTIONS** - 

