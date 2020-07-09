# Angela Holden
# julian.py

# The Julian date of a year is the ordinal number of any date within the year.  For example, January 1 is always Julian date 1, February 1 is Julian date 32, and December 31 is Julian date 365 in non-leap years and 366 in leap years.
#
# Here's a way of calculating the Julian date daynum. Use int arithmetic in these calculations:
#
# (1) daynum = 31*(month−1) + day
# (2) If the month is after February, subtract (4*month + 23) // 10 from daynum
# (3) If it’s a leap year and after February 29, add 1 to daynum
#
# Using this algorithm, write a function julian(day,month,year) which returns the int Julian date of its arguments.  Define a main() function which reads the date from the user as three separate int values; you don't have to verify that it's valid.  Then call your function passing the three input arguments and print the int result.
#
# Hint: use your is_leap(year) function from [H5-4] in your test for (3) above. Also be careful about implementing the above calculations: do them in the order given (do (1) first, then (2), then (3)).

