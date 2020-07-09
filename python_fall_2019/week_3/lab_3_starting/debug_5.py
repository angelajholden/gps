#
# debug_5.py =>
#
# L3 extra problem:

# Note this code defines and a function using def
# More on this topic in HTT6...

# What does the following code do?

# We'll run it in the PyCharm debugger and find out...

def quot(x, y):
    z = x / y
    return z

def prod(x, y):
    a = quot(x, y) * (quot(y, x) ** 2)
    return a

print(prod(3, 4))
