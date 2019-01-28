"""

BlackJack Game
"""

import random

SUITS = ('Hearts', 'Diamonds', 'Spades', 'Clubs')

RANKS = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine',
         'Ten', 'Jack', 'Queen', 'King', 'Ace')

VALUES = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7,
          'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

PLAYING = True

class Card:
    """Class card"""

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}."

# Test Card class:
# card_test = Card('Hearts', 'Two')
# print(card_test)

class Deck:
    """Class Deck"""

    def __init__(self):
        self.deck = []
        for suit in SUITS:
            for rank in RANKS:
                self.deck.append((suit,rank))

    def __str__(self):
        return f"Deck: {self.deck}. TOTAL Cards: {len(self.deck)}."

    def shuffle(self):

        random.shuffle(self.deck)

    def deal(self):

        suit, rank = self.deck.pop()
        return Card(suit, rank)

# Test shuffle and deal functions:
# deck_test = Deck()
# print(deck_test)
# deck_test.shuffle()
# print(deck_test)
# card_dealed = deck_test.deal()
# print("Card dealed is:", card_dealed)
# print(deck_test)

class Hand:
    """Class Hand"""

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def __str__(self):
        return 'Hand cards: ' + " ".join([str(card) for card in self.cards]) + f' Total value = {self.value}.'

    def add_card(self, card):

        self.cards.append(card)

        if card.rank == 'Ace':
            self.aces += 1

        self.value += VALUES.get(card.rank,0)

        # self.adjust_for_ace()

    def adjust_for_ace(self):

        while self.aces > 0 and self.value > 21:
            self.value -= 10
            self.aces -= 1

# Test add_card function without adjust_for_ace:
# deck_test = Deck()
# print(deck_test)
# deck_test.shuffle()
# print(deck_test)
# card_dealed = deck_test.deal()
# print("Card dealed is:", card_dealed)
# print(deck_test)
# hand_test = Hand()
# print(hand_test)
# hand_test.add_card(card_dealed)
# print(hand_test)
# card_dealed2 = deck_test.deal()
# print("Card dealed is:", card_dealed2)
# hand_test.add_card(card_dealed2)
# print(hand_test)

# Test add_card function with adjust_for_ace:
# hand_test = Hand()
# print(hand_test)
# hand_test.add_card(Card('Hearts', 'Ace'))
# print(hand_test)
# hand_test.add_card(Card('Diamonds', 'Ace'))
# print(hand_test)
# hand_test.add_card(Card('Diamonds', 'King'))
# print(hand_test)
# hand_test.add_card(Card('Spades', 'Ace'))
# print(hand_test)

class Chips:
    """Chip Class"""

    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self, bet):

        self.total += bet

    def lose_bet(self, bet):

        self.total -= bet

class Player:
    """Player class"""

        def __init__(self):
            self.hand = Hand()
            self.chips = Chips()

def take_bet():
    """take a bet"""

    while True:
        try:
            bet = int(input("Take a bet: "))
            return bet
        except:
            print('You need a number. Please try again! \n')
        else:
            break

# Test take_bet function:
take_bet()

def hit(deck,hand):
    """Hit function"""

    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def hit_or_stand(deck, hand):
    """"""

    global playing

    if not hit(deck, hand):
        playing = False

def show_some(player, dealer):
    """Show the cards hand of the player and the cards hand of the dealer except 1"""

    print(" ".join([str(card) for card in dealer.hand.cards[1:]]))
    print(" ".join([str(card) for card in player.hand.cards))

def show_all(player, dealer):
    """Show the cards hand of the dealer and the player, also show their total values."""

    print('Hand cards: ' + " ".join([str(card) for card in dealer.hand.cards]) + f' Total value = {dealer.hand.value}.')
    print('Hand cards: ' + " ".join([str(card) for card in player.hand.cards]) + f' Total value = {player.hand.value}.')


def player_busts():
    pass

def player_wins():
    pass

def dealer_busts():
    pass

def dealer_wins():
    pass

def push():
    pass
