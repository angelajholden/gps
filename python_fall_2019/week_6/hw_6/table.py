# Angela Holden
# table.py

# Do Exercise 4 at the end of HTT9, but only print a 9 x 9 table of products.
# Your table should look like this:

# |  * | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 |
# --------------------------------------------------------
# | 00 | 00 | 00 | 00 | 00 | 00 | 00 | 00 | 00 | 00 | 00 |
# | 01 | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 |
# | 02 | 00 | 02 | 04 | 06 | 08 | 10 | 12 | 14 | 16 | 18 |
# | 03 | 00 | 03 | 06 | 09 | 12 | 15 | 18 | 21 | 24 | 27 |

# ....and so forth.This means that each cell's numeric entry must be exactly 2 digits, with a leading 0 if necessary.
#
# Each of the numeric cells is exactly 4 characters wide, with the two-digit entry centered therein.
#
# Finally, you MUST use nested for-loops to print out each row of the table, after the initial header row "|  * | 00 |...", followed by the row of -.
#
# The outer for-loop must be of the form for row in range(10): with a loop body that prints out the formatted value of row(leftmost cell), then with the inner loop of the form for col in range(10): with a loop body that prints out the next cell's value of row*col, formatted as above with | as cell delimiters.

print("| " + " *", end=" ")
for h in range(10):
    num = "0" + str(h)
    if (h == 9):
        print("| " + num, end=" |\n")
    else:
        print("| " + num, end=" ")

for b in range(10 + 1):
    border = ("-----")
    print(border, end="")
print("-")

for row in range(10):
    leftcol = "0" + str(row)
    print("| " + leftcol, end=" ")
    for col in range(10):
        result = row * col
        if (result <=9):
            print("| " + "0" + str(result), end=" ")
            if (col == 9):
                print(end="|\n")
        elif (col == 9):
            print("| " + str(result), end=" |\n")
        else:
            print("| " + str(result), end=" ")
