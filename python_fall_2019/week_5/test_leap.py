# Angela Holden
# test_leap.py

# The year y is a leap year if and only if y is evenly divisible by 4, but not by 100 - or if y is evenly divisible by 400.  Thus, 2016 is a leap year (evenly divisible by 4 but not by 100.  1900 is NOT a leap year, since it's evenly divisible by 100 but NOT by 400.  And 2000 IS a leap year, since it's evenly divisible by 400.
#
# Define a bool function is_leap(year) which returns True if year is a leap year, and False otherwise.  Then write 10 different pytest test functions, each of which tests a different year.  Try to pick a variety of both leap and non-leap years. Put both your function and your tests in the same file. Also be sure there's no console input or output within your code, or pytest will complain.
#
# Remember that each such pytest test function must (a) have a name that starts with test_, (b) have no arguments, and (c) provide a test of the form assert is_leap(YYYY)==True if YYYY is a leap year, or assert is_leap(YYYY)==False if not.
#
# No main() function here: just the function definition and the 10 pytest test methods.

