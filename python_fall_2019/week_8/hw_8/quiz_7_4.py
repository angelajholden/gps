# What does the following code print?

# moxie = "dog"
# anna = "girl"
#
# print (moxie < anna and moxie > "apple" or len(anna) < 3)

# What does the following code print?

# def expp(a,b,c):
#     y = a**b**c
#     return y
#
# def mystery(x):
#     a = expp(x,2,1) + expp(2,1,x)
#     return a
#
# n = 2
# result = mystery(n)
# print(result)

# Complete the following code by adding one or more statements in each underlined area.  Resulting code should print answer as the sum of the odd integers from 1 through 45, inclusive.
#
# ____________________
#
# while n < 47:
#     answer = answer + n
#     __________________
# print(answer)
#
# You CANNOT change any code; just add new code in given areas.

answer = 0
n = 1
while n < 47:
    if n % 2 == 1:
        answer = answer + n
    n = n + 1
print(answer)
