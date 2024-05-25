from deck import Deck
from hand import DealerHand, PlayerHand
from card import Card

# don't change these imports
from numpy.random import randint, seed
seed(20)

class Blackjack:
    """
    Game of blackjack!

    # Removes the game summaries from the previous doctest run
    >>> from os import remove, listdir
    >>> for f in listdir("game_summaries"):
    ...    remove("game_summaries/" + f)

    #######################################
    ### Doctests for calculate_score() ####
    #######################################
    >>> card_1 = Card("A", "diamonds")
    >>> card_2 = Card("J", "spades")
    >>> hand_1 = PlayerHand()
    >>> Blackjack.calculate_score(hand_1)
    0
    >>> hand_1.add_card(card_1)
    >>> Blackjack.calculate_score(hand_1) # (Ace)
    11
    >>> hand_1.add_card(card_2)
    >>> Blackjack.calculate_score(hand_1) # (Ace, Jack)
    21

    >>> card_3 = Card("A", "spades")
    >>> hand_2 = PlayerHand()
    >>> hand_2.add_card(card_1, card_3)
    >>> Blackjack.calculate_score(hand_2) # (Ace, Ace)
    12
    >>> hand_2.add_card(card_2)
    >>> Blackjack.calculate_score(hand_2) # (Ace, Ace, Jack)
    12

    >>> hand_3 = PlayerHand()
    >>> card_4 = Card(2, "spades")
    >>> card_5 = Card(4, "spades")
    >>> hand_3.add_card(card_4, card_5)
    >>> Blackjack.calculate_score(hand_3)
    6

    #######################################
    ### Doctests for determine_winner() ####
    #######################################
    >>> blackjack = Blackjack(10)
    >>> blackjack.determine_winner(10, 12)
    -1
    >>> blackjack.determine_winner(21, 21)
    0
    >>> blackjack.determine_winner(22, 23)
    0
    >>> blackjack.determine_winner(12, 2)
    1
    >>> blackjack.determine_winner(22, 2)
    -1
    >>> blackjack.determine_winner(2, 22)
    1
    >>> print(blackjack.get_log())
    Player lost with a score of 10. Dealer won with a score of 12.
    Player and Dealer tie.
    Player and Dealer tie.
    Player won with a score of 12. Dealer lost with a score of 2.
    Player lost with a score of 22. Dealer won with a score of 2.
    Player won with a score of 2. Dealer lost with a score of 22.
    <BLANKLINE>  
    >>> blackjack.reset_log()

    #######################################
    ### Doctests for play_round() #########
    #######################################
    >>> blackjack_2 = Blackjack(10)
    >>> blackjack_2.play_round(1, 15)
    >>> print(blackjack_2.get_log())
    Round 1 of Blackjack!
    wallet: 10
    bet: 5
    Player Cards: (10, spades) (A, spades)
    Dealer Cards: (Q, spades) (?, ?)
    Dealer Cards Revealed: (7, hearts) (Q, spades)
    Player won with a score of 21. Dealer lost with a score of 17.
    <BLANKLINE>
    
    >>> blackjack_2.reset_log()
   
    >>> blackjack_2.play_round(3, 21)
    >>> print(blackjack_2.get_log())
    Round 2 of Blackjack!
    wallet: 15
    bet: 5
    Player Cards: (4, spades) (7, spades)
    Dealer Cards: (A, diamonds) (?, ?)
    (J, diamonds) was pulled by a Player
    Dealer Cards Revealed: (5, spades) (A, diamonds)
    (6, spades) was pulled by a Dealer
    (2, spades) was pulled by a Dealer
    (8, spades) was pulled by a Dealer
    Player won with a score of 21. Dealer lost with a score of 22.
    Round 3 of Blackjack!
    wallet: 20
    bet: 10
    Player Cards: (6, diamonds) (9, hearts)
    Dealer Cards: (K, diamonds) (?, ?)
    (Q, diamonds) was pulled by a Player
    Dealer Cards Revealed: (J, hearts) (K, diamonds)
    Player lost with a score of 25. Dealer won with a score of 20.
    Round 4 of Blackjack!
    wallet: 10
    bet: 5
    Player Cards: (5, hearts) (10, hearts)
    Dealer Cards: (2, hearts) (?, ?)
    (3, hearts) was pulled by a Player
    (7, clubs) was pulled by a Player
    Dealer Cards Revealed: (2, hearts) (2, diamonds)
    (K, clubs) was pulled by a Dealer
    (3, clubs) was pulled by a Dealer
    Player lost with a score of 25. Dealer won with a score of 17.
    <BLANKLINE>
    
    >>> with open("game_summaries/game_summary2.txt", encoding = 'utf-8') as f:
    ...     lines = f.readlines()
    ...     print("".join(lines[10:26]))
    Dealer Hand:
    ____
    |7  |
    | ♥ |
    |__7|
    ____
    |Q  |
    | ♠ |
    |__Q|
    Winner of ROUND 1: Player
    <BLANKLINE>
    ROUND 2:
    Player Hand:
    ____
    |4  |
    | ♠ |
    <BLANKLINE>

    >>> blackjack_3 = Blackjack(5)
    >>> blackjack_3.play_round(5, 21)
    >>> print(blackjack_3.get_log())
    Round 1 of Blackjack!
    wallet: 5
    bet: 5
    Player Cards: (2, spades) (2, diamonds)
    Dealer Cards: (2, hearts) (?, ?)
    (3, spades) was pulled by a Player
    (3, hearts) was pulled by a Player
    (3, diamonds) was pulled by a Player
    (3, clubs) was pulled by a Player
    (4, spades) was pulled by a Player
    (4, hearts) was pulled by a Player
    Dealer Cards Revealed: (2, hearts) (2, clubs)
    (4, diamonds) was pulled by a Dealer
    (4, clubs) was pulled by a Dealer
    (5, spades) was pulled by a Dealer
    Player lost with a score of 24. Dealer won with a score of 17.
    Wallet amount $0 is less than bet amount $5.

    >>> blackjack_4 = Blackjack(500)
    >>> blackjack_4.play_round(13, 21) # At least 52 cards will be dealt
    >>> blackjack_4.reset_log()
    >>> blackjack_4.play_round(1, 17)
    >>> print(blackjack_4.get_log())
    Not enough cards for a game.
    """
    # Class Attribute(s)

    game_num = 0

    def __init__(self, wallet):
        # Initialize instance attributes
        # auto-increment as needed
        self.deck = Deck()
        self.wallet = wallet
        Blackjack.game_num = Blackjack.game_num + 1
        self.game_number = Blackjack.game_num
        self.log = ''
        self.bet = 5
        self.round_played = 0
    
    def play_round(self, num_rounds, stand_threshold):
        """
        Plays `num_rounds` Blackjack rounds.

        Parameters:
            num_rounds (int): Number of rounds to play.
            stand_threshold (int): Score threshold for when the player
            will stand (ie player stands if they have a score >= 
            this threshold)
        """
        # This could get pretty long!
        assert type(num_rounds) == int and num_rounds > 0
        assert type(stand_threshold) == int and stand_threshold > 1
        min_bet = 5
        self.bet = min_bet
        for i in range(num_rounds):
            card_lst = self.deck.cards
            deck = self.deck
            min_num = 4
            bet = self.bet
            wallet = self.wallet
            if len(card_lst) < min_num:
                text = 'Not enough cards for a game.'
                self.log = self.log + text
                return
            if wallet < bet:
                text = 'Wallet amount $' + str(wallet) + ' is less than bet amount $'\
                + str(bet) + '.'
                self.log = self.log + text
                return
            self.round_played = self.round_played + 1
            num_mongean = randint(0, 5)
            num_modified = randint(0, 5)
            deck.shuffle(modified_overhand=num_modified, mongean=num_mongean)
            player_hand = PlayerHand()
            dealer_hand = DealerHand()
            n = 2
            for j in range(n):
                deck.deal_hand(player_hand)
                deck.deal_hand(dealer_hand)
            text = 'Round ' + str(self.round_played) + ' of Blackjack!\n'
            self.log = self.log + text
            text = 'wallet: ' + str(wallet) + '\n'
            self.log = self.log + text
            text = 'bet: ' + str(bet) + '\n'
            self.log = self.log + text
            text = 'Player Cards: ' + player_hand.__repr__() + '\n'
            self.log = self.log + text
            text = 'Dealer Cards: ' + dealer_hand.__repr__() + '\n'
            self.log = self.log + text
            self.hit_or_stand(player_hand, stand_threshold)
            dealer_hand.reveal_hand()
            text = 'Dealer Cards Revealed: ' + dealer_hand.__repr__() + '\n'
            self.log = self.log + text
            dealer_threshold = 17
            self.hit_or_stand(dealer_hand, dealer_threshold)
            player_score = Blackjack.calculate_score(player_hand)
            dealer_score = Blackjack.calculate_score(dealer_hand)
            result = self.determine_winner(player_score, dealer_score)
            if result == 1:
                wallet = wallet + bet
                bet = bet + min_bet
            if result == -1:
                wallet = wallet - bet
                if bet > min_bet:
                    bet = bet - min_bet
            self.wallet = wallet
            self.bet = bet
            self.add_to_file(player_hand, dealer_hand, result)

            
    def calculate_score(hand):
        """
        Calculates the score of a given hand. 

        Sums up the ranks of each card in a hand. Jacks, Queens, and Kings
        have a value of 10 and Aces have a value of 1 or 11. The value of each
        Ace card is dependent on which value would bring the score closer
        (but not over) 21. 

        Should be solved using list comprehension and map/filter. No explicit
        for loops.

        Parameters:
            hand: The hand to calculate the score of.
        Returns:
            The best score as an integer value.
        """
        assert type(hand) == PlayerHand or type(hand) == DealerHand
        max_value = 21
        half_value = 11
        ace_value = 10
        card_lst = hand.cards
        num_lst = [i.rank for i in card_lst]
        num_lst = list(map(lambda x: ace_value if x == 'J' or x == 'Q' or x == 'K' else x, num_lst))
        ace_lst = list(filter(lambda x: x == 'A', num_lst))
        num_lst = list(filter(lambda x: x != 'A', num_lst))
        total_1 = sum(num_lst)
        if total_1 >= max_value:
            total_2 = len(ace_lst)
        else:
            if total_1 >= half_value:
                total_2 = len(ace_lst)
            else:
                if len(ace_lst) >= 1:
                    if total_1 + half_value + len(ace_lst) -1 > max_value:
                        total_2 = len(ace_lst)
                    else:
                        total_2 = half_value + len(ace_lst) - 1
                else:
                    total_2 = 0
        total = total_1 + total_2
        return total

    def determine_winner(self, player_score, dealer_score):
        """
        Determine whether the Blackjack round ended with a tie, dealer winning, 
        or player winning. Update the log to include the winner and
        their scores before returning.

        Returns:
            1 if the player won, 0 if it is a tie, and -1 if the dealer won
        """
        max_value = 21
        if player_score > max_value and dealer_score > max_value:
            result = 0
        if player_score > max_value and dealer_score <= max_value:
            result = -1
        if player_score <= max_value and dealer_score <= max_value:
            if player_score < dealer_score:
                result = -1
            if player_score == dealer_score:
                result = 0
            if player_score > dealer_score:
                result = 1
        if player_score <= max_value and dealer_score > max_value:
            result = 1
        if result == 1:
            text = 'Player won with a score of ' + str(player_score) +\
            '. Dealer lost with a score of ' + str(dealer_score) + '.\n'
        if result == -1:
            text = 'Player lost with a score of ' + str(player_score) +\
            '. Dealer won with a score of ' + str(dealer_score) + '.\n'
        if result == 0:
            text = 'Player and Dealer tie.\n'
        self.log = self.log + text
        return result

    def hit_or_stand(self, hand, stand_threshold):
        """
        Deals cards to hand until the hand score has reached or surpassed
        the `stand_threshold`. Updates the log everytime a card is pulled.

        Parameters:
            hand: The hand the deal the cards to depending on its score.
            stand_threshold: Score threshold for when the player
            will stand (ie player stands if they have a score >= 
            this threshold).
        """
        while 1:
            score = Blackjack.calculate_score(hand)
            deck = self.deck
            card_lst = deck.cards
            if score >= stand_threshold:
                return
            if len(card_lst) == 0:
                return
            top = card_lst[0]
            deck.deal_hand(hand)
            if type(hand) == PlayerHand:
                text = top.__repr__() + ' was pulled by a Player\n'
            if type(hand) == DealerHand:
                text = top.__repr__() + ' was pulled by a Dealer\n'
            self.log = self.log + text
            self.deck = deck

    def get_log(self):
        return self.log
    
    def reset_log(self):
        self.log = ''
        
        
    def add_to_file(self, player_hand, dealer_hand, result):
        """
        Writes the summary and outcome of a round of Blackjack to the 
        corresponding .txt file. This file should be named game_summaryX.txt 
        where X is the game number and it should be in `game_summaries` 
        directory.
        """
        
        # Remember to use encoding = "utf-8" 
        filename = 'game_summaries/game_summary' + str(self.game_number) + '.txt'
        file = open(filename, 'a', encoding = 'utf-8')
        file_read = open(filename, 'r', encoding = 'utf-8')
        l = file_read.readlines()
        if len(l) == 0:
            text = ''
        else:
            text = '\n'
        file_read.close()
        text = text + 'ROUND ' + str(self.round_played) + ':\n'
        text = text + 'Player Hand:\n'
        text = text + player_hand.__str__() + '\n'
        text = text + 'Dealer Hand:\n'
        text = text + dealer_hand.__str__() + '\n'
        if result == 1:
            winner = 'Player'
        if result == -1:
            winner = 'Dealer'
        if result == 0:
            winner = 'Tied'
        text = text + 'Winner of ROUND ' + str(self.round_played) + ': ' + winner + '\n'
        file.write(text)
        file.close()
