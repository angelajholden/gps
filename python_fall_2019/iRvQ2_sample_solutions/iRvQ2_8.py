#
# [iRvQ2-8] Define a function check_if_entry(d,k,v) for dictionary d, string k, and string v.
#
#    It should return True if k is a string key in the dictionary d with string value v;
#      otherwise, return False.
#
#
# Check if key k is in dictionary d:
#
# if k in d.keys(): # equivalently => if k in d:
#
# Within this if-statement, check if v is value for d[k]:
#
#   if d[k]==v:
#
# Return True if yes, False otherwise
#
#        return True
#   else:
#        return False
#
# Finally, if k is not a key in d, return False:
#
# else:
#     return False

def check_if_entry(d,k,v):

    if k in d:
        if d[k]==v:
            return True
        else:
            return False
    else:
        return False

# test this...

d = {1:'one',2:'two',3:'three'}

print ("check_if_entry(d,1,'one') is %s" % check_if_entry(d,1,'one')) # key 1 has value 'one'
print ("check_if_entry(d,2,'dos') is %s" % check_if_entry(d,1,'dos')) # key 2 doesn't have value 'dos'
print ("check_if_entry(d,3,'three') is %s" % check_if_entry(d,3,'three')) # key 3 has value 'three'
print ("check_if_entry(d,47,'magic') is %s" % check_if_entry(d,47,'magic')) # no such key 47 in d

