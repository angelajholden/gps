# Angela Holden
# boolexpr.py

# Write a Boolean (bool) function is_in_semester(month,day) that returns True when month/day falls within the dates of our current GPS Fall Semester 2019, starting on September 4 and ending on December 13. If month/day falls outside this range (which includes both starting and ending dates), return False.
#
# Then write a main() function that reads integers month and day from the user, calls is_in_semester(month,day), then prints out 'month/day is in Fall Semester' or 'month/day is NOT in Fall Semester'. Example for month==12, day==1 => print 12/1 is in Fall Semester. Finally, call main() as the last statement in your .py file.
#
# Note that your function should only return True or False, with main()calling is_in_semester(...), then printing out the text which depends upon its bool returned value. No "chatterbox functions"! See the HTT6 Glossary...

def is_in_semester(month, day):
    if month == 9:
        if day >= 4 and day <= 30:
            result = True
    elif month == 10:
        if day >= 1 and day <= 31:
            result = True
    elif month == 11:
        if day >= 1 and day <= 30:
            result = True
    elif month == 12:
        if day >= 1 and day <= 13:
            result = True
        else:
            result = False
    else:
        result = False

    return result

month = 12
day = 15

main = is_in_semester(month, day)

if main == True:
    print (str(month) + "/" + str(day) + " is in Fall Semester.")
else:
    print (str(month) + "/" + str(day) + " is NOT in Fall Semester.")
