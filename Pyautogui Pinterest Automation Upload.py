# This algorithm will take control of your mouse and keyboard
# It mimics mouse clicks and hotkeys
# Download Pyautogui by visiting the webpage below
# https://pypi.org/project/PyAutoGUI/
import pyautogui as py

##### NOTE #####
### TO CANCEL THIS AUTOMATION PRESS CTRL + C #####
### OR MOVE YOUR MOUSE TO THE TOP LEFT ASAP ######

# FINALLY - Make sure your content(Pin that is to be uploaded to Pinterest)
# Make sure the content is named 1, 2, 3, 4, 5, etc
# Check  out my File Name Change script attached to this repository on Github

# 1. Bring up Pinterest homepage and manually click on Pinterest Uploads
# 2. Mannually upload your first file onto Pinterest so the file shows up
# again when this for loop processes.
# 3. Bring up Google Sheets and prefill the sheets with the name you want
# the Pin to be labeled as.
### If Pin 1 is to be called Hello. Make sure you have Hello. in the first Google Sheet

# Make sure page zoom is 100% not 80% or other

## Make sure Google Excel has proper cell highlighted
# and make sure the character length of the cell is not beyond 100 characters

# Clicking to make sure python script is out of the way
py.click(106, 534, duration=0.55)
py.time.sleep(1)

# The loop will begin at 1 and count up by 1 to 10854
# If you want the loop to count by two paste this
# below: range(1, 10854, 2)
for a in range(1, 10854, 1):
        if a == 10854:
                break

        # Clicking on Google Sheet
        py.keyDown('ctrl')
        py.press('tab')
        py.keyUp('ctrl')
        py.time.sleep(0.75)

        # Press Down so have excel start one above the cell I want to use
        py.press('down')
        py.keyDown('ctrl')
        py.press('c')
        py.keyUp('ctrl')
        py.time.sleep(0.25)

        # Back to Pinterest
        py.keyDown('ctrl')
        py.press('tab')
        py.keyUp('ctrl')
        py.time.sleep(0.5)

        # Clicking on Upload
        py.click(431, 420, duration=0.55)
        py.time.sleep(5.75)
        py.typewrite('abc')
        py.time.sleep(0.25)
        py.typewrite(' ')
        py.time.sleep(0.25)
        py.typewrite('(')
        py.time.sleep(0.25)
        py.typewrite(str(a), interval=0.25)# CHANGE TO 0
        py.time.sleep(0.25)
        py.typewrite(')')
        py.time.sleep(0.25)
        if a % 50 == 0:

# The modulo operator - % is explained by this stackoverflow webpage below
# https://stackoverflow.com/questions/8002217/how-do-you-check-whether-a-number-is-divisible-by-another-number-python
# The above means if the number A types is a multiple or divisible by 50

                ############################################################
                #FINISHING TOUCHES
                ############################################################

                # Get ride of the popup after typing in 150 or something
                py.time.sleep(0.5)
                py.hotkey('tab')
                py.time.sleep(0.5)
                py.hotkey('tab')
                py.time.sleep(0.5)
                py.hotkey('tab')
                py.time.sleep(0.5)
                py.hotkey('enter')

                # Delete Extra Pin to Upload
                py.time.sleep(0.5)
                # Clicking random spot just above the three dots
                # So can delete the extra Pin
                py.click(542, 202, duration=0.5)
                py.time.sleep(0.5)
                py.hotkey('tab')
                py.time.sleep(0.5)
                py.hotkey('enter')
                py.time.sleep(0.5)
                py.hotkey('tab')
                py.time.sleep(0.5)
                py.hotkey('enter')
                py.time.sleep(1)

                # Click on Circle to Select Pin to Post
                py.click(1140, 190, duration=0.55)
                py.time.sleep(0.5)

                #Click on Select All
                py.click(204, 100, duration=0.55)
                py.time.sleep(0.5)

                #### You can edit all descriptions, titles, links, etc
                # By clicking on the little Pen icon
                # After you select all

                # Click on Edit Button after Select All
                py.hotkey('tab')
                py.time.sleep(0.5)
                py.hotkey('enter')
                py.time.sleep(0.5)

                # Selecting the Board to Assign all Pins to
                py.click(645, 227, duration=0.55)
                py.time.sleep(2)

                # Select Title Quote Board
                py.click(577, 224, duration=0.55)
                py.time.sleep(1)
                py.typewrite('Quotes F', interval=0.05)
                py.time.sleep(0.5)
                py.hotkey('tab')
                py.time.sleep(0.5)
                py.hotkey('enter')
                py.time.sleep(0.5)
                

                # Clicking on Description for Pin
                py.click(672, 418, duration=0.55)
                py.time.sleep(0.5)
                py.hotkey(']')
                py.time.sleep(0.5)

                # Clicking on Link destination
                py.hotkey('tab')
                py.time.sleep(0.5)
                py.hotkey('.')
                py.time.sleep(0.5)

                # Click on Update Info
                py.click(865, 669, duration=0.55)
                py.time.sleep(8)

                # Click on Publish
                py.click(1202, 99, duration=0.55)

                # WAIT TIME 6 MIN
                py.time.sleep(360)

                # Click on the Plus Sign to Upload More Pins
                py.click(1261, 102, duration=0.55)
                py.time.sleep(1)

                # Click on Create Pin
                py.click(1084, 174, duration=0.55)
                py.time.sleep(5.5)

                # Should restart after this

        else:
                # The time sleep is for after typing in the proper number for A then Enter is for uploading the image to Pinterest
                py.time.sleep(0.5)
                py.hotkey('Enter')
                py.time.sleep(1)

                # Clicking on Title
                py.hotkey('tab')
                py.time.sleep(0.5)
                py.hotkey('tab')
                py.time.sleep(0.5)
                py.keyDown('ctrl')
                py.press('v')
                py.keyUp('ctrl')
                py.time.sleep(0.25)

                # Clicking on the plus at the top left to introduce
                # another pin to upload
                py.click(36, 177, duration=1)
                py.time.sleep(2)



