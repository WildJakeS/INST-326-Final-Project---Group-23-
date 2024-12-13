# INST-326-Final-Project---Group-23- 

## Overview  
This program will implement a simple text based Blackjack game named ``BEWILDERING BLACKJACK``. Players will play against the dealer in a unique game of Blackjack where players will need to reach a score of 42 to win. To further increase the challenge, unique cards will be added to enhance the game such as the Joker card.

Through this project, we hope to create a user-friendly and engaging game that demonstrates our  problem-solving ability, data structure and object-oriented programming skills and growth.


## Features  
- After the winner is declared, players have the ability to replay for multiple rounds without needing to restart the code
- Jokers double your current hand
- Aces can be counted as 1 or 11 based on the total hand value
- Multiplayer support added
- Personalized named option for players


## Usage
### Option 1: Clone Repository

git `clone` https://github.com/WildJakeS/INST-326-Final-Project---Group-23-.git 
`cd` INST-326-Final-Project---Group-23-

### Option 2: Copy/ Downdload the code
Copy or download the code from the cards.py file in the ``INST-326-Final-Project---Group-23-`` repository

## Running the code  
python cards.py  

Running this code will start the game.The game will handle the dealer's actions and determine the winner.

## Playing the Game  
- Goal: get your hand as close to 21 without exceeeding it
- Commands:  
hit: Draw another card  
stand: End your turn

## Gameplay Example 
Run this code in your terminal
```bash 
python cards.py
```
Example of how they game will play
```
Welcome to Blackjack!  
Enter the number of players: 1  
Enter Player 1's name: Player 1  

Player 1's Turn:  
Player 1's Hand: ['K of Spades', '2 of Diamonds'] -> Score: 12  
Do you want to 'hit' or 'stand'? hit  
Player 1 busted!  
  
Dealer's Turn...  
Dealer's Hand: ['8 of Clubs', '8 of Diamonds', '2 of Hearts'] -> Score: 18  
Player 1 wins!  
Would you like to play again? (y/n) y  

Player 1's Turn:  
Player 1's Hand: ['Q of Clubs', '3 of Clubs'] -> Score: 13  
Do you want to 'hit' or 'stand'? hit  
Player 1's Hand: ['Q of Clubs', '3 of Clubs', '8 of Hearts'] -> Score: 21  
Do you want to 'hit' or 'stand'? stand  

Dealer's Turn...  
Dealer's Hand: ['A of Clubs', '3 of Hearts', '10 of Hearts', '9 of Hearts'] -> Score: 23  
Player 1 wins!  
Would you like to play again? (y/n) n 
