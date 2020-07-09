#
# [iRvQ2-10] Print out every character of string s that occurs exactly once within s.
#
# You may assume s has already been assigned a string value.
#

s = input ("Enter a string: ")

print ('Characters of %s that occur exactly once are:' % s)
for each_char in s:
    if s.count(each_char) == 1: # does this character occur just once?
        print (each_char)

