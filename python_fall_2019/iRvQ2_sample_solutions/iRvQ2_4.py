#
#[iRvQ2-4] What does the following code print? Also, under each
#  Boolean operator and and or in the print() statement,
#  write the number that gives the order in which that operator
#  is applied in the evaluation of the expression with the given values.
#  Write 1 under the operator that's applied first, 2 under the second,
#  and so forth.  Note that due to Boolean operator "short circuiting",
#  you may have some operators that are never applied in evaluating
#  the expression within print().

larry = 'curly'
moe = 'larry'
curly = 'moe'
print (larry > curly or larry < moe and curly < moe and len(larry) > len(moe) or len(moe) < len(curly))

# larry > curly => 'curly' > 'moe' => False ('curly' is before 'moe' in dictionary)
# larry < moe => 'curly' < 'larry' => True ('curly' is before 'larry' in dictionary)
# curly < moe => 'moe' < 'larry' => False ('moe' is after 'larry' in dictionary)
# len(larry) > len(moe) => len('curly') > len('larry') => 5 > 5 => False
# len(moe) < len(curly) => len('larry') < len('moe') => 5 < 3 => False
#
# Thus the above print() statement is equivalent to:
#
# print(False or True and False and False or False)
#
# In above, 'and' is evaluated before 'or': True and False and False,
#   evaluated left to right.
# The leftmost 'and' is evaluated first (1), yielding False which short-circuits
#   the expression evaluation.
#
# Thus the rightmost 'and' isn't evaluated => no number under rightmost 'and'
#
# The remaining 'or' expressions are evaluated left to right, until first True is encountered:
#   but there are no True values, so all 'or's are evaluated:
#
#   The leftmost 'or' is evaluated next (2), then the rightmost 'or' (3)
#
# The above results in:
#
# print(False or True and False and False or False)
#             2        1                  3
#
# So the original print() should be labeled as follows:
#
# print (larry > curly or larry < moe and curly < moe and len(larry) > len(moe) or len(moe) < len(curly))
#                      2               1               -                        3
#
# The result printed is False == False or (True and False and False) or False ==
#  False or False or False ==
#  False



