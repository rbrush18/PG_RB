import pyautogui as pg
import webbrowser
import time

sport = pg.prompt(
    """
What is your favorite sport?

""")

if sport == "a":
    category = pg.prompt(
        """
What is your favorite player in that sport?

        """)

elif sport == "b":
    category = pg.prompt(
        """
What kind of health-related emergency?
a)Choking
b)Heart attack
c)Allergic reaction

""")
    
pg.alert("""
If you are in immediate danger, please call 911 immediately.
Follow the instructions in the webpages that open following this message for other guidance.
""")
if sport == "a":
    if category == "a":
        webbrowser.open("http://www.redcross.org/get-help/how-to-prepare-for-emergencies/types-of-emergencies/fire/if-a-fire-starts")
    elif category == "b":
        webbrowser.open("https://www.ready.gov/floods")

elif emergency == "b":
    if category == "a":
        webbrowser.open("https://www.youtube.com/watch?v=PA9hpOnvtCk")
    elif category == "b":
        webbrowser.open("https://www.mayoclinic.org/first-aid/first-aid-heart-attack/basics/art-20056679")
