# Angela Holden
#
# H8-2: test_poker_odds2.py
#
#   Starting code H8-2
#

import random

# The following two lists of str are used to translate from internal int
#   representation to external string equivalent

SUITS = ["Clubs", "Diamonds", "Hearts", "Spades"]
RANKS = ["", "Ace", "Two", "Three", "Four", "Five", "Six", "Seven",
         'Eight', "Nine", "Ten", "Jack", "Queen", "King"]

# Here's two Python classes whose objects represent a playing card
#   and a deck of such cards

class Card():

    """
    Represents a single playing card,
        whose rank internally is int _rank: 1..13 => "Ace".."King"
        and whose suit internally is int _suit 0..3 => "Clubs".."Spades"
    """

    def __init__(self, rank=1, suit=3): # this is the constructor!

        '''
        Initialize card with given int suit and int rank
        '''
        self._rank = rank
        self._suit = suit

    def __str__(self): # this is the "stringifier" or cast operator

        """
        Return the string name of this card:
        "Ace of Spades": translates int fields to strings
        """

        # Example:
        #
        # "Ace of Spades" is returned if self._rank==1, self._suit==3

        str_to_return = RANKS[self._rank] + " of " + SUITS[self._suit]

        return str_to_return


class Deck():

    """
    Represents a deck of 52 standard playing cards,
        as an internal field referencing a list of Card refs
    """

    def __init__(self): # constructor

        """
        Initialize deck: field _cards is list containing
            52 Card refs, initially
        """

        self._cards = []

        for rank in range(1, 14):
            for suit in range(4):
                c = Card(rank, suit) # create next Card with given value
                self._cards.append(c) # add it to this Deck

    def __str__(self):

        """
        "Stringified" deck: string of Card named,
        with \n for easier reading
        """
        str_to_return = '' # accumulate each card's str() description, separated by '\n'

        # for index in range(len(self._cards)):
        #     self._cards[index]

        for c in self._cards:
            temp = str(c)  # temp is the stringified card
            str_to_return = str_to_return + temp + "\n"  # note \n at end

        return str_to_return

    def shuffle(self):
        random.shuffle(self._cards)  # note random function that does this

    def dealCard(self):
        to_return = self._cards.pop(0)  # get and remove top card from deck
        return to_return

def buildDict(hand):

    dict = {}

    for card in hand:
        dict[card._rank] = dict.get(card._rank, 0) + 1

    return dict


def hasOnePair(dict):

    # Check for EXACTLY one pair in dict and NO three-of-a-kind

    # Note there might be 2 pairs; hence the counting of pairs
    #
    # Or.. there might be three-of-a-kind plus a single pair:
    #   hence check for full house

    pair_count = 0
    three_count = 0
    for v in dict.values():
        if v == 2:
            pair_count += 1
        elif v == 3:
            three_count += 1

    if pair_count==1 and three_count != 1: # check for JUST one pair
        return True
    else:
        return False


def hasTwoPairs(dict):
    
    """
    Complete this!
    :param dict: dictionary with card ranks to check
    """

    return False  # fix this


def hasThreeOfAKind(dict):

    """
    Complete this!
    :param dict: dictionary with card ranks to check
    """

    return False


def hasFullHouse(dict):

    """
    Complete this!
    :param dict: dictionary with card ranks to check
    """

    return False


def hasFourOfAKind(dict):

    """
    Complete this!
    :param dict: dictionary with card ranks to check
    """

    return False


def hasStraight(dict):

    """
    Complete this!
    :param dict: dictionary with card ranks to check
    """

    return False


def hasFlush(dict):

    """
    Complete this!
    :param dict: dictionary with card ranks to check
    """

    return False


def hasStraightFlush(dict):

    """
    Complete this!
    :param dict: dictionary with card ranks to check
    """

    return False


def hasRoyalFlush(dict):

    """
    Complete this!
    :param dict: dictionary with card ranks to check
    """

    return False


def main():

    # finish this...

    TRIALS = 10000  # int(input ("Input number of hands to test: "))

    hand = []  # list of Card in hand

    # accumulators for different counts

    onepairCount = 0
    twopairCount = 0
    threeCount = 0
    fourCount = 0
    fullHouseCount = 0

    # more for Extra Credit: 0.25 per additional hand

    for num in range(TRIALS):

        d = Deck()
        d.shuffle()
        hand = []

        for count in range(5):
            hand.append(d.dealCard())

        dict = buildDict(hand)

        if hasOnePair(dict):
            onepairCount += 1

        elif hasTwoPairs(dict):
            twopairCount += 1

        elif hasThreeOfAKind(dict):
            threeCount += 1

        elif hasFourOfAKind(dict):
            fourCount += 1

        elif hasFullHouse(dict):
            fullHouseCount += 1

    # add EC code if you wish...

    # print out results...

    print("Number / %% of one pair hands is: %d / %.4f%%" \
          % (onepairCount, 100.0 * onepairCount / TRIALS))

    print("Number / %% of two pair hands is: %d / %.4f%%" \
          % (twopairCount, 100.0 * twopairCount / TRIALS))

    print("Number / %% of 3-of-a-kind hands is: %d / %.4f%%" \
          % (threeCount, 100.0 * threeCount / TRIALS))

    print("Number / %% of 4-of-a-kind hands is: %d / %.4f%%" \
          % (fourCount, 100.0 * fourCount / TRIALS))

    print("Number / %% of full house hands is: %d / %.4f%%" \
          % (fullHouseCount, 100.0 * fullHouseCount / TRIALS))

    # print out EC results if done

if __name__ == "__main__":
    pass
    # main()  # uncomment to run general poker odds calculations

# your Pytest tests should follow here...