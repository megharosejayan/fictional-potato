
import pyautogui as pag
import time

time.sleep(1)
distance = 300
while distance > 0:
    pag.dragRel(distance,0,1,button='left')
    distance = distance - 20
    pag.dragRel(0,distance,1,button='left')
    pag.dragRel(-distance,0,1,button='left')
    distance = distance - 20
    pag.dragRel(0,-distance,1,button='left')
    #for failsafe purposes
    time.sleep(3)

