movies = {
    "Nice Guys": [3,5],
    "Skyfall": [18,2],
    "Fight Club": [12,5]
}

while True:
    choice = input("What movie would you like to watch?" ).strip().title()
    if choice in movies:
        age = int(input("How old are you? ").strip())

        # Check user age
        if age >= movies[choice][0]:
            # Check capacity
            num_seats = movies[choice][1]
            if num_seats > 0:
                print("Enjoy the film!")
                movies[choice][1] = movies[choice][1] - 1
            else:
                print("Sorry, we are all out of tickets for that movie")
        else:
            print("You are not old enough to view this movie")

    else:
        print("We don't have that movie")
    