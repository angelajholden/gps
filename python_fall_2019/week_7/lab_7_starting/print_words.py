#
#   L7-6 - print_words.py:
#
#       Starting code
#

def split_into_words(big_string):
    pass

def print_longest_v1(all_words):
    pass

def print_longest_v2(all_words):
    pass

def print_first_2_equals_last_2 (all):
    pass

def main():

    FILENAME = 'words_2.txt'

    fvar = open (FILENAME, 'r') # open file for reading

    big_string = fvar.read() # read the entire file into a single string

    # (a) split big_string into list of words (works since one word per line in file)

    all_words = split_into_words(big_string)

    # (b) find longest word in file via accumulator

    print_longest_v1(all_words)

    # (c) find longest word using sorted list of (length,word) tuples

    print_longest_v2(all_words)

    # (d) find all words with first two chars == last two (example bonobo

    print_first_2_equals_last_2(all_words)

    fvar.close()

main()
