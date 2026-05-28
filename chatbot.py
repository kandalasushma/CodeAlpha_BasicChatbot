while True:
    user = input("You: ").lower()

    if user == "hello":
        print("Bot: Hi!")

    elif user == "how are you":
        print("Bot: I'm fine, thanks!")

    elif user == "bye":
        print("Bot: Goodbye!")
    
    elif user == "what are you doing":
        print("Bot: nothing")
        break

    else:
        print("Bot: I don't understand.")