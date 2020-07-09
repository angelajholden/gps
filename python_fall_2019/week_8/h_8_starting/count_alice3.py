# Angela Holden
#
# count_alice3.py:
#
#   Starting code H8-1 (from worked Lab 8-3)
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

    aline = aline.lower()

    # Continue with your code to remove punctuation here,
    #   but leave single quotes (') alone

    words = aline.split() # splits the line on whitespace (blanks, '\n', '\t')

    allwords.extend(words) # add all words in this line to allwords

# Now iterate thru allwords, processing single quotes (apostrophes)
#   and accumulating filtered words in new_allwords as we go...

# new_allwords = allwords

# Suggested code follows for processing single quotes:

new_allwords = []

for word in allwords:
    if word == "'": # toss single-quote words
        continue # new Python keyword: starts next loop iteration
    elif word == "'tis": # check if word is 'tis and add to new_allwords if so
        new_allwords.append(word)
    elif word[0] == '\'': # if it starts with ', remove it and add
        new_allwords.append(word[1:])
    elif word[-1] == '\'': # if it ends with ', remove it and add
        new_allwords.append(word[:-1])
    else: # no ', so just add to new_allwords
        new_allwords.append(word)

new_allwords.sort()

# for w in new_allwords:
#     print(w)

# print (new_allwords)

# Now build and use a dictionary to count each word in new_allwords...

# The following uses code from HTT12 Exercise 3 - but note our overall
#   approach is different with respect to punctuation...

counts = {} # initialize counting dictionary to empty

for word in new_allwords:
    counts[word] = counts.get(word, 0) + 1

keys = list(counts.keys())
keys.sort()

print("%15s - %s" % ("word", "count"))

for k in keys:
    print("%15s - %d" % (k, counts[k]))

print (len(new_allwords))

fvar.close()
