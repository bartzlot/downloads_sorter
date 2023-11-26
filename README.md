# Python Downloads Folder Sorter

* creates folders specified in .env file
* sorts them according to extensions assigned to folder in .env file
* you can determine the time of refreshing script (checking for new files in your downloads folder)

## How to make this script run on start-up on MacOS

### STEP 1: intall all requirements required for this script to run properly

```bash
pip install -r requirements.txt
```
* NOTE: You have to be in script folder

### STEP 2: you have to create a .plist file in ~/Library/LaunchAgents/ 

```bash 
echo '<?xml version="1.0" encoding="UTF-8"?>\n<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">\n<plist version="1.0">\n<dict>\n    <key>Label</key>\n    <string>com.user.yourscript</string>\n    <key>ProgramArguments</key>\n    <array>\n        <string>/usr/bin/python3</string>\n        <string>/path/to/your/script.py</string>\n    </array>\n    <key>RunAtLoad</key>\n    <true/>\n</dict>\n</plist>' > ~/Library/LaunchAgents/com.user.downloads_filter.plist 
```
* You have to repalce the ```/path/to/your/script.py``` and ```/usr/bin/python3``` (if you're not using default python version)

* Then accept any permissions popup's

### How set-up the script for yourself's preferences

#### All preferences and settings are stored in ```.env``` file and you can change them to fulfill your needs

* **DOWNLOADS_PATH** - path to the folder you want to sort

* **REFRESH_TIME_SPAN** - time [in minutes] for another refresh to occur

* **FOLDER_NAMES** - folder names that you want to create/operate for sorting (they must be separated with ```,``` -> ! without spaces)

* **FILTER_EXTENSTIONS** - filters must be separated by ```/``` and contain no spaces and folders filters separator is ```|```

  * NOTE: .env file has to contain same amount of folder names and filters extensions separated by ```|``` to work properly
  * Folder containing rest not sorted extensions should be placed on the end of the ```FOLDER_NAMES``` list
  * Extension for rest folder should be set as ```ALL_OTHER```
  * Proper example of ```.env``` file you can see in repository

## How to make this script run on start-up on Windows

### STEP 1: intall all requirements required for this script to run properly

```bat
pip install -r requirements.txt
```
* NOTE: You have to be in script folder

### STEP 2: you have to create a .bat file
```bat
@echo off
C:\path\to\your\script.py
pause
```
 * replace ```path\to\your\script.py``` with actual path to this script on your system

### STEP 3: find the Path to Your Startup Folder

* for the current user's Startup folder, the path is usually C:\Users\YourUsername\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup.
* replace YourUsername with your actual Windows username
### STEP 4: run in cmd command down below to copy ```.bat``` file to use this script on start-up 
```bat
copy C:\path\to\run_script.bat "C:\Users\[YourUsername]\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
```
* ```C:\path\to\run_script.bat``` change this to actual script path
* ```[YourUsername]``` change this to your username
