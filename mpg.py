# Beatrice Akinpelu
# 02/02/2024

# this program calculates Miles Per Gallon (MPG) based on user input

# Get user input for miles driven and gallons used
miles_driven = float(input("Enter the number of miles driven: "))
gallons_used = float(input("Enter the number of gallons used: "))

# Calculate MPG
mpg = miles_driven / gallons_used

# Print the result
print(f"Your car's MPG is: {mpg:.2f} miles per gallon.")
