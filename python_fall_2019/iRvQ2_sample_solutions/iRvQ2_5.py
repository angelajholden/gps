#
# [iRvQ2-5] The following code has an infinite loop.  Explain why.
#
# n = 7
# m = 5
# count = 0
# while n*m != 0:
#     count = count + n*m
#     m = m - 2
#     n = n + 2
# print(count)
#

# The continues while n*m != 0, meaning it ends
#   when n*m==0.
#
# This implies that either n or m must be 0 to end the loop.
#
# But n and m are initialized to odd integers, and are modified at the
#   bottom of the while-loop.
#
# This modification keeps both n and m as odd numbers (odd - 2 is odd, odd + 2 is odd)
#   But this means n*m can never be 0, since odd*odd is odd != 0 an even value.
#
# So the loop never ends...
#

n = 7
m = 5
count = 0
while n*m != 0:
    count = count + n*m
    m = m - 2
    n = n + 2
print(count)


