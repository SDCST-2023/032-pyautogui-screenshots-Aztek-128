import pyautogui as p
import time

#debug
numclicks = 100
p.PAUSE = 0.1


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
    store = p.locateCenterOnScreen('assets/store.png',confidence = 0.7)
    x = store[0]
    y = store[1]
    p.moveTo(x-130,y+50)
    p.click()

def purchase():
    p.moveTo(1303,458)
    p.scroll(-200)


    cursor = p.locateCenterOnScreen('assets/cursor.png')

    if cursor != None:
        time.sleep(1)
        xcoords = cursor[0]
        ycoords = cursor[1]
        dy = 70

        while True:
            p.click(xcoords,ycoords-100,2)
            ycoords = ycoords+dy
            if ycoords >970:
                break

    time.sleep(1)
    p.scroll(300)        


'''def gold():
    while True:
        golden = p.locateCenterOnScreen('assets/goldencookie.png')
        if golden !=None:
            p.click(golden)'''




def main():
    p.confirm("run?")
    p.hotkey('ctrl','win','right')
    while True:
        clicks() 
        upgrade()  
        purchase() 
        #gold()

main()