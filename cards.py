"""
Blackjack Game

This Python program implements a simple text-based Blackjack game. 
Players compete against the dealer by trying to get their hand's value 
as close to 21 as possible without exceeding it. Aces can be counted 
as 1 or 11 based on the total hand value.

Features:
- Game can be replayed for multiple rounds
- Jokers double the hand's score when drawn
- Multiplayer support added
- Personalized player names

Usage:
Running the code will start the game; users must follow and decide to either hit or stand. 
The game will automatically handle the dealer's actions and decide the winner.

Author: Jake Sheehi, Jaylen Williams, Johnathan Cook, Ugo Onyejiaka
Course: INST-326-0301
Group: Group 23
Date: November 22, 2024
Version: 0.2

"""

import random

# Constant variables
CARD_VALUES = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
    "J": 10, "Q": 10, "K": 10, "A": 11, "Joker": 0  # Joker added
}
SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]

# Helper Functions
def create_deck():
    """Creates a standard 52-card deck plus 2 Jokers."""
    deck = [f"{value} of {suit}" for value in CARD_VALUES.keys() if value != "Joker" for suit in SUITS]
    deck.extend(["Joker", "Joker"])  # Add two Jokers to the deck
    return deck

def calculate_score(hand):
    """Calculates the total score of a hand in Blackjack.

    - Aces count as 11, but are reduced to 1 if the total score exceeds 21.
    - Jokers double the score of the hand.

    @param hand: A list of strings representing the player's or dealer's hand.
    @return: An integer representing the calculated score of the hand.
    """
    score = 0
    aces = 0
    jokers = 0
    for card in hand:
        value = card.split(" ")[0]
        if value == "Joker":
            jokers += 1
        else:
            score += CARD_VALUES[value]
            if value == "A":
                aces += 1

    # Adjust for Aces if score > 21
    while score > 21 and aces:
        score -= 10
        aces -= 1

    # Apply Joker doubling effect
    score *= (2 ** jokers)
    return score

def deal_card(deck):
    """Deals a single random card from the deck.

    @param deck: A list of strings representing the current deck of cards.
    @return: A string representing the dealt card.
    """
    return deck.pop(random.randint(0, len(deck) - 1))

def blackjack():
    """Runs the main Blackjack game loop."""
    print("Welcome to Blackjack!")

    # Prompt for number of players
    num_players = int(input("Enter the number of players: "))
    players = []
    for i in range(num_players):
        player_name = input(f"Enter Player {i + 1}'s name: ")
        players.append({"name": player_name, "hand": []})

    while True:
        # Initialize Deck and Shuffle
        deck = create_deck()
        random.shuffle(deck)

        # Deal cards to players
        for player in players:
            player["hand"] = [deal_card(deck), deal_card(deck)]

        # Dealer's Hand
        dealer_hand = [deal_card(deck), deal_card(deck)]

        # Players' Turns
        for player in players:
            print(f"\n{player['name']}'s Turn:")
            while True:
                print(f"{player['name']}'s Hand:", player["hand"], "-> Score:", calculate_score(player["hand"]))
                action = input("Do you want to 'hit' or 'stand'? ").lower()
                if action == "hit":
                    player["hand"].append(deal_card(deck))
                    if calculate_score(player["hand"]) > 21:
                        print(f"{player['name']} busted!")
                        break
                elif action == "stand":
                    break
                else:
                    print("Invalid input! Please type 'hit' or 'stand'.")

        # Dealer's Turn
        print("\nDealer's Turn...")
        while calculate_score(dealer_hand) < 17:
            dealer_hand.append(deal_card(deck))
        print("Dealer's Hand:", dealer_hand, "-> Score:", calculate_score(dealer_hand))

        # Determine Winners
        for player in players:
            player_score = calculate_score(player["hand"])
            dealer_score = calculate_score(dealer_hand)
            if dealer_score > 21 or player_score > dealer_score:
                print(f"{player['name']} wins!")
            elif player_score < dealer_score:
                print(f"{player['name']} loses!")
            else:
                print(f"{player['name']} ties with the dealer!")

        # Play Again
        play_again = input("Would you like to play again? (y/n) ").lower()
        if play_again == "n":
            break

if __name__ == "__main__":
    blackjack()
