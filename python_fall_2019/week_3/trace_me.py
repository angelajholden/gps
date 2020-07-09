#
# H3-5: run the following in the PyCharm debugger and print
#       the following requested info...

import math

# What are we trying to accumulate in l, when the following code is executed?
# Hint: it doesn't do it correctly...

num = int(input("enter number of floats: "))

l = 0.0

for b in range(num):
    a = float(input("enter next float: "))
    l = min (l, abs(a-math.pi))

    print ("set breakpoint on this line...")
    # LOCATION 1:

print (l)

print ("set another breakpoint on this line...")

# LOCATION 2:
# list values of a, b, and l for each time through loop (b=0,1,2,3,4)
# list final values of a, b, and l
