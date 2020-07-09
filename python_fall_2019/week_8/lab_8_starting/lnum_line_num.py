0001: # Angela Holden
0002: # linenum.py:
0003: #
0004: #   Starting code for L8-1
0005: #
0006: 
0007: # read filename fname from user
0008: fname = input("Enter the file name to process: ")
0009: 
0010: # open file named fname for reading
0011: file_var = open(fname, 'r')
0012: 
0013: # open file named 'lnum_' + fname for writing
0014: out_var = open('lnum_' + fname, 'w')
0015: 
0016: # iterate over each line within fname:
0017: 
0018: linenum = 1
0019: 
0020: 
0021: for each_line in file_var:
0022:     # print(each_line[:-1]) # slicing to remove the newline/double spacing, can also use 'end=""'
0023: 
0024: #   modify the line by adding 'dddd: ' to the start of the line
0025:     each_line = ('%04d: ' % linenum) + each_line
0026: 
0027: #   write this modified line to output file
0028:     out_var.write(each_line)
0029: 
0030:     linenum = linenum + 1
0031: 
0032: # close both files
0033: file_var.close()
0034: out_var.close()
