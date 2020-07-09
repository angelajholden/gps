# Angela Holden
# interest.py

# [H2-5](interest.py) Exercise 7 at the end of HTT2 (in HTT2.13) gives a Python program that computes compound interest.
# The provided code does this by using a formula using the exponentiation operator **:
#
# b**n == b*b*...b (n times).
#
# Rewrite this program without using this ** operator.
# Use a for-loop to compute r = b**e in the following way:
#
# result = 1
# for counter in range (e):
#     result = result * b
#
# You may assume that e is always an int value.

m = input('Enter a number: ')
n = input('Enter an exponent: ') # even though I don't use **

b = int(m)
e = int(n)

result = 1

for counter in range(e):

    counter = counter * counter

    result = result * b

print(result)

