# Angela Holden
# patterns2.py

# Write a program that reads an int N >= 0, then prints out each of the following patterns of *.
# If you do NOT use the string repetition operator * in either problem, you will earn 0.25 points of Extra Credit for each.
# Also, each pattern must be output via a single function call to the given named function with single parameter N.
# Examples for N==4 follow, with explanations of how the displayed diagram reflects this value of N:

# (a) def triangle(N) => N lines, all right justified: first having N stars, second having N-1, ..., and finally the Nth having 1 star):

# ****
#  ***
#   **
#    *

# (b) def hollow_box(N) => N lines, first and last having N stars, others with star in first and Nth column:

# ****
# *  *
# *  *
# ****

import string

# print(string.punctuation) print out the list of punctuation characters
# print(string.punctuation[9]) count the number of characters to find the * index

def triangle(N):
    while N >= 0:
        # print(star * N) This I figured out myself!
        print("{:>4}".format(star * N)) # https://scientificallysound.org/2016/10/17/python-print3/
        N = N - 1

star = string.punctuation[9]
N = 4
triangle(N)

def hollow_box(N):
    for row in range(1, N + 1): # for loop Rows
        for col in range(1, N + 1): # for loop Columns
            if (row == 1 or row == N or col == 1 or col == N):
                print(star, end='') # if row or column is equal to the first or last number in the range, print a star
            else:
                print(' ', end='') # if it's not the first or last in the row or col range print a space
        print()

star = string.punctuation[9]
N = 4
hollow_box(N)
