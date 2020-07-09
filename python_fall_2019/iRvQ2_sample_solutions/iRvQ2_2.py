#
# [iRvQ2-2] What are the sentinel values for input in the following code?
#
# sum = 0
# input_int = int(input("Enter an integer: "))
# while input_int % 2 == 0:
#     sum += input_int
#     print(input_int)
#     input_int = int(input("Enter an integer: "))
# print (sum)
#

#
# The following code terminates input when input_int % 2 != 0,
#   meaning input_int is an odd integer
#
# Thus any odd integer is an input sentinel
#

sum = 0
input_int = int(input("Enter an integer: "))
while input_int % 2 == 0:
    sum += input_int
    print(input_int)
    input_int = int(input("Enter an integer: "))
print (sum)

