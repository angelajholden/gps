# Suppose numbers references a list of integers.  Write Python code which doubles each of the elements of numbers in place.
#
# "In place" means that list numbers should reference the same list in memory before and after your code executes.
#
# numbers = [1, 2, 3, 4, 5]
# number_ref_copy = numbers

# your code here



# Make sure
#    (numbers is number_ref_copy) == True
# after your code executes

# numbers = [1,2,3,4,5]
#
# number_ref_copy = [item ** 2 for item in numbers]
#
# print(number_ref_copy)

# Find the value of string myname, such that
# the following code prints ['', '', '1', '1111']

# myname = "00101111"
# init = myname.split('0')
# print(init)

# Suppose the text file myname.txt contains three lines, each terminated by a newline ('\n').
#
# When the code below is executed, the output is:
#
# Eric
# Vernon
# Level
#
# Find the values of the original three lines in myname.txt.

# file_ref = open ("myname.txt","r")
# aline = file_ref.readline()
# bline = file_ref.readline()
# cline = file_ref.readline()
# print(linelist[0:2])
# print (aline+bline+cline)
# file_ref.close()

# moxie = 'dog'
# anna = 'girl'
# print (moxie > anna or moxie < 'apple' and len(anna) > 3)

# def exor(a, b):
#     y = a and not b or not a and b
#     return y
#
# def mystery(x):
#     a = exor(exor(x,not x),exor(not x,x))
#     return a
#
# n = 47
# result = mystery(n % 47 == 0)
# print(result)

# x = 5
#
# if x <= 0:
#     if x < 0:
#         print(x, "is invalid")
#     else:
#         print(x, "is 0")
# else:
#     print(x, "is positive")
#
# # elif x > 0:
# #     print(x, "is positive")
# # else:
# #     print(x, "is 0")

s = 'pumpkin'
print (s[s.find('x')] * s.index('p'))
