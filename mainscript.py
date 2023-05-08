import pyautogui as p
import time

#debug
numclicks = 100
p.PAUSE = 0.1


def clicks():
    #x = p.locateCenterOnScreen('assets/cookie.png')
    #print(x)
    if cookie != None:
        p.moveTo(cookie)
        y = 0
        while y < numclicks:
            p.click(cookie)
            y = y+1

    




def upgrade():
    store = p.locateCenterOnScreen('assets/info.png',confidence = 0.7)
    x = store[0]
    y = store[1]
    p.moveTo(x+80,y+50)
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


def gold():
    start = time.time()
    future = start + 10

    current = time.time()
    if current  < future:
        while True:
            golden = p.locateCenterOnScreen('assets/goldencookie.png',confidence = 0.5)
            print(golden)
            if golden!= None:
                p.click(golden)
                break


            while True:
                golden = p.locateCenterOnScreen('assets/goldencookie3.png',confidence = 0.5)
                print(golden)
                if golden!= None:
                    p.click(golden)
                    break

                while True:
                    golden = p.locateCenterOnScreen('assets/goldencookie2.png',confidence = 0.5)
                    print(golden)
                    if golden!= None:
                        p.click(golden)
                        break

                    while True:
                        golden = p.locateCenterOnScreen('assets/goldencookie4.png',confidence = 0.5)
                        print(golden)
                        if golden!= None:
                            p.click(golden)
                            break
                            
                        while True:
                            golden = p.locateCenterOnScreen('assets/goldencookie5.png',confidence = 0.5)
                            print(golden)
                            if golden!= None:
                                p.click(golden)
                                break

  



def main():
    p.confirm("run?")
    p.hotkey('ctrl','win','right')
    p.sleep(0.5)
    global cookie
    cookie = p.locateCenterOnScreen('assets/cookie.png', confidence = 0.5)

    while True:
        clicks() 
        upgrade()  
        purchase() 
        gold()

main()