import pyautogui as p
import time


time.sleep(3)


x = p.locateCenterOnScreen('assets/cookie.png')

if x != None:
    p.moveTo(x)
    while True:
        p.leftClick(x)




