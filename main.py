import pyautogui
import time
import random
print("Screen Width: ", pyautogui.size()[0])
print("Screen Height: ", pyautogui.size()[1])
pyautogui.moveTo(pyautogui.size()[0]/2, pyautogui.size()[1]/2, duration = 0.5) #move the cursor to center of screen
while True:
    totalClick = 2
    directionX = 1 if random.randint(0,1) else -1
    xRel = (50*directionX)
    moveTime = random.uniform(0.2,1)
    returnTime = random.uniform(0.2,2)
    pyautogui.moveRel(xRel,50,duration = moveTime)
    pyautogui.click()
    pyautogui.moveRel(xRel*-1,-50,duration = returnTime)
    pyautogui.click()
    if random.randint(0,1):
        time.sleep(0.2)
        pyautogui.click
        totalClick += 1
    idle = random.randrange(3,5)
    print("x:", xRel, "  y:", 50, "  idle:", idle, "sec", "  totalClick:", totalClick, "  moveTime:", moveTime, "  returnTime:", returnTime)
    time.sleep(idle)