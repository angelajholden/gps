# Angela Holden
# noexp.py

e = input('Enter a number: ')
p = input('Enter its exponent: ')
x = int(e) # convert e to an int
n = int(p) # convert n to an int
result = 1
for counter in range (n):
    result = result * x

print(result)
