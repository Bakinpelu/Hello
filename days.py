# Beatrice Akinpelu
# 02/02/2024

# this program takes the starting day number and the length of the stay as input and calculates
# the day of the week you will return on

def calculate_return_day(start_day, length_of_stay):
    days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    return_day = (start_day + length_of_stay) % 7

    return days_of_week[return_day]

# Get user input for starting day and length of stay
start_day = int(input("Enter the starting day number (0 for Sunday, 1 for Monday, ..., 6 for Saturday): "))
length_of_stay = int(input("Enter the length of your stay in nights: "))

# Calculate and print the return day
return_day = calculate_return_day(start_day, length_of_stay)
print(f"You will return home on a {return_day}.")
