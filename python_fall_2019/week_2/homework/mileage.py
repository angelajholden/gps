# Angela Holden
# mileage.py

# Write a program that will compute MPG for a car.
# Prompt the user to enter the number of miles driven and the number of gallons used.
# Print a nice message with the answer.

x = input('Enter the miles driven: ')
y = input('Enter the gallons of gas used - whole number only: ')

miles = int(x)
gas = int(y)

mpg = miles / gas

print('Your mileage is ' + str(mpg) + ' mpg.')

