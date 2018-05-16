import pyautogui as pg
import webbrowser
import time
#make sure you log into Amazon first
webbrowser.open("https://www.amazon.com/")
time.sleep(10)
pg.hotkey('tab')
pg.hotkey('tab')
pg.hotkey('tab')
pg.hotkey('tab')
pg.hotkey('tab')

time.sleep(1)
pg.typewrite("pencils", 0.1)

pg.hotkey('enter')

time.sleep(1)

i=0
while i < 32:
    pg.hotkey('tab')
    time.sleep(.3)
    i += 1

pg.hotkey('enter')

time.sleep(1)

i=0
while i < 37:
    pg.hotkey('tab')
    time.sleep(.3)
    i += 1

time.sleep(1)

pg.hotkey('enter')

time.sleep(1)

