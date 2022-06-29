import pyautogui as pag
import time

time.sleep(3)

#resolution of the screen
print(pag.size())
#current position of the mouse
print(pag.position())

#move the mouse over time(3rd argument->no of seconds it takes to do it)
pag.moveTo(100,100,3)

#move the mouse relative to its current position
pag.moveRel(100,100,3)

#click (xcor,ycor,no.of clicks,duration)
pag.click(-1189,756,3,3)
pag.write("10")
