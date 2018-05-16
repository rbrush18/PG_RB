print("What's your favorite color?")
color = input()

if color == "red":
    print("I love red!")
elif color == "blue":
    print("Red is pretty sweet too!")
elif color == "orange":
    print("Orange is one of our school colors!")
else:
    print(color + " is nice too!")
        

print("What's your favorite subject?")
subject = input()

if subject == "Math" or subject == "math":
    print("That's my favorite as well!")
else:
    print(subject + " is a great course too.")


print("What sport do you like to play most?")
sport = input()

if sport == "hockey" or sport == "hockey":
    print("What position do you play?")
    hockeyposition = input()

    if hockeyposition == "right wing":
        print("I play right wing too!")
    elif hockeyposition == "left wing" or hockeyposition == "center" or hockeyposition == "defense" or hockeyposition == "forward":
        print("That's cool!")

print("What is your favorite video game")
videogame = input()

if videogame == "Madden" or videogame == "madden" or videogame == "Madden 18" or videogame == "madden 18" or videogame == "Madden 17" or videogame == "madden 17":
    print("Same!")
else:
    print(videogame + " is also cool!")
