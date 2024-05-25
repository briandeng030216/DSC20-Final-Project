class Card:
    """
    Card class.

    # Doctests for str and repr
    >>> card_1 = Card("A", "spades")
    >>> print(card_1)
    ____
    |A  |
    | ♠ |
    |__A|
    >>> card_1
    (A, spades)
    >>> card_2 = Card("K", "spades")
    >>> print(card_2)
    ____
    |K  |
    | ♠ |
    |__K|
    >>> card_2
    (K, spades)
    >>> card_3 = Card("A", "diamonds")
    >>> print(card_3)
    ____
    |A  |
    | ♦ |
    |__A|
    >>> card_3
    (A, diamonds)

    # Doctests for comparisons
    >>> card_1 < card_2
    False
    >>> card_1 > card_2
    True
    >>> card_3 > card_1
    True

    # Doctests for set_visible()
    >>> card_3.set_visible(False)
    >>> print(card_3)
    ____
    |?  |
    | ? |
    |__?|
    >>> card_3
    (?, ?)
    >>> card_3.set_visible(True)
    >>> print(card_3)
    ____
    |A  |
    | ♦ |
    |__A|
    >>> card_3
    (A, diamonds)
    """

    # Class Attribute(s)

    def __init__(self, rank, suit, visible=True):
        """
        Creates a card instance and asserts that the rank and suit are valid.
        """
        rank_lst = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
        suit_lst = ['spades', 'hearts', 'diamonds', 'clubs']
        assert rank in rank_lst
        assert suit in suit_lst
        self.rank = rank
        self.suit = suit
        self.visible = visible
        x = rank
        c = suit
        if rank == 'J':
            x = 11
        if rank == 'Q':
            x = 12
        if rank == 'K':
            x = 13
        if rank == 'A':
            x = 14
        if suit == 'hearts':
            c = '♥'
        if suit == 'spades':
            c = '♠'
        if suit == 'clubs':
            c = '♣'
        if suit == 'diamonds':
            c = '♦'
        self.x = x
        self.c = c

    def __lt__(self, other_card):
        rank1 = self.x
        rank2 = other_card.x
        suit1 = self.suit
        suit2 = other_card.suit
        if suit1 == 'spades':
            suit1 = 1
        if suit1 == 'hearts':
            suit1 = 2
        if suit1 == 'diamonds':
            suit1 = 3
        if suit1 == 'clubs':
            suit1 = 4
        if suit2 == 'spades':
            suit2 = 1
        if suit2 == 'hearts':
            suit2 = 2
        if suit2 == 'diamonds':
            suit2 = 3
        if suit2 == 'clubs':
            suit2 = 4
        if rank1 < rank2:
            return True
        if rank1 > rank2:
            return False
        if rank1 == rank2:
            if suit1 < suit2:
                return True
            if suit1 > suit2:
                return False


    def __str__(self):
        """
        Returns ASCII art of a card with the rank and suit. If the card is
        hidden, question marks are put in place of the actual rank and suit.

        Examples:
        ____
        |A  |
        | ♠ |
        |__A|
        ____
        |?  |
        | ? |
        |__?|             
        """
        if self.visible == True:
            rank = str(self.rank)
            suit = self.c
        if self.visible == False:
            rank = '?'
            suit = '?'
        text1 = '____\n'
        text2 = '|' + rank +'  |\n'
        text3 = '| ' + suit + ' |\n'
        text4 = '|__' + rank + '|'
        text = text1 + text2 + text3 + text4
        return text

    def __repr__(self):
        """
        Returns (<rank>, <suit>). If the card is hidden, question marks are
        put in place of the actual rank and suit.           
        """        
        if self.visible == True:
            return '(' + str(self.rank) + ', ' + self.suit + ')'
        else:
            return '(?, ?)'

    def get_rank(self):
        return self.rank
    
    def get_suit(self):
        return self.suit

    def set_visible(self, visible):
        assert type(visible) == bool
        self.visible = visible