#
# modules_2.py =>
#
# L3-6 problem:
#
# Run this and observe the output.
#
# Then uncomment the four r.seed(...) statements, and rerun.
#
# We'll discuss in class why the output changes, and explain why r.seed() is useful
#

import random as r

print("\nwith seed(4747):\n")
# r.seed(4747)
for count in range(5):
    print(r.randint(1, 10))

print("\nwith seed():\n")
# r.seed()
for count in range(5):
    print(r.randint(1, 10))

print("\nwith seed(4747):\n")
# r.seed(4747)
for count in range(5):
    print(r.randint(1, 10))

print("\nwith seed():\n")
# r.seed()
for count in range(5):
    print(r.randint(1, 10))
