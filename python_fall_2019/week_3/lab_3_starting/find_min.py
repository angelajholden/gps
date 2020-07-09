#
# L3-5: find the logical bug in the following program
#

# Angela Holden
# find_min.py
# I'm not sure what the bug is. I had trouble getting the debugger to work.

import math

number = int(input("Enter number of ints to process: "))

min_so_far = 0.0

for count in range(number):
    next_int = int(input("Enter next integer: "))
    min_so_far = min(min_so_far, next_int)  # note the built-in function min()

print("Smallest entered is:", min_so_far)

