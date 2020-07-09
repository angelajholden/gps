#
# [iRvQ2- 3] Complete the following code by adding one or more
# statements in each underlined area. Your resulting code should
# print answer as the sum of the odd integers from 1 through 47, inclusive.
#
# You CANNOT change any code;
# just add new code in given areas.
#
# ____________________
#
# ____________________
#
# while n < 48:
#     answer = answer + n
#
#     __________________
#
# print(answer)
#

# both n and answer should be initialized:
#  answer is an accumulator => answer = 0
#  n is a counter for the value added repeatedly to answer:
#    n=1 => initial value for summing

answer = 0 # initialize accumulator
n=1 # initialize counter

while n < 48:
    answer = answer + n
    n = n + 2 # advance to next odd
print(answer)

# answer = 1+3+5+7+...+45+47 == 47 + 0+2+4+6+...+44+46
#   == 24 + 2*(1+2+3+...+22+23)
#   == 24 + 2(24*23//2)
#   == 24 + 24*23
#   == 576