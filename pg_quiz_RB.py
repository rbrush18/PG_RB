import pyautogui as pg
import time
import webbrowser

points=0

#Question goes here
answer = pg.prompt(
"""
Which would you rather be?


a) The star of your favorite sports team
b) The richest man/woman in the world
c) The most popular man/woman in the world


"""
    )

pg.alert("You chose " + answer)

# Answer and points
if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3

#Question goes here
answer = pg.prompt(
"""
Which would you rather do as your job?


a) Play your favorite sport
b) Sit around in a mansion doing whatever you want
c) Sing and record music for hundreds of millions to listen to


"""
    )

pg.alert("You chose " + answer)

# END OF SURVEY
pg.alert("OK, here's your character...")
#Tom Brady
if points < 4:
    pg.alert("You are Tom Brady!")
    webbrowser.open("http://images.performgroup.com/di/library/omnisport/1d/c6/tom-brady-4517-usnews-getty-ftr_slmkna5vndow1b5401mhj52v8.jpg?t=1044817107&w=960&quality=70")

#Bill Gates
elif points >=3  and points <= 5
    pg.alert("You are Bill Gates!")
    webbrowser.open("https://cdn.vox-cdn.com/thumbor/JUcnTuekWuN7Nx4L-f56i0tex1A=/0x0:5622x3722/1200x800/filters:focal(3498x1001:4396x1899)/cdn.vox-cdn.com/uploads/chorus_image/image/57340875/850286096.0.jpg")
    
#Taylor Swift
elif points >= 5:
    pg.alert("You are Taylor Swift!")
    webbrowser.open("http://elbroide.com/wp-content/uploads/2017/10/Taylor-Swift-1200x800.png")
