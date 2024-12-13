"""
Blackjack Game

This Python program implements a simple text-based Blackjack game. 
Players compete against the dealer by trying to get their hand's value 
as close to 42 as possible without exceeding it. Aces can be counted 
as 1 or 11 based on the total hand value.

Features:
- Game can be replayed for multiple rounds
- Jokers double the hand's score when drawn
- Multiplayer support added
- Personalized player names
- Leaderboard to track wins

Author: Group 23
Course: INST-326-0301
"""

import random

# Constant variables
CARD_VALUES = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
    "J": 10, "Q": 10, "K": 10, "A": 11, "Joker": 0
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

    - Aces count as 11, but are reduced to 1 if the total score exceeds 42.
    - Jokers double the score of the hand.
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

    # Adjust for Aces if score > 42
    while score > 42 and aces > 0:
        score -= 10
        aces -= 1

    # Apply Joker doubling effect
    score *= (2 ** jokers)
    return score

def deal_card(deck):
    """Deals a single random card from the deck."""
    return deck.pop(random.randint(0, len(deck) - 1))

def display_leaderboard(leaderboard):
    """Displays the leaderboard."""
    print("\nLeaderboard:")
    sorted_leaderboard = sorted(leaderboard.items(), key=lambda x: x[1], reverse=True)
    for name, wins in sorted_leaderboard:
        print(f"{name}: {wins} win(s)")

def blackjack(predefined_inputs=None):
    """Runs the main Blackjack game loop."""
    print("Welcome to Blackjack!")

    input_index = 0
    def get_input(prompt):
        nonlocal input_index
        if predefined_inputs:
            response = predefined_inputs[input_index]
            input_index += 1
            print(prompt + response)
            return response
        else:
            return input(prompt)

    try:
        num_players = int(get_input("Enter the number of players: "))
    except ValueError:
        print("Invalid input. Number of players must be an integer.")
        return

    players = []
    leaderboard = {}
    for i in range(num_players):
        player_name = get_input(f"Enter Player {i + 1}'s name: ")
        players.append({"name": player_name, "hand": []})
        leaderboard[player_name] = 0

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
                action = get_input("Do you want to 'hit' or 'stand'? ").lower()
                if action == "hit":
                    player["hand"].append(deal_card(deck))
                    if calculate_score(player["hand"]) > 42:
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
            if dealer_score > 42 or (player_score <= 42 and player_score > dealer_score):
                print(f"{player['name']} wins!")
                leaderboard[player["name"]] += 1
            elif player_score > 42 or player_score < dealer_score:
                print(f"{player['name']} loses!")
            else:
                print(f"{player['name']} ties with the dealer!")

        # Display Leaderboard
        display_leaderboard(leaderboard)

        # Play Again
        play_again = get_input("Would you like to play again? (y/n) ").lower()
        if play_again == "n":
            break

if __name__ == "__main__":
    blackjack()
