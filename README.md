# Extended board Tic-tac-toe with AI
Game tic-tac-toe with larger boards made in python, using pygame.

AI can use minimax with alpha beta pruning algorithm.
## Purpose of the project
I wanted to practice using git and learn python, so I came
up with this project.

## Project assumptions
I wanted to make a game that would run on command line
and then turn it into a windowed version using pygame.

## About game
This is an **extended** version of the 3x3 tic-tac-toe game.
## Board
In my game, the player can choose a **board size** from 3x3 to 
10x10. Only square boards are available.

Player can also choose the number of x or o's **in the line**
needed to win. The allowed values are in the range 3 to 10.
## Game modes
There are two ways to play: player vs player or player vs AI.
Starting player is always drawn at the start of the round.
### Player vs player
Two players take turns choosing a square.
### Player vs AI
Player chooses field. Then computer calculates his move based on:
- **Minimax with alpha beta prune algorithm** written on the
 basis of [Code train](https://www.youtube.com/watch?v=trKjYdBASyQ&t=1054s)
 and [Stack Abuse article](https://stackabuse.com/minimax-and-alpha-beta-pruning-in-python/)
- **My algorithm**, that check the possibility of winning or losing in a few moves.
If there is no one, it chooses field at random.

**Algorithms is selected based on the size of the board. 
For the 3x3 board it will choose minimax,
and for larger boards it will choose my algorithm.**
