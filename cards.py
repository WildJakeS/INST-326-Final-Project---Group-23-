"""
Blackjack Game

This Python program implements a simple text-based Blackjack game. 
Players compete against the dealer by trying to get their hand's value 
as close to 21 as possible without exceeding it. Aces can be counted 
as 1 or 11 based on the total hand value.

Features:
- *

Usage:
- *

Future Enhancements:
- *

Author: Jake Sheehi, Jaylen Williams, Johnathan Cook, Ugo Onyejiaka
Course: INST-326-0301
Group: Group 23
Date: November 22, 2024
Version: 0.1

"""

import random

#Constant variables
CARD_VALUES = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
    "J": 10, "Q": 10, "K": 10, "A": 11 #to add more, unique cards later
}
SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]

# Helper Functions
def create_deck():
    """Creates a standard 52-card deck with 13 ranks across 4 suits.

    @return: A list representing the deck of cards."""
    return [f"{value} of {suit}" for value in CARD_VALUES.keys() for suit in SUITS]

def calculate_score(hand):
    """Calculates the total score of a hand in Blackjack.

    - Aces count as 11, but are reduced to 1 if the total score exceeds 21.
    
    @param hand: A list of strings representing the player's or dealer's hand.
    @return: An integer representing the calculated score of the hand."""
    score = 0
    aces = 0
    for card in hand:
        value = card.split(" ")[0]
        score += CARD_VALUES[value]
        if value == "A":
            aces += 1
    
    # Adjusts for Aces if score > 21 (to be changed / dynamic)
    while score > 21 and aces:
        score -= 10
        aces -= 1
    return score

def deal_card(deck):
    """Deals a single random card from the deck.

    @param deck: A list of strings representing the current deck of cards.
    @return: A string representing the dealt card."""

    return deck.pop(random.randint(0, len(deck) - 1))



def blackjack():
    """Runs the main Blackjack game loop.

    - Initializes the deck, shuffles it, and deals cards to the player and dealer.
    - Handles user actions ('hit' or 'stand').
    - Determines the winner based on Blackjack rules.
    
    @return: None"""

    print("Welcome to Blackjack!")
    
    # Initialize Deck and Shuffle
    deck = create_deck()
    random.shuffle(deck)
    
    # Player and Dealer Hands
    player_hand = [deal_card(deck), deal_card(deck)]
    dealer_hand = [deal_card(deck), deal_card(deck)]
    
    # Gameloop
    while True:
        # Displays Hands
        print("\nYour Hand:", player_hand, "-> Score:", calculate_score(player_hand))
        print("Dealer's Hand: [", dealer_hand[0], ", ??? ]")
        
        # Player's turn
        action = input("Do you want to 'hit' or 'stand'? ").lower()
        if action == "hit":
            player_hand.append(deal_card(deck))
            if calculate_score(player_hand) > 21:
                print("\nYour Hand:", player_hand, "-> Score:", calculate_score(player_hand))
                print("You busted! Dealer wins.")
                break
        elif action == "stand":
            break
        else:
            print("Invalid input! Please type 'hit' or 'stand'.")
    
    # Dealer's Turn
    if calculate_score(player_hand) <= 21:
        print("\nDealer's Turn...")
        while calculate_score(dealer_hand) < 17:
            dealer_hand.append(deal_card(deck))
        print("Dealer's Hand:", dealer_hand, "-> Score:", calculate_score(dealer_hand))
        
        # Choose winner
        player_score = calculate_score(player_hand)
        dealer_score = calculate_score(dealer_hand)
        if dealer_score > 21 or player_score > dealer_score:
            print("You win!")
        elif player_score < dealer_score:
            print("Dealer wins!")
        else:
            print("It's a tie!")

if __name__ == "__main__":
    """Entry point of the program. Starts the Blackjack game."""

    blackjack()
