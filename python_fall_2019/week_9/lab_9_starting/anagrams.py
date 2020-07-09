"""
Lab 9-4 Module: anagrams.py:

Find and print all words in the largest set of anagram-like words

Starting code follows...

You will find the following operations useful:

    charlist = list(string) => create a list of single chars in string
    word = ''.join(charlist) => join charlist back into a word

"""

def makeSorted(w):
    '''
    Build and return a new string with each of w's chars
      in sorted order:

    Finish this...
    '''
    pass

# open words.txt file for reading (the 'dictionary of words')

wordFile = open("words.txt","r")

# Initialize anagrams as empty dict

anagrams = {}

for word in wordFile: # for each word (== a line from words.txt)...

    # Strip trailing newline from word

    # Create alpha_sort: string with sorted chars in stripped word
    
    alpha_sort = makeSorted(word)
    
    # If alpha_sort already in anagrams dictionary as key:
    #   Append stripped word to anagrams[alpha_sort]
    #          (adding to list of all words having same chars)
    # else:
    #   Set anagrams[alpha_sort] to new list with only stripped word
    #          ([word])

print (anagrams)

input("ENTER to continue:")

wordFile.close()

# Here, dictionary anagrams has all "anagram lists" for dictionary:
# Now build tuple w/ first int elt as length of value list,
#   2nd as value list

anagram_freq = []

# for each list value v in dictionary anagrams
#      append ((len(v),v)) to anagram_freq

# sort anagram_freq in reverse order, ordering by length of list v

anagram_freq.sort(reverse=True)

# print first 20 values of anagram_freq (slices!)

for elt in anagram_freq[:20]:
    print (elt)
