import pyautogui
import keyboard
import mouse
import mouseinfo
import time
import decimal
import random
import logging

import datetime
#import PyDirectInput



x = pyautogui.prompt('Enter Password')
print(x)

#pyautogui.press(, )
# Halts application until 'enter' is pressed.
#keyboard.wait('enter')

#time.sleep(2)
# use the press function instead of 'write': --> pyautogui.press()

#Random Number Generator
rngUUU   = random.uniform(0,.001)
rngUU    = random.uniform(0,0.1)
rngMicro = random.uniform(0,1)
rngTiny  = random.uniform(0,10)
rngSmall = random.uniform(0,100)
rngLarge = random.uniform(0,100000)
rngHuge  = random.uniform(0,1000000)
rngMacro = random.uniform(0,10000000)

# random decimal
x = decimal.Decimal(str(random.uniform(100, 1000)))
print(x)

#Chooses a CryptoSafe random float using the rng (above) as the start/stop values.
randomfloat = random.SystemRandom().uniform(rngUUU,rngMacro)
print(randomfloat)


#Finds image on screen that matches image:
x = pyautogui.locateOnScreen(r'Images\\litfoo.png')
print(x)


#pyautogui.scroll(rng)





#To Do:
    # Create GUI Dashboard          [ ]
    # Create RNG                    [ ]
    #                               [ ]
    #                               [ ]
    #                               [ ]
    #                               [ ]
    #                               [ ]
    # Create chat bot to talk       [ ]
    # Create Logging Module         [ ]

# Reminders
    #Don't use pyautogui for key and mouse inputs
