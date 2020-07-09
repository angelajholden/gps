# Angela Holden
# linenum.py:
#
#   Starting code for L8-1
#

# read filename fname from user
fname = input("Enter the file name to process: ")

# open file named fname for reading
file_var = open(fname, 'r')

# open file named 'lnum_' + fname for writing
out_var = open('lnum_' + fname, 'w')

# iterate over each line within fname:

linenum = 1


for each_line in file_var:
    # print(each_line[:-1]) # slicing to remove the newline/double spacing, can also use 'end=""'

#   modify the line by adding 'dddd: ' to the start of the line
    each_line = ('%04d: ' % linenum) + each_line

#   write this modified line to output file
    out_var.write(each_line)

    linenum = linenum + 1

# close both files
file_var.close()
out_var.close()
