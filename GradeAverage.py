#Day 11/50 - AI Python Challenge
#Grade Average : Calculate average of 5 test scores and determine pass/fail.

def grade_average():
    # Step 1: Create an empty list to hold the test scores
    scores = []

    # Step 2: Use a loop to collect 5 scores from the user
    for i in range(5):
        # Ask user to input a test score
        score = float(input(f"Enter score {i + 1}: "))
        scores.append(score)  # Add it to the list

    # Step 3: Calculate the average score
    total = sum(scores)
    average = total / len(scores)

    # Step 4: Print the average score
    print(f"\n📊 Average Score: {average:.2f}")

    # Step 5: Determine and print pass or fail
    if average >= 40:
        print("✅ Result: Pass")
    else:
        print("❌ Result: Fail")

# Run the function
grade_average()