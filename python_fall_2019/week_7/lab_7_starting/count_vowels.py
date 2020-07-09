#
#   count_vowels.py:
#
#       Starting code for L7-1
#

def count_vowels(str2count):
    return 0

def main():

    string_to_count = input ("Enter string to count vowels therein: ")

# formatting in following is printf-style formatting:

    total_vowel_count = count_vowels(string_to_count)

    print ("The number of vowels in '%s' is %d" % (string_to_count,total_vowel_count))

# here's the same formatting done with new format():

    print ("The number of vowels in '{}' is {}".format (string_to_count,total_vowel_count))

main()

