import pyautogui
import time
from ecapture import ecapture as ec
i = int(input("Enter number of times you want to send the message"))
msg = "I Love you"
a=0

while a < i:
    time.sleep(3)
    pyautogui.typewrite(msg)
    pyautogui.press('enter')
    a+=1
    print(a)