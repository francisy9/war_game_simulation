# War Game Simulation
## Second Python porject. Created and finished in Sep 2020.

How the game works: 

1: A deck of cards are split evenly between 2 players facing down. 

2: Each player plays a card each turn. 

3: The player who played the card with a higher value takes all cards in play. (i.e. King has a higher value than Queen. In this iteration, Ace has the highest value)

4: If the cards played have the same value, the two players go to 'war'.

5: Then, both players place 10 cards (or however many card remaining in their hand - 1) onto the board.

6: Back to step 3

7: Until a player uses up all of its cards, then the other player wins. 

Use:

To see how varying certain numbers or rules would change the number of rounds needed to finish the game. E.g. changing 10 to 3 would massively prolong the game or changing the game so that if a player doesn't have a fixed amount of cards to go to war, that player loses.

How to run:

`git clone git@github.com:francisy9/war_game_simulation`

`cd TicTacToe`

`python War_Game_Simulation.py`
