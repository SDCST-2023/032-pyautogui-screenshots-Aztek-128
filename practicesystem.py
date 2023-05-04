import pyautogui as p
import time
time.sleep(3)


while True:
    golden = p.locateCenterOnScreen('assets/goldencookie.png')
    print(golden)
    