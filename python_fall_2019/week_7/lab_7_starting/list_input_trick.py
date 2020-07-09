#
# Lab 7 example showing how to read a list of literals directly from user
#

# eval() is the Python interpreter - available WITHIN the interpreter.  Pretty meta, eh?

def main():

    list1 = eval(input("Enter a list using [...] formatting: "))

    print (list1)

main()
