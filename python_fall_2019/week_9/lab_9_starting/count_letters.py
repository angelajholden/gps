"""
Lab 9-1 Module: count_letters.py:

Print out frequency counts of all letters 'a'..'z', 'A'..'Z' found in input string.
Only counts >0 should be printed.

Starting code follows...

"""

import string

st = input ("Enter a string to count its upper+lower case letters: ")

print ("You entered '%s'" % st)

counts = {} # Initialize new dictionary (counts) to empty

for ch in st:
    pass

    # if ch is upper or lower-case letter: # how to do this?
    #     if ch is already in counts:
    #         add 1 to counts[ch],
    #     else:
    #         initialize counts[ch] to 1

    # Shortcut: use counts.get(key,default_value_if_not_there)

print (counts) # print the raw dictionary, now be populated

# Dictionaries don't store in order of sorted keys by default...
# so we need to get a sorted list of keys
#
# Suggested approach: get keys list via counts.keys() then sort giving skeys

# Now iterate key through sorted keys skeys,
#     fetching each count[key]
#     and print in this format:
#          'E' - 47
#
# Example line of output for key k, value v==counts[k]
#
# print ("'%s' - %d" % (k,v)) => old style printf-formatting
