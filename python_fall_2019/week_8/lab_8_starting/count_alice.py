#
# count_alice.py:
#
#   Starting code L8-3
#

FILENAME = 'alice.txt'

fvar = open (FILENAME, 'r') # open file for reading

allwords = [] # accumulate the words in this list

for aline in fvar:

    aline = aline.replace('"', ' ')
    aline = aline.replace('?', ' ')
    aline = aline.replace('!', ' ')
    aline = aline.replace('.', ' ')
    aline = aline.replace(',', ' ')
    aline = aline.replace(';', ' ')
    aline = aline.replace(':', ' ')
    aline = aline.replace('--', ' ')
    aline = aline.replace('(', ' ')
    aline = aline.replace(')', ' ')
    aline = aline.replace('[', ' ')
    aline = aline.replace(']', ' ')
    aline = aline.replace('_', '')

    words = aline.lower().split() # splits the line on whitespace (blanks, '\n', '\t')

    #print (words) # just to see the words flying across the screen...

    # allwords.append(words) # why doesn't this work?

    allwords.extend(words) # this does...

    # allwords = allwords + words # as does this - but why is this inefficient?

print(allwords)
print('There are {} in the story.'.format(len(allwords)))
print('The word \'alice\' occurs {} times.'.format(allwords.count('alice')))

final_allwords = []

for each_word in allwords:
    if each_word is not "'":
        final_allwords.append(each_word)

print('There are {} words in the story.'.format(len(final_allwords)))
print('The word \'alice\' occurs {} times.'.format(final_allwords.count('alice')))

final_allwords.sort()
for w in final_allwords:
    print(w)

fvar.close()
