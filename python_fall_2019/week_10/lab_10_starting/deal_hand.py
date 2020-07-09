#
# deal_hand.py:
#
# 	Starting code for L10-3
#
#   Modify Deck.dealHand() as described in handout
#

import deck as d


def main():

    the_deck = d.Deck()

    for count in range(11):
        hand = the_deck.dealHand()  # last hand will empty the_deck: should not crash!

        print([str(c) for c in hand])

main()
