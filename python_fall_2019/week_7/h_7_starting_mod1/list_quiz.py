# Angela Holden
# list_quiz.py:
#
#   Starting code for H7-3
#

# Give short one-question quiz on HTT10 (Lists) to user

print('''\nWhat will the following code print:

    phrase = "Sometimes you feel like a nut, sometimes you don't..."
    words = phrase.split()
    result = ""
    for w in words:
        result = result + w[0]
    print(result) 
''')

answer = input("? ")

if answer == 'Syflansyd':
    print('\nYes! You are correct.')
elif answer == 'syflansyd':
    print('\nYes, but you didn\'t capitalize the first S.')
else:
    print('\nNope. The correct answer is: Syflansyd')

print('''\nFirst use .split() to split each word in the phrase.
Next use an accumulator pattern to grab the first letter, or [0] index, of each word.
Then print the first letter of each word in a neat row.
Something to note; punctuation is not included as a delimiter when splitting.
''')
