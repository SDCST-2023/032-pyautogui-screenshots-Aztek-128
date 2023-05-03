import pyautogui as p
import time
time.sleep(3)
p.scroll(-220)

cursor = p.locateCenterOnScreen('assets/cursor.png')

if cursor != None:
    time.sleep(3)
    xcoords = cursor[0]
    ycoords = cursor[1]
    print(cursor)
    p.moveTo(cursor[0],cursor[1]-60)
    L = 0
    while L<10:
        p.moveTo(cursor[0], cursor[1]+600,4)
        for i in range(10):
            p.click(cursor[0],cursor[1],0.5)
            ycoords = cursor[1]+60
        
        


time.sleep(3)


p.scroll(300)