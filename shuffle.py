class Shuffle:
    """
    Different kinds of shuffling techniques.
    
    >>> cards = [i for i in range(52)]
    >>> cards[25]
    25
    >>> mod_oh = Shuffle.modified_overhand(cards, 1)
    >>> mod_oh[0]
    25
    >>> mod_oh[25] 
    24
 
    >>> mongean_shuffle = Shuffle.mongean(mod_oh)
    >>> mongean_shuffle[0]
    51
    >>> mongean_shuffle[26]
    25
    
    >>> odd_cards = [1, 2, 3, 4, 5]
    >>> mod_oh_even = Shuffle.modified_overhand(odd_cards, 2)
    >>> mod_oh_even
    [1, 2, 3, 4, 5]
    """     
        
    def modified_overhand(cards, num):
        """
        Takes `num` cards from the middle of the deck and puts them at the
        top. 
        Then decrement `num` by 1 and continue the process till `num` = 0. 
        When num is odd, the "extra" card is taken from the bottom of the
        top half of the deck.
        """
        
        # Use Recursion.
        # Note that the top of the deck is the card at index 0.
        assert type(cards) == list
        assert type(num) == int
        assert num <= len(cards)
        assert num >= 0
        length = len(cards)
        if num == 0:
            return cards
        else:
            if length % 2 == 1 and num % 2 == 1:
                start = int(length / 2 - num / 2)
                end = int(length / 2 + num / 2)
            if length % 2 == 0 and num % 2 == 0:
                start = int(length / 2 - num / 2)
                end = int(length / 2 + num / 2)
            if length % 2 == 1 and num % 2 == 0:
                start = int(length / 2 - num / 2 - 0.5)
                end = int(length / 2 + num / 2 - 0.5)
            if length % 2 == 0 and num % 2 == 1:
                start = int(length / 2 - num / 2 - 0.5)
                end = int(length / 2 + num / 2 - 0.5)
            shuffled_cards = cards[start: end]
            new_cards = shuffled_cards + cards[0: start] + cards[end: ]
            return Shuffle.modified_overhand(new_cards, num - 1)
                    

    def mongean(cards):
        """
        Implements the mongean shuffle. 
        Check wikipedia for technique description. Doing it 12 times restores the deck.
        """
        
        # Remember that the "top" of the deck is the first item in the list.
        # Use Recursion. Can use helper functions.
        
        length = len(cards)
        if length == 0:
            return []
        elif length == 1:
            return cards
        else:
            if length % 2 == 0:
                top = [cards[-1]]
                bottom = [cards[-2]]
                return top + Shuffle.mongean(cards[0: -2]) + bottom
            else:
                top = [cards[-2]]
                bottom = [cards[-1]]
                return top + Shuffle.mongean(cards[0: -2]) + bottom
