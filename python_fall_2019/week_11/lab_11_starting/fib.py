#
# L11-2: fib.py
#

def F_iter(n):
    # iterative way

    # if n == 0:
    #     return 0
    #
    # if n == 1:
    #     return 1

    if n < 2:
        fibN = n

    fibN_1 = 1
    fibN_2 = 0

    for count in range(n-1):
        fibN = fibN_1 + fibN_2
        fibN_2 = fibN_1
        fibN_1 = fibN

    return fibN

def F_rec(n):
    # do the same but use recursion: no looping!
    pass


def main():
    # finish this
    pass

main()
