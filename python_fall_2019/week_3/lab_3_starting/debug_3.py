#
# debug_3.py =>
#
# L3 extra problem:
#
# What does this code do?
# We'll run it in the PyCharm debugger and find out...

first_int = 47
second_int = 29

print ('first_int is',first_int,', second_int is',second_int)
first_int = first_int - second_int
second_int = second_int + first_int
first_int = second_int - first_int

print ('first_int is',first_int,', second_int is',second_int)

# Do the following two code examples each compute the same as above?

# temp = first_int
# first_int = second_int
# second_int = temp

# first_int, second_int = second_int, first_int # tuple assignment
