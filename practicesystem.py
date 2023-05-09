import pyautogui as p
import time
time.sleep(0.5)

start = time.time()
future = start + 1
current = time.time()


while current < future:
    current = time.time()
    print(current - start)
    while True:
        golden = p.locateCenterOnScreen('assets/goldencookie.png',confidence = 0.5)
        print(golden)
        if golden!= None:
            p.click(golden)
        
        while True:
            golden = p.locateCenterOnScreen('assets/goldencookie3.png',confidence = 0.5)
            print(golden)
            if golden!= None:
                p.click(golden)

            while True:
                golden = p.locateCenterOnScreen('assets/goldencookie2.png',confidence = 0.5)
                print(golden)
                if golden!= None:
                    p.click(golden)


                while True:
                    golden = p.locateCenterOnScreen('assets/goldencookie4.png',confidence = 0.5)
                    print(golden)
                    if golden!= None:
                        p.click(golden)
                        
                    while True:
                        golden = p.locateCenterOnScreen('assets/goldencookie5.png',confidence = 0.5)
                        print(golden)
                        if golden!= None:
                            p.click(golden)
                        else:
                            break
