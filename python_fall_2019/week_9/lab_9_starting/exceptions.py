"""
Lab 9-2 Module: exceptions.py

Define read_pos_float() so it throws exception if float <=0.0 is read,
    otherwise return the float

"""

def read_pos_float():
    pass

    # Read a string and cast it to float:
    #     (if user enters an invalid float,
    #      what exception is thrown?)
    #
    # if > 0.0, return it
    # else throw a new Exception exception

def main():
    while True:
        try:
            returned = read_pos_float()
        except BaseException:
            pass
            # if we get here, no problems so exit loop via break

        # Finish the exception handlers below...

        # except < put name of exception for bad floats here >:
        #   print("bad float")
        # except Exception:
        #   print("Exception occurred.")
        #   print("float must be > 0.0.  Please reenter.")

    print('You entered:', returned)
    # Note how this indented statement is OUTSIDE and just after the while-loop

main()
