#Day 12/50 - AI Python Challenge
#Countdown Timer : Create a simple countdown from 10 to 0.

import time  # Import time module to add delay

def countdown_timer():
    print("⏳ Starting countdown...\n")

    # Loop from 10 down to 0
    for i in range(10, -1, -1):
        print(i)         # Print the current number
        time.sleep(1)    # Wait for 1 second before next number

    print("\n🚀 Time's up!")

# Run the function
countdown_timer()