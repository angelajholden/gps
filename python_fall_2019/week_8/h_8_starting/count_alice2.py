# Angela Holden
#
# count_alice2.py:
#
#   Starting code for H7-1
#
# start with your Lab 7 count_alice and continue...

FILENAME = 'alice.txt'

fvar = open(FILENAME, 'r')  # open file for reading

allwords = []  # accumulate the words in this list

for line in fvar:

    line = line.replace('"', ' ')
    line = line.replace('?', ' ')
    line = line.replace('!', ' ')
    line = line.replace('.', ' ')
    line = line.replace(',', ' ')
    line = line.replace(';', ' ')
    line = line.replace(':', ' ')
    line = line.replace('--', ' ')
    line = line.replace('(', ' ')
    line = line.replace(')', ' ')
    line = line.replace('[', ' ')
    line = line.replace(']', ' ')
    line = line.replace('_', '')

    line = line.lower()  # lower case it

    words = line.split()  # splits the line on whitespace (blanks, '\n', '\t')

    allwords.extend(words)

final_allwords = []

for each_word in allwords:
    if each_word is not "'":
        if each_word[0] == "'":
            each_word = each_word[1:]
        final_allwords.append(each_word)

# I could not figure out how to keep the ' before tis and till. I tried a couple of ways to add the ' back in to those two words specifically, but I couldn't get the logic right. Other than specifically looking to see which words need it, how does the program know what word should or should not have an ' without explicitly telling it those words. I'd love to know what the solution to this is.

final_allwords.sort()
for w in final_allwords:
    print(w)

print('There are {} words in the story.'.format(len(final_allwords)))

print(len(final_allwords))

fvar.close()
