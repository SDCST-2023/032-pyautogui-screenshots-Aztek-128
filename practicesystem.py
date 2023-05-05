import pyautogui as p
import time
time.sleep(3)



while True:
    golden = p.locateCenterOnScreen('assets/goldencookie.png',confidence = 0.5)
    print(golden)
    if golden!= None:
        p.click(golden)

    while True:
        golden = p.locateCenterOnScreen('assets/golden2cookie.png',confidence = 0.5)
        print(golden)
        if golden!= None:
            p.click(golden)