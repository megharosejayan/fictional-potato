import pyautogui as pag
import time

time.sleep(3)

#mouse functions

#resolution of the screen
print(pag.size())
#current position of the mouse
print(pag.position())

#move the mouse over time(3rd argument->no of seconds it takes to do it)
pag.moveTo(100,100,3)

#move the mouse relative to its current position (xcor,ycor,duration-sec)
pag.moveRel(100,100,3)

#click (xcor,ycor,no.of clicks,interval between clicks, button)
pag.click(688,369,1,1,button='left')

pag.write("Hi")

pag.rightClick(x=688, y=369)
#pag.middleClick(x=moveToX, y=moveToY)
#pag.doubleClick(x=moveToX, y=moveToY)
#pag.tripleClick(x=moveToX, y=moveToY)

#scrolls up
pag.scroll(500)
#scrolls down
pag.scroll(-500)

#mouse up and down
#left click and hold at 500,400
pag.mouseDown(500,400,button='left')
#drags to 900,400
pag.moveTo(900,400)
#releases the left click
pag.mouseUp()



