#
# Starting code for L8-2
#

def parse_date(dstring):
    ''' Parse dstring as mm/dd/yyyy and return the tuple (mm,dd,yyyy),
        where mm, dd, yyyy are all integers.
        Assume mm/dd/yyyy is valid.
    '''

    dstring_split = dstring.split('/')
    # print(dstring_split)

    # to_return = (int(dstring_split[0]), int(dstring_split[1]), int(dstring_split[2]))

    to_return = [ int(d) for d in dstring_split ]

    return tuple(to_return)

    # pass

def main():

    date = input ("Enter date in form mm/dd/yyyy: ")

    result = parse_date(date)

    print (result)

main()

