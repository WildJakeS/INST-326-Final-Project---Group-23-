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
    """Creates a standard deck of 52 cards plus 2 Jokers."""
    deck = [f"{rank} of {suit}" for rank in CARD_VALUES if rank != "Joker" for suit in SUITS]
    deck.extend(["Joker", "Joker"])
    random.shuffle(deck)
    return deck

def calculate_score(hand):
    """Calculates the total score of a player's hand."""
    score = 0
    aces = 0
    for card in hand:
        rank = card.split(" ")[0]
        score += CARD_VALUES[rank]
        if rank == "A":
            aces += 1

    # Adjust for aces if score exceeds 42
    while score > 42 and aces:
        score -= 10
        aces -= 1

    return score

def display_leaderboard(leaderboard):
    """Displays the leaderboard with player wins."""
    print("\nLeaderboard:")
    for player, wins in leaderboard.items():
        print(f"{player}: {wins} wins")

def get_input(prompt):
    """Handles user input and ensures valid responses."""
    while True:
        response = input(prompt).strip().lower()
        if response in ["hit", "stand", "y", "n"]:
            return response
        print("Invalid input! Please type 'hit', 'stand', 'y', or 'n'.")

def blackjack(predefined_inputs=None):
    """Main function for playing the Blackjack game."""
    print("Welcome to Blackjack!")

    num_players = int(input("Enter the number of players: "))
    players = [input(f"Enter Player {i + 1}'s name: ") for i in range(num_players)]
    leaderboard = {player: 0 for player in players}

    while True:
        deck = create_deck()
        dealer_hand = []
        player_hands = {player: [] for player in players}

        # Deal initial two cards to each player and the dealer
        for player in players:
            player_hands[player].append(deck.pop())
            player_hands[player].append(deck.pop())
        dealer_hand.append(deck.pop())
        dealer_hand.append(deck.pop())

        # Player turns
        for player in players:
            print(f"\n{player}'s Turn:")
            while True:
                hand = player_hands[player]
                score = calculate_score(hand)
                print(f"{player}'s Hand: {hand} -> Score: {score}")

                if score > 42:
                    print(f"{player} busted!")
                    break

                action = get_input("Do you want to 'hit' or 'stand'? ")
                if action == "stand":
                    break
                elif action == "hit":
                    hand.append(deck.pop())

        # Dealer's turn
        print("\nDealer's Turn:")
        while calculate_score(dealer_hand) < 30:  # Dealer hits until score >= 30
            dealer_hand.append(deck.pop())

        dealer_score = calculate_score(dealer_hand)
        print(f"Dealer's Hand: {dealer_hand} -> Score: {dealer_score}")

        # Determine winners
        for player in players:
            player_score = calculate_score(player_hands[player])
            if player_score > 42:
                print(f"{player} loses!")
            elif dealer_score > 42 or player_score > dealer_score:
                print(f"{player} wins!")
                leaderboard[player] += 1
            elif player_score == dealer_score:
                print(f"{player} ties with the dealer!")
            else:
                print(f"{player} loses!")

        # Ask to play again
        play_again = get_input("Would you like to play again? (y/n) ")
        if play_again == "n":
            break

    # Display final leaderboard
    display_leaderboard(leaderboard)

if __name__ == "__main__":
    blackjack()
