name = "Ryan Brush"

subjects = ["English","Math","Science","History","Latin"]

print("Hello " + name)

for i in subjects:
    print("One of my subjects is " + i)

characters = ["Kensi","Deeks","Callen","Sam","Mosely"]

for i in characters:
    if i == "Callen":
        print(i + " is my favorite!")
    elif i == "Mosely":
        print(i + " is the assistant director.")
    else:
        print("One great character in NCIS: Los Angeles is " + i)



movies = []

while True:
    print("What's one of your favorite movies? Type 'end' to quit")
    answer = input()
    if answer == "end":
        break
    else:
        movies.append(answer)

for i in movies:
    print("One of your favorite movies is " + i)
