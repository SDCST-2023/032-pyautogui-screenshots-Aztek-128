import pyautogui as p
import time

#debug
numclicks = 10



def clicks():
    x = p.locateCenterOnScreen('assets/cookie.png')
    print(x)
    if x != None:
        p.moveTo(x)
        y = 0
        while y < numclicks:
            p.click(x)
            y = y+1


def upgrade():
    store = p.locateCenterOnScreen('assets/store.png')
    x = store[0]
    y = store[1]
    p.moveTo(x-130,y+50)
    p.click()


def main():
    p.confirm("run?")
    p.hotkey('ctrl','win','right')
    while True:
        clicks() 
        upgrade()   

main()