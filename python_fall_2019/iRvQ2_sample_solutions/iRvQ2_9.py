
# [iRvQ2-9] Write code that alters in place the following list alist
#     so that every even integer in alist is replaced with 0.
#
# 'Top-level list element' means 'an element accessed via alist[k]
#  for some k and is itself a list. "In place" means that list alist should reference the same list in memory after your code executes.
#
# alist = [[1,2],3,4,[[5,6],7]]
#

# Even integers are 2,4,6
# These elements are alist[0][1], alist[2], and alist[3][0][1]
#
# set each of these to 0:

alist = [[1,2],3,4,[[5,6],7]]
print ("original alist is %s" % alist)

alist[0][1] = 0
alist[2] = 0
alist[3][0][1] = 0

print ("altered alist is %s" % alist)

