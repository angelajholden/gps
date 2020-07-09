# Angela Holden
# mypower.py

def power (base,exp): # these are formal parameters - base: 2 exp: 3

    result = 1
    for counter in range(exp):
        result = result * base

    # return result, now having value base**exp

    return result

def main():

    b = int(input("enter the base: "))
    e = int(input("enter the exponent: "))

    print (b, '**', e, ' is ', power(b,e), sep='')

    print (power(b,e))

main()

