#
# [iRvQ2-7] What is the output when the following code is run?
#
# t="Moxie"
# for index in range(len(t)-1,0,-1):
#     if index%2 == 0:
#         print (t[index])
#

# len(t) == len("Moxie") == 5
#
# So loop is:
#
# for index in range(5-1,0,-1):
#   ...
# or
# for index in range(4,0,-1):
#
# This results in index taking on values 4,3,2,1
#
# Only the even (4,2) values are printed in print(t[index])
#
# So t[4] == 'e' is printed first,
#   then t[2] == 'x' is printed next:
#
# Output:
#
# e
# x

t="Moxie"
for index in range(len(t)-1,0,-1):
    if index%2 == 0:
        print (t[index])
