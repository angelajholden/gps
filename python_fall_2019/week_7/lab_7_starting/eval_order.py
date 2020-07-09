#
# Experiment:
#
# In what order does the interpreter evaluate the subexpressions within
#   the following expression?
#
#  moxie > 64 or anna != 23 and moxie < 64 or anna == 23

def moxie_gt_64():
    print ("moxie > 64 evaluated...")
    return moxie > 64

def anna_ne_23():
    print ("anna != 23 evaluated...")
    return anna != 23

def moxie_lt_64():
    print ("moxie < 64 evaluated...")
    return moxie < 64

def anna_eq_23():
    print ("anna == 23 evaluated...")
    return anna == 23


moxie = 64
anna = 22

print ("eval of expression:")
print (moxie > 64 or anna != 23 and moxie < 64 or anna == 23)

print("eval order shown by function all output (no parentheses):")
print (moxie_gt_64() or anna_ne_23() and moxie_lt_64() or anna_eq_23())

print("eval order for fully parenthesized expression")
print ((moxie_gt_64() or (anna_ne_23() and moxie_lt_64())) or anna_eq_23())

print ((moxie > 64) or ((((anna != 23)) and (moxie < 64))) or anna == 23)


