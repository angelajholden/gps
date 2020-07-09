# Angela Holden
#
#  unidump.py:
#
#  Skeleton code for H7-2: finish it
#
#  Prompt user to enter int N, then print out N Unicode characters from 32 through 32+N-1, 32 per line, with no intervening spaces.

N = int(input("Enter integer N: "))

for n in range(32, 32+N):
    if n % 32 == 0:  # start next line, then add linenum prefix
        print() # blank line
        print('%04d: ' % n, end='')
    print(chr(n), sep='', end='')

print() # blank line
