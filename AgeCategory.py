#Day 4/50 - AI Python Challenge
#Age Category : Determine if someone is a child, teenager, adult, or senior based on age.

print("Welcome to the age category clasifier page!")

age = int(input("Plesae Enter your age: "))

# Determine age category:
if age < 12:
    category = 'Child'
elif 13 <= age <=19:
    category = 'Teenageer'
elif 20 <= age <= 64:
    category = 'Adult'
else:
    category = 'Senior Citizen'

print(f'\nYou are categorized as {category}')