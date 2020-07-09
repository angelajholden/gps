#
#   patterns.py:
#
#     Starting code for Lab 6-2
#

def main():

    N = int(input("Enter an integer N: "))


    # (a) single line of N *

    print('*' * N)

    print('\n')

    for count in range(N):
        print('*', end='')
    print() #separator

    print('\n')

    # (b) square of N by N *

    for count in range(N):
        print('*' * N)

    print('\n')

    for rownum in range(N): # no star operator, use nested loops
        for colnum in range(N):
            print('*', end='')
        print()  # separator

    # (c) triangle as shown

    print('\n')

    for count in range(1, N+1):
        print('*' * count)

    for count in range(N):
        print('*' * (count+1))


main()

