#
# out_riffle.py:
#
# 	Starting code for L10-4
#

import deck as d

def main():

    the_deck = d.Deck()
    the_deck.shuffle()

    the_deck.dealCard() # after 8 out-shuffles, deck returns to original state.
    the_deck.dealCard() # after 21 out-shuffles, deck returns to original state.
    the_deck.dealCard() # after 21 out-shuffles, deck returns to original state.
    the_deck.dealCard() # after 23 out-shuffles, deck returns to original state.

    original_deck = str(the_deck)

    print (the_deck)

    out_shuffle_count = 0

    while True:

        the_deck.outRiffle()
        out_shuffle_count += 1

        if str(the_deck) == original_deck:
            break

    print ('after',out_shuffle_count,'out-shuffles, deck returns to original state.')

main()