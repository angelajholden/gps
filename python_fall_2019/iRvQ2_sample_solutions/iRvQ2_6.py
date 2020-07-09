#
# [iRvQ2-6] Write Python statements which assign values to a and b,
# such that their reference diagram looks like this: (see iRvQ_6.jpg)
#

# Build separate lists of length 3 for each of a and b;
#   each element of both are initially 47

a = [47,47,47]
b = [47,47,47]

# Now make a[0] (first a element) refer to b:

a[0] = b

# Then make each of b[0],b[1],b[2] refer to a:

b[0] = a
b[1] = a
b[2] = a



