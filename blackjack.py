import random

import os


def clear():
    os.system('cls')

# location for global variables


suits = ['Hearts', 'Spades', 'Clubs', 'Diamonds']

ranks = ['2', '3', '4', '5', '6', '7', '8',
         '9', '10', 'Jack', 'Queen', 'King', 'Ace']

values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
          '8': 8, '9': 9, '10': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11, }

game = True

player_turn = True

####################


class Card():
    """ create an object that will be a card """

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{self.rank} of {self.suit}'


# D4 = Card('Diamonds', '4')
# # D4.__str__()


class Deck():
    """
    create 52 cards 1 of each rank for each suit
    1 of hearts, 1 of spades, 1 of clubs, 1 of diamonds, 2 of hearts, etc....
    """

    def __init__(self):
        self.deck = [Card(suit, rank) for suit in suits for rank in ranks]

    def __str__(self):
        fulldeck = [eachcard.__str__() for eachcard in self.deck]
        return f'The cards in this deck are: {fulldeck}'

    def shuffledeck(self):
        """
        shuffleing of the deck
        """
        random.shuffle(self.deck)

    def dealcard(self):
        onecard = self.deck.pop()
        return onecard


# testdeck = Deck()
# testdeck.shuffledeck()
# # print(testdeck)
# print(testdeck.dealcard())


class Hand():
    """
    cards assinged/handed out to a hand
    """

    def __init__(self):
        self.cards = []
        self.points = 0
        self.ace = 0

    def addToHand(self, card):
        self.cards.append(card)
        self.points += values[card.rank]

        if card.rank == 'Ace':
            self.ace += 1

    def removeAces(self):
        if self.points > 21 and self.ace > 0:
            self.points -= 10
            self.ace -= 1


# player1 = Hand()
# player1.addToHand(testdeck.dealcard())

# dealer = Hand()
# dealer.addToHand(testdeck.dealcard())


def showPartial(player, dealer):
    print('Player Cards:')
    for card in player.cards:
        print(card)
    print(f'player points: {player.points}')

    print('\nDealer Cards:')
    print(dealer.cards[1])
    print('Card Hidden')
    print(f'Dealer points: ??')


def showAll(player, dealer):
    print('Player cards:')
    for card in player.cards:
        print(card)
    print(f'player points: {player.points}')

    print('\nDealer Cards:')
    for card in dealer.cards:
        print(card)
    print(f'Dealer points: {dealer.points}')


# print(f'\n first card:')
# showCards(player1)
# print('\n')


def hit(deck, hand):
    card = deck.dealcard()
    hand.addToHand(card)
    if hand.points > 21:
        hand.removeAces()


# hit(testdeck, player1)
# showCards(player1)


def hit_or_stand(deck, hand):
    """
        player_turn set to True
        continue asking to hit or stand until player decides to setand
        player turn then will become false
    """
    global player_turn
    ask = input('\nWould you like to hit or stand? : ').lower()

    if ask[0] == 'h':
        hit(deck, hand)
    elif ask != 'hit':
        print("Dealer's turn.")
        player_turn = False
# hit_or_stand(testdeck, player1)

# showCards(player1)


def winScenarios(player, dealer):
    if player.points > dealer.points:
        print('\nPlayer wins!')
    elif player.points < dealer.points and dealer.points <= 21:
        print('\nDealer wins!')
    elif dealer.points > 21:
        print('\nDealer busts!')
        print('Player Wins')
    elif dealer.points == player.points:
        print('\nDealer Wins!')

#####################################################################


while game:

    # start by initializing a deck
    deck = Deck()
    deck.shuffledeck()

    # create the player's hand and the dealer's hand
    player = Hand()

    dealer = Hand()

    # alternate adding 2 cards to each hand
    player.addToHand(deck.dealcard())
    dealer.addToHand(deck.dealcard())
    player.addToHand(deck.dealcard())
    dealer.addToHand(deck.dealcard())

    showPartial(player, dealer)

    while player_turn:

        hit_or_stand(deck, player,)
        clear()

        showPartial(player, dealer)

        # if over 21 bust
        if player.points > 21:
            clear()
            print('\nPlayer Busts!')
            player_turn = False

    if player.points <= 21:
        clear()

        while dealer.points < 17:
            dealer.addToHand(deck.dealcard())

        showAll(player, dealer)

        # win scenarios
        winScenarios(player, dealer)

    ask = input('\nWould you like to play again? ').lower()

    if ask[0] == 'y':
        clear()
        print('Good luck\n')
        player_turn = True
        continue
    elif ask == 'no':
        clear()
        print('Thank you for playing!')
        game = False
    else:
        print('Sorry, I do not understand')
