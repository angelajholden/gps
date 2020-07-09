# Angela Holden
# randN.py

import random

numRolls = int(input('Enter a number: '))

sum = 0

for num in range(numRolls):
    num = random.randrange(1, 7)

    #print(num)

    sum = sum + num

#print(sum)

aveRoll = sum / numRolls

print(aveRoll)

# The average number of rolls varies by a fraction as the number of rolls goes up.

