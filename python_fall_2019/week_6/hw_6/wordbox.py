# Angela Holden
# wordbox.py

# Write a program which reads a word, lower-cases all its letters, then prints out a square array where the first row contains the word, and each subsequent line is the previous line circular-shifted one place to the left.  Example for entered word word == "MoXiE":
#
# moxie
# oxiem
# xiemo
# iemox
# emoxi
#
# Try doing this any way you can.
#
# Hint 1: lower-case word, then repeat the following len(word)times: (a) print word, (b) move first char of word to end.
# Hint 2: lower-case word, then think about selecting len(word) characters from word+word - by slicing!

word = "MoXie"
word = word.lower()

idx = 0

for n in range(len(word)):
    newWord = word[idx:] + word[0:idx]
    idx = idx + 1
    print(newWord)
