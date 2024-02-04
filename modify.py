# Beatrice Akinpelu
# 02/02/2024

# the program greets you with a general message if you enter "you" as your name, greets
# your instructor with a specific message 

# Get the user's name
user_name = input("What is your name? ")

# Define your instructor's name
instructor_name = "Nathan Braun"  # Replace with the actual name of your instructor

# Check if the user is you or your instructor
if user_name.lower() == "you":
    print("Hello, you! Nice to meet you.")
elif user_name.lower() == instructor_name.lower():
    print(f"Hello, {Nathan Braun}! It's great to see you.")
else:
    print(f"Sorry, {user_name}, I'm programmed to greet only you and your instructor.")
