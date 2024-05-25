from card import Card
from hand import PlayerHand, DealerHand
from shuffle import Shuffle

class Deck:
    """
    Card deck of 52 cards.

    >>> deck = Deck()
    >>> deck.get_cards()[:5]
    [(2, spades), (2, hearts), (2, diamonds), (2, clubs), (3, spades)]

    >>> deck.shuffle(modified_overhand=2, mongean=3)
    >>> deck.get_cards()[:5]
    [(A, spades), (Q, spades), (10, spades), (7, hearts), (5, hearts)]

    >>> deck2 = Deck()
    >>> deck2.shuffle(mongean=3, modified_overhand=2)
    >>> deck2.get_cards()[:5]
    [(A, spades), (Q, spades), (10, spades), (7, hearts), (5, hearts)]

    >>> hand = PlayerHand()
    >>> deck.deal_hand(hand)
    >>> deck.get_cards()[0]
    (Q, spades)
    >>> hand
    (A, spades)
    """

    # Class Attribute(s)

    def __init__(self):
        """
        Creates a Deck instance containing cards sorted in ascending order.
        """
        rank_lst = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
        suit_lst = ['spades', 'hearts', 'diamonds', 'clubs']
        card_lst = [Card(i, j) for i in rank_lst for j in suit_lst]
        self.cards = card_lst

    def shuffle(self, **shuffle_and_count):
        """Shuffles the deck using a variety of different shuffles.

        Parameters:
            shuffle_and_count: keyword arguments containing the
            shuffle type and the number of times the shuffled
            should be called.
        """
        shuffle_lst = list(shuffle_and_count.items())
        new_lst = []
        for i in shuffle_lst:
            if i[0] == 'modified_overhand':
                new_lst.append(i)
        for i in shuffle_lst:
            if i[0] == 'mongean':
                new_lst.append(i)
        for i in new_lst:
            shuffle_type = i[0]
            num = i[1]
            if shuffle_type == 'modified_overhand':
                new_card_lst = Shuffle.modified_overhand(self.cards, num)
                self.cards = new_card_lst
            if shuffle_type == 'mongean':
                for j in range(num):
                    new_card_lst = Shuffle.mongean(self.cards)
                    self.cards = new_card_lst

    def deal_hand(self, hand):
        """
        Takes the first card from the deck and adds it to `hand`.
        """
        assert type(hand) == PlayerHand or type(hand) == DealerHand
        card_lst = self.cards
        card = card_lst[0]
        new_card_lst = card_lst[1:]
        hand.add_card(card)
        self.cards = new_card_lst

    def get_cards(self):
        return self.cards
