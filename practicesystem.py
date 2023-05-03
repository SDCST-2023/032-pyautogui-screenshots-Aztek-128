import pyautogui as p
import time
time.sleep(3)
p.scroll(-220)

cursor = p.locateCenterOnScreen('assets/cursor.png')

if cursor != None:
    time.sleep(3)
    xcoords = cursor[0]
    ycoords = cursor[1]
    dy = 70

    while True:
        p.click(xcoords,ycoords-250,1)
        ycoords = ycoords+dy

time.sleep(3)


p.scroll(300)