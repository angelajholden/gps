import random
import math

# randOne = random.randrange(1, 11)
# one = math.sqrt(randOne)
# print(one)
#
# randTwo = random.randrange(1, 11)
# two = math.sqrt(randTwo)
# print(two)
#
# print(one + two)

#Write a complete Python program which prints out the sum of 10 random integers, each in the range [-1,1]. You should be able to generate both -1 and 1 as possible random ints in this code.

#r = range(10)

sum = 0
for i in range(10):
    i = random.randrange(-1, 2)
    sum = sum + i

print(sum)
