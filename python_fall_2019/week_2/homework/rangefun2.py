# Angela Holden
# rangefun2.py

x = int(1)
y = int(11)
z = int(1)

for num in range(x, y, z):
    print(num, end=' ')
print() # 1 2 3 4 5 6 7 8 9 10

x = int(1)
y = int(14)
z = int(2)

for num in range(x, y, z):
    print(num, end=' ')
print() # 1 3 5 7 9 11 13

x = int(47)
y = int(22)
z = int(-24)

for num in range(x, y, z):
    print(num, end=' ')
print() # 47 23

x = int(10)
y = int(0)
z = int(-1)

for num in range(x, y, z):
    print(num, end=' ')
print() # 10 9 8 7 6 5 4 3 2 1

x = int(20)
y = int(-1)
z = int(-4)

for num in range(x, y, z):
    print(num, end=' ')
print() # 20 16 12 8 4 0

x = int(3)
y = int(34)
z = int(6)

for num in range(x, y, z):
    print(num, end=' ')
print() # 3 9 15 21 27 33
