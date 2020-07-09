#
# debug_2.py:
#
# L3-3: We'll run this in the PyCharm debugger to understand print()'s behavior...
#

result = '' # empty string: len(result) == 0
starting = input("Enter a string: ")

print ("'",end='')

for ch in starting:
    print(ch, end='')  # print char but don't start new line (yet)

print ("'",end='')

print(" was your entered string...")  # adds arg to line already being built..

# then adds newline, which then 'flushes" chars accumulated in print buffer,
# printing them out
