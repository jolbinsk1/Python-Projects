# Two Basic Python Games

## Game 1: Blackjack 

The script runs a simple text-based version of the card game Blackjack. The game allows a single player to play against a dealer. The player can bet chips, and hit or stand to get a hand value as close to 21 as possible without going over it.

### How to Play

1) The game starts with a welcome message and a shuffled deck.
2) Both the player and the dealer are dealt two cards each.
3) The player can place a bet.
4) The player can choose to "Hit" (take another card) or "Stand" (end their turn).
5) The dealer reveals their hand and must hit until their hand value is at least 17.
6) The game determines the winner based on the hand values:
- Player busts if their hand value exceeds 21.
- Player wins if their hand value is higher than the dealer's without busting.
- Dealer wins if the dealer's hand value is higher than the player's without busting.
- A tie results in a push.
7) The player can choose to play another hand or exit the game.

### Project Structure

- `Card` class: Represents a single playing card.
- `Deck` class: Represents a deck of cards.
- `Hand` class: Represents a player's or dealer's hand.
- `Chips` class: Manages the player's chips and bets.
- Various functions to handle gameplay actions like taking bets, hitting, standing, and showing cards.

### How to Run

To run the game, all you need to do is execute the Python script. You will interact with the game through the terminal.

``` bash
python blackjack.py
```

## Game 2: Tic Tac Toe

This is a simple text-based input version of Tic Tac Toe. The game allows two players to play against each other, taking turns to place their markers (X or O) on a 3x3 board.

### How to Play

1) The game starts with a welcome message and prompts both players to enter their usernames.
2) Players choose their markers (X or O).
3) The game randomly decides which player goes first.
4) Players take turns to place their markers on the board by choosing a position (1-9).
5) The game checks for a win condition after each move:
- A player wins if they have three of their markers in a row, column, or diagonal.
- The game is a tie if the board is full and no player has won.
6) The game displays the board after each move.
7) Players can choose to play another round or exit the game.

### Project Structure

- `display_board(board)`: Displays the Tic Tac Toe board.
- `player_info()`: Prompts players for their usernames and markers.
- `place_marker(board, marker, position)`: Places a marker on the board.
- `win(board, marker)`: Checks if a player has won.
- `first_turn(username_1, username_2)`: Randomly decides which player goes first.
- `empty_space(board, position)`: Checks if a position on the board is empty.
- `player_turn(board)`: Prompts a player to choose their next move.
- `full_board_check(board)`: Checks if the board is full.
- A while loop that handles the flow of the game.

### How to Run

Just like in blackjack, all you need to do is Python script. You will interact with the game through the terminal.

```bash
python tic_tac_toe.py
```
