#
# debug_4.py =>
#
# L3 extra problem:
#
# What does this do?
# We'll run it in the PyCharm debugger and find out...

starting = input("Enter a string: ")

result = ''

for ch in starting:
    result = ch + result

print(result)
