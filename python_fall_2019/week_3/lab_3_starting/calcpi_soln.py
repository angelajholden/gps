import math
import random

print(math.pi)  # see what value we're aiming to approximate...

# 1: Read the int value of N from the user

N = int (input("Enter number of trials: "))

# 2: Set up an accumulator counter named in_circle, initialized to 0;
#    Similarly for pi_estimate

in_circle = 0
pi_estimate = 0.0

# 3: Repeat N times => for count in range(...):

for count in range(N):
    # print out the current count for every 1000th iteration
    if count % 1000 == 0:
        print (count)

    # 3.1: Generate a random x in the range (-1.0,1.0)
    # 3.2: Generate a random y in the same range

    x = random.uniform(-1.0,1.0)
    y = random.uniform(-1.0,1.0)

    # 3.3: Calculate distance d of (x,y) from (0,0)

    distance = math.sqrt((x-0.0)**2 + (y-0.0)**2)

    # 3.4: if d within unit circle (d <= 1.0):
    #           increment in_circle count

    if distance <= 1.0:
        in_circle += 1 # in_circle = in_circle + 1

# 4. (NOT in the above loop body's 3.1, 3.2, 3.3)
#    Print out the final value of pi_estimate as 4 times in_circle
#    divided by N and its difference from math.pi.

pi_estimate = 4 * in_circle / N
print (pi_estimate, abs(pi_estimate-math.pi))
