#
# random_card.py:
#
# 	Starting code for L10-1
#

import deck
import card

TRIALS = 1000


def main():

    the_deck = deck.Deck()

    two_ace_count = 0

    for count in range(TRIALS):
        the_deck = deck.Deck()
        the_deck.shuffle()

        card1 = the_deck.dealRandomCard()
        card2 = the_deck.dealRandomCard()
        print(card1, card2)

        # if both are aces, add 1 to two_ace_count

        if card1._rank == 1 and card2._rank == 1:
            two_ace_count += 1

    print (100.0 * two_ace_count/TRIALS)


main()