# INST-326-Final-Project---Group-23- 
Jake Sheehi - Game Logic   
Johnathan Cook  - User Interface  
Ugo Onyejiaka  - Testing and Debugging  
Jaylen Williams -  Documentation

## Overview  
This program will implement a simple text based Blackjack game named ``BEWILDERING BLACKJACK``. Players will play against the dealer in a unique game of Blackjack where players will need to reach a score of 42 to win. To further increase the challenge, unique cards will be added to enhance the game such as the Joker card.

Through this project, we hope to create a user-friendly and engaging game that demonstrates our  problem-solving ability, data structure and object-oriented programming skills and growth.


## Features  
- After the winner is declared, players have the ability to replay for multiple rounds without needing to restart the code
- Jokers double your current hand
- Aces can be counted as 1 or 11 based on the total hand value
- Multiplayer support added
- Personalized named option for players
- Leaderboard to showcase total wins 


## Usage
### Option 1: Clone Repository
```bash
git clone https://github.com/WildJakeS/INST-326-Final-Project---Group-23-.git 
cd INST-326-Final-Project---Group-23-
```
### Option 2: Copy/ Downdload the code
Copy or download the code from the cards.py file in the ``INST-326-Final-Project---Group-23-`` repository

## Running the code  
```bash
python cards.py  
```

Running this code will start the game. The game will handle the dealer's actions and determine the winner.

## Playing the Game  
- Goal: To win the game, you must get your hand as close to 42 without exceeeding it.
- Commands:  
  - hit: Draw another card  
  - stand: End your turn

## Gameplay Example 
Run this code in your terminal to start the game
```bash 
python cards.py
```
Example of how they game will play
```
 Welcome to Blackjack!
Enter the number of players: 2  
Enter Player 1's name: Player 1
Enter Player 2's name: Player 2

Player 1's Turn:
Player 1's Hand: ['6 of Clubs', '8 of Hearts'] -> Score: 14
Do you want to 'hit' or 'stand'? hit
Player 1's Hand: ['6 of Clubs', '8 of Hearts', 'Q of Diamonds'] -> Score: 24
Do you want to 'hit' or 'stand'? hit
Player 1's Hand: ['6 of Clubs', '8 of Hearts', 'Q of Diamonds', '6 of Spades'] -> Score: 30
Do you want to 'hit' or 'stand'? stand

Player 2's Turn:
Player 2's Hand: ['6 of Diamonds', 'Q of Spades'] -> Score: 16
Do you want to 'hit' or 'stand'? hit
Player 2's Hand: ['6 of Diamonds', 'Q of Spades', '6 of Hearts'] -> Score: 22
Do you want to 'hit' or 'stand'? hit
Player 2's Hand: ['6 of Diamonds', 'Q of Spades', '6 of Hearts', 'J of Hearts'] -> Score: 32
Do you want to 'hit' or 'stand'? hit
Player 2's Hand: ['6 of Diamonds', 'Q of Spades', '6 of Hearts', 'J of Hearts', 'K of Diamonds'] -> Score: 42
Do you want to 'hit' or 'stand'? stand

Dealer's Turn:
Dealer's Hand: ['K of Spades', '9 of Clubs', '2 of Clubs', '4 of Hearts', '7 of Clubs'] -> Score: 32  
Player 1 loses!  
Player 2 wins!  
Would you like to play again? (y/n) y  

Player 1's Turn:  
Player 1's Hand: ['9 of Spades', '2 of Clubs'] -> Score: 11
Do you want to 'hit' or 'stand'? hit  
Player 1's Hand: ['9 of Spades', '2 of Clubs', '8 of Clubs'] -> Score: 19
Do you want to 'hit' or 'stand'? hit  
Player 1's Hand: ['9 of Spades', '2 of Clubs', '8 of Clubs', '3 of Hearts'] -> Score: 22
Do you want to 'hit' or 'stand'? hit  
Player 1's Hand: ['9 of Spades', '2 of Clubs', '8 of Clubs', '3 of Hearts', '5 of Clubs'] -> Score: 27
Do you want to 'hit' or 'stand'? hit  
Player 1's Hand: ['9 of Spades', '2 of Clubs', '8 of Clubs', '3 of Hearts', '5 of Clubs', '4 of Hearts'] -> Score: 31
Do you want to 'hit' or 'stand'? hit  
Player 1's Hand: ['9 of Spades', '2 of Clubs', '8 of Clubs', '3 of Hearts', '5 of Clubs', '4 of Hearts', 'K of Spades'] -> Score: 41  
Do you want to 'hit' or 'stand'? hit  
Player 1's Hand: ['9 of Spades', '2 of Clubs', '8 of Clubs', '3 of Hearts', '5 of Clubs', '4 of Hearts', 'K of Spades', 'A of Clubs'] -> Score: 42  
Do you want to 'hit' or 'stand'? hit  
Player 1's Hand: ['9 of Spades', '2 of Clubs', '8 of Clubs', '3 of Hearts', '5 of Clubs', '4 of Hearts', 'K of Spades', 'A of Clubs', '8 of Spades'] -> Score: 50  
Player 1 busted!  

Player 2's Turn:  
Player 2's Hand: ['2 of Spades', 'Q of Clubs'] -> Score: 12  
Do you want to 'hit' or 'stand'? hit  
Player 2's Hand: ['2 of Spades', 'Q of Clubs', '7 of Diamonds'] -> Score: 19  
Do you want to 'hit' or 'stand'? hit  
Player 2's Hand: ['2 of Spades', 'Q of Clubs', '7 of Diamonds', '8 of Hearts'] -> Score: 27  
Do you want to 'hit' or 'stand'? hit  
Player 2's Hand: ['2 of Spades', 'Q of Clubs', '7 of Diamonds', '8 of Hearts', 'Joker'] -> Score: 27  
Do you want to 'hit' or 'stand'? hit   
Player 2's Hand: ['2 of Spades', 'Q of Clubs', '7 of Diamonds', '8 of Hearts', 'Joker', '7 of Hearts'] -> Score: 34  
Do you want to 'hit' or 'stand'? stand  

Dealer's Turn:  
Dealer's Hand: ['5 of Spades', 'A of Diamonds', '6 of Clubs', '7 of Clubs', '3 of Spades'] -> Score: 32  
Player 1 loses!  
Player 2 wins!  
Would you like to play again? (y/n) n  

Leaderboard:
Player 1: 0 wins  
Player 2: 2 wins 
