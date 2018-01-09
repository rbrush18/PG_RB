import pyautogui as pg
import time

pg.hotkey('ctrl','winleft','d')
pg.hotkey('winleft')
pg.typewrite('chrome\n',0.5)
pg.hotkey('winleft','up')

pg.typewrite('amazon.com\n',0.5)
time.sleep(4)

pg.hotkey('tab')
time.sleep(.2)
pg.hotkey('tab')
time.sleep(.2)
pg.hotkey('tab')
time.sleep(.2)
pg.hotkey('tab')
time.sleep(.2)
pg.hotkey('tab')
time.sleep(.2)

pg.typewrite('boosted board\n')
time.sleep(.2)
pg.moveTo(1032, 590)
pg.click()
time.sleep(.2)
pg.moveTo(1205, 468)
pg.click()
time.sleep(.2)
pg.moveTo(936, 359)
pg.click()
