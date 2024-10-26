import pyautogui as pg
import time

imageOffset = 25

def checkImage():
  try:
    pos = pg.locateOnScreen("./image2.png", confidence=0.8)
    pg.moveTo(pos[0]+imageOffset,pos[1]+imageOffset,1)
    pg.click()
    time.sleep(1)
  except:
    print("imageas loaded but couldn't find it in Dofus")

checkImage()