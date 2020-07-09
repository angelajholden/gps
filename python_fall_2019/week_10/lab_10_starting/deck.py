'''
Represents a standard deck of 52 playing cards,
requiring Card import
'''

#
# out_riffle.py:
#
# 	Starting code for L10-1
#

import card
import random

class Deck():
    """
    Represents a deck of 52 standard playing cards,
        as a list of Card refs
    """

    def __init__(self):
        '''
        Initialize deck: field _cards is list containing
            52 Card refs, initially
        :return: nothing
        '''

        self._cards = []
        for rank in range(1, 14):
            for suit in range(4):
                c = card.Card(rank, suit)
                self._cards.append(c)

    def __str__(self):
        '''
        "Stringified" deck: string of all Card names,
        in deck order separated by '\n' for easier reading
        '''

        toreturn = ''

        # for index in range(len(self._cards)):
        #     self._cards[index]

        for c in self._cards:
            temp = str(c)  # temp is the stringified card
            toreturn = toreturn + temp + "\n"  # note \n at end

        return toreturn

    def shuffle(self):
        random.shuffle(self._cards)  # note random function to do this

    def dealCard(self):
        toreturn = self._cards.pop(0)  # get and remove top card from deck
        return toreturn

    ## L10-1: add new method dealRandomCard()

    def dealRandomCard(self):
        # generate random int in range 0..len(self._cards)

        random_place = random.randrange(0,len(self._cards))

        card_to_return = self._cards.pop(random_place)

        return card_to_return

    ## L10-3: add new method dealHand()

    def dealHand(self):

        hand_to_return = []

        try:
            for count in range(5):
                next_card = self.dealCard()
                hand_to_return.append(next_card)

        except IndexError:

            self.__init__()

            for count in range(5-len(hand_to_return)):
                next_card = self.dealCard()
                hand_to_return.append(next_card)

        return hand_to_return

    ## L10-4: add new method outRiffle()

    def outRiffle(self):

        # list of Cards is self._cards
        # create two empty lists

        top_half = []
        bottom_half = []

        # save # cards in deck

        cards_in_deck = len(self._cards)

        # copy the first half of self._cards into top_half:
        #   (loop cards_in_deck//2 times, deal from deck and append to top_half))

        for count in range(cards_in_deck//2):

            #card_to_move = self._cards[count]
            card_to_move = self.dealCard()

            top_half.append(card_to_move)

        # if cards_in_deck is odd, deal next card and append to top_half

        if cards_in_deck % 2 == 1:
            top_half.append(self.dealCard())

        # now append the remaining self._cards into bottom_half

        for card in self._cards:
            bottom_half.append(card)

        self._cards = []

        # now copy back into new_cards list,
        #   doing perfect out shuffle via alternation

        new_cards = []

        # repeat cards_in_deck//2 times

        for count in range(cards_in_deck // 2):

        #   append next card from top_half to new_cards

            new_cards.append(top_half[count])

        #   append next card from bottom_half to new_cards

            new_cards.append(bottom_half[count])

        # is there one card extra in top_half? (len(top_half) > len(bottom_half)
        #  if so, append this last card of top_half to new_cards

        if len(top_half) > len(bottom_half):
            new_cards.append(top_half[-1])

        # now replace old self._cards with new_cards

        self._cards = new_cards


def main():
    '''
    Create, print then shuffle, print again
    Then deal first two cards and print, along with bottom card
    '''

    deck = Deck()
    print(str(deck))

    print("Now we shuffle:\n")

    deck.outRiffle()
    print(str(deck))

    c = deck.dealCard()

    c2 = deck.dealCard()

    print("The first card dealt is", c, "and the second is", c2)
    print("Bottom of deck is", deck._cards[-1])  # can't hide the implementation!


if __name__ == "__main__":
    main()
