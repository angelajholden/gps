#
# [iRvQ2-1] What does the following code print?
#
# def one(a,b):
#      return a+b
# def two(a,b):
#      return one(a*b,a-b) - one(b-a,b*a)
# a=1
# b=2
# print (two(a,b))


def one(a,b):
     return a+b

def two(a,b):
     return one(a*b,a-b) - one(b-a,b*a)

a=1
b=2
print (two(a,b))

# two(1,2) =>
# one(1*2,1-2) - one(2-1,2*1) =>
# one(2,-1) - one(1,2) =>
# (2+-1) - (1+2) =>
# 1 - 3 =>
# -2 is printed


