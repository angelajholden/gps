#
# two_aces.py:
#
# 	Starting code for L10-2
#

import deck

TRIALS = 1000


def main():

    two_aces_count = 0

    for count in range(TRIALS):

        new_deck = deck.Deck()
        new_deck.shuffle()

        # deal card1 from new_deck
        # deal card2 from new_deck

        card1 = new_deck.dealCard()
        card2 = new_deck.dealCard()

        # if card1 and card2 are both aces,
        #   add 1 to both_aces_count

        if card1._rank == 1 and card2._rank == 1:
            two_aces_count += 1

    print (two_aces_count)
    print (100.0*two_aces_count/TRIALS)


main()