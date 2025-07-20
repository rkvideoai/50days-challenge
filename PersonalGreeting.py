#Day 1/50 - AI Python Challenge
#Personal Greeting : Ask for name, age, and favorite color, then create a personalized message.
def personal_greetings():
    #Emoji Unicode
    wave_emoji = "\U0001F44B"      # 👋
    heart_emoji = "\u2764"         # ❤️
    rainbow_emoji = "\U0001F308"   # 🌈
    smile_emoji = "\U0001F60A"     # 😊

    #ask the user for their name
    name = input("What is your name? ")
    #ask the age of the user
    age = input("What is your age? ")
    #ask the user for thier favorite color
    favorite_color = input("What is your favorite_color? ")

    #create personalize message using emoji codes
    message = ( 
     f"\nHello {name}! {wave_emoji}\n" 
     f"You are {age} years young, and love the color {favorite_color}! {heart_emoji}\n"
     f"{favorite_color.capitalize()} is such a beautiful choice! {rainbow_emoji}\n"
     f"Wishing you a joyful day filled with colors and smiles! {heart_emoji} {smile_emoji}"
    )
    #Show the final massage
    print(message)

#run the function
personal_greetings()

