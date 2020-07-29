import pyautogui
import time
import keyboard
import datetime
import os


#checks that path is valid
path = os.getcwd()
os.path.isdir(path)
print ("The current working directory is %s" % path)


#Checks if "Images" directory exists
os.path.isdir('\Images')

# Changes to current working directory to "Images"
cwdPath = path +'\Images'
os.chdir(cwdPath)

print ("The current working directory is %s" %os.getcwd())
time.sleep(4)

newFolder = path + "\year"

# define the access rights
access_rights = 0o755

try:
    os.mkdir(newFolder, access_rights)
except OSError:
    print ("Creation of the directory %s failed" % newFolder)
else:
    print ("Successfully created the directory %s" % newFolder)

time.sleep(3)

try:
    while True:
        time.sleep(2)
        uniq_filename = str(datetime.datetime.now().date()) + '_' + str(datetime.datetime.now().time()).replace(':', '.')
        pyautogui.screenshot(r'Images\\Game Pictures\\' + uniq_filename + '.png')
        print('Screenshot captured,' + ' "' + uniq_filename + '.png"' + ' is now in your library!')
except KeyboardInterrupt:
    print("Hard Exit Initiated. Goodbye!")

# To do:
    # Screenshot loops                                        [X]
    # Places photos in correct subdirectory                   [X]
    # Creates Tempfiles (Might not even be needed)            [ ]
    # Creates New Folder based on date/session                [ ]
    # Organizes the photos in chronological order             [X]
    # Takes picture when keys are pressed                     [ ]
    # Create a function that can be called by Main.py         [ ]

#Reminders
    # https://stackabuse.com/creating-and-deleting-directories-with-python/ for creating/manipulating a directory