jokes = [ "Calder police - I've been robbed!", "You are welcome!", "Nevermind, it's pointless!" ]

available_jokes = ["robbers", "tanks", "pencils"]

def tell_joke(category):
    setup = ["Knock Knock? "]
    for line in setup:
        input(line)
        if category == "robbers":
            input("Calder... ")
            print(jokes[0])
            if "robbers" in available_jokes:
                available_jokes.remove("robbers")
        elif category == "tanks":
            input("Tank... ")
            print(jokes[1])
            if "tanks" in available_jokes:
                available_jokes.remove("tanks")
        else:
            input("Broken pencil... ")
            print(jokes[2])
            if "pencils" in available_jokes:
                available_jokes.remove("pencils")

def get_feedback(user_response):
    if user_response == "finished":
        rating = int(input("Rate our game 1-10: "))
        print(f"You gave us {rating * 10}% satisfaction!")
        recommend = input("Recommend to a friend? (yes/no) ")
        if recommend == "yes":
            print("Thanks!")
        else:
            print("Oh! sorry to hear that.")

print("Welcome to the Knock-Knock Joke Game!")
want_joke = input("Do you want to hear a joke? (yes/no) ")

if want_joke == "no":
    print("Okay, suit yourself!")
else:
    while want_joke == "yes":
        if len(available_jokes) > 0:
            print(f"Available jokes: {', '.join(available_jokes)}")
            choice = input("Choose a joke: ")
            if choice not in available_jokes:
                print("That joke isn't available.")
            else:
                tell_joke(choice)
            want_joke = input("Another joke? (yes/finished) ")
        else:
            print("You've heard all the jokes!")
            want_joke = "finished"

    get_feedback(want_joke)
    
