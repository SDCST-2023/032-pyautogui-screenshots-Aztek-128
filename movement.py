import pyautogui as p
import time
time.sleep(2)

dy = 5
y0 = 200
x0 = 900
while True:
    p.click(x0,y0)
    y0 = y0+dy