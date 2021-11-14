import pyautogui
import time
import threading
import random

# set global variable flag
flag = 1
screenWidth, screenHeight = pyautogui.size()

def normal():
    global flag
    while flag==1:
        a = random.randrange(100, screenWidth, 1)
        b = random.randrange(100, screenHeight, 1)
        pyautogui.moveTo(a, b, 2)
        time.sleep(10)
        if flag==False:
            print('The while loop is now closing')

def get_input():
    global flag
    keystrk=input('Press a key \n')
    # thread doesn't continue until key is pressed
    print('You pressed: ', keystrk)
    flag=False
    print('flag is now:', flag)

n=threading.Thread(target=normal)
i=threading.Thread(target=get_input)
n.start()
i.start()
