#
# list_quiz_example.py:
#
#   Example code for H7-3
#

# Give short one-question quiz on HTT10 (Lists) to user

# THIS CODE IS ONLY AN EXAMPLE! You must do own original quiz
#  question to get credit for this problem...

print('''\nEnter the output of the following code: 

		s = 'moxie, sasha, sandy'
		slist = s.split()
		result = [elt[:-1] for elt in slist] 
		print (result)
		''')

answer = eval(input("? "))  # note the trick with eval(), which allows lists to be entered

if answer == ['moxie', 'sasha', 'sand']:
    print('\nCorrect!')
else:
    print('\nSorry, that is incorrect.')

print('''
s.split() returns a list of strings delimited by *whitespace* 
in the original string: commas are *not* used as delimiters
when splitting. 

Result: slist is ['moxie,','sasha,','sandy']. Note the ',' at 
the end of the first two strings in the list, but not for the third.

Then the list comprehension [elt[:-1] for elt in slist] builds 
a new list, which is bound to result.  Each element in result is 
obtained by trimming the last character from each of slist's elements, 
using the slice [:-1] to pull all but the last char.

print(result) thus yields: 

['moxie','sasha','sand']

''')
