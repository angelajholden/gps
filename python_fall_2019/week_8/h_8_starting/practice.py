# def one(a, b):
#     return a + b
#
#
# def two(a, b):
#     return one(a * b, a - b) - one(b - a, b * a)
#
#
# a = 1
# b = 2
# print(two(a, b))


# n = 1
# answer = 2
# while n < 48:
#     answer = answer + n
#     n = n + 2
# print (answer)

# larry = 'curly'
# moe = 'larry'
# curly = 'moe'
# print (larry > curly or larry < moe and curly < moe and len(larry) > len(moe) or len(moe) < len(curly))

t="Moxie"
for index in range(len(t)-1,0,-1):
    if index%2 == 0:
        print (t[index])
