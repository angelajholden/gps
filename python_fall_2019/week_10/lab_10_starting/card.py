"""
Card represents a single standard playing card,
with two int attributes:
  _rank from 1 (Ace) to 13 (King),
  _suit from 0 (Clubs) to 3 (Spades)

"""

#
# out_riffle.py:
#
# 	Starting code for L10-1
#

SUITS = ["Clubs", "Diamonds", "Hearts", "Spades"]
RANKS = ["", "Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]


class Card():
    """
    Represents a single playing card,
        whose rank is the int attribute _rank: 1..13 => "Ace".."King"
        and whose suit is the int attribute _suit 0..3 => "Clubs".."Spades"
    """

    def __init__(self, rank=1, suit=3):
        '''
        Initialize card with given int suit 0..3 and int rank 1..13
        '''
        self._rank = rank
        self._suit = suit


    def __str__(self):
        '''
        Return the string name of this card:
        "Ace of Spades":
        Note the use of lists RANKS and SUITS with indexing into these
        translating the int fields to descriptive strings
        '''

        # "Ace of Spades" is string for self._rank==1, self._suit==3

        toreturn = RANKS[self._rank] + " of " + SUITS[self._suit]

        return toreturn


def main():
    """
    Create several Cards and print
    Also demonstrate adding new field dynamically...
    """

    card1 = Card(1, 3)  # Ace of Spades

    print(card1)
    print(str(card1))  # equivalent to above
    print(card1.__str__())  # long-winded form

    card2 = Card(12, 2)  # Queen of Hearts

    print(str(card2))

    card1._newfield = 47
    print(card1._newfield)


if __name__ == "__main__":
    main()
