#Dominic Santistevan
#12/6/18
#Deck of Cards
import random

deck = []
player1Hand = []
player2Hand = []

def makedeck(deck):
    """ Populate the deck of cards """
    SUITS = ["hearts","diamonds","clubs","spades"]
    VALUES = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    for e in SUITS:
        for i in VALUES:
            card = i+" "+e
            deck.append(card)

def shuffledeck(deck):
    for i in range(len(deck))
    j = random.randrange(len(deck))
    temp = deck[i]
    deck[i] = deck[j]
    deck[j] = temp

def dealcard(deck,player1Hand,player2Hand):
    for i in range(5):
        card = deck.pop()
        player2Hand.append(card)
        card = deck.pop()
        player1Hand.append(card)

    makedeck(deck)
    print(len(deck))
    print(deck)

    print()
    print()
    print()
    shuffledeck(deck)
    print(deck)

    dealcard(deck,player1Hand,player2Hand)

    print()
    print(player1Hand)
    print(player2Hand)

    
makedeck()
print(len(deck))
print(deck)

