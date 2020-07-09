# Write a Python definition for a function named cross. 
# It should have four formal parameters named x1, y1, x2 and y2.
# When called, it should compute and return the square root of x1 times y1 plus x2 times y2.
# You don't have to call this function: just write its definition.

import math

def cross(x1, y1, x2, y2):
	math.sqrt(x1) * y1 + x2 * y2
	return cross



def a(x,y):
	t = x - y
	return t

def b(w):
	u = a(w, 2) + a(2, w + 1)
	return u

moxie = 47
result = b(moxie)
print(result)

b(47)

u = a(47, 2) + a(2, 47 + 1)

t = 47 - 2
t = 45

t = 2 - 47 + 1
t = -44

u = 45 + -44
u = 1

result = 1
print("The result is " + 1)



if x==y:
    print("x==y")
elif x > y:
    print(x)
else:
    print(y)


4 * 3 + 2 ** 2 // 10 // 5


#n = input (Enter an integer: ']
# there should not be a space between input and opeing paranthesis
# missing opening single quote before Enter
# closing bracket after closng single quote should be closing paranthesis
#print ('A random integer k with k\'s value in -n<=k<n is:', random.randrange(-n,n)
# space and single quote after the word integer
# + sign before and after k to concatenate
# single quotes around the word 'with'
# + sign before k to concatenate
# single quote and forward slash before s
# single quotes around words 'value in'
# + sign after closing quote of phrase value in to concatenate
# add a single opening quote before the word is
# add a closing parenthesis at the end of the print statement
# Here's how it should look:
n = input('Enter an integer: ')
print('A random integer ' + k + 'with ' + k '\'s value in ' + -n<=k<n + 'is: ', random.randrange(-n,n))



# Write a complete Python program that generates and prints the square root of the sum of the squares of two separate random integers, each in the range 1 and 10, inclusive.

# "Inclusive" means both 1 and 10 should be possible values for the random int, as well as 2,3,4,5,6,7,8, and 9.

import random

def square(x):
  y = x * x
  return y

def sumofsquares(x, y):
  a = square(x)
  b = square(y)

	return a + b
	
a = random.randrange(1, 10)
b = random.randrange(1, 10)
result = sumofsquares(a, b)
print(result)


def square(x):
    runningtotal = 0
    for counter in range(x):
        runningtotal = runningtotal + x
    return runningtotal

if a == b:
    print("==")
elif a > b:
    print(">")
else:
    print("<")

if a < b:
  print("<")
else:
  if a > b:
    print(">")
  else:
    print("==")

    