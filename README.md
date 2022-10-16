# UnBlock Me Solver
A simple solver for the tile puzzle game that uses search to find the best moves to achieve goal. The user will use a limit to allow the program to explore other branches after the limit has been reached.

## Tile Puzzle Game
The tile puzzle game is a straightforward puzzle game where the player is given a 3x3 board of numbers 1-8 and one blank tile. The player then proceeds to move the tiles so that the tiles are in numerical order. For this program, the board is represented as a List of Lists and uses various functions to swap tiles to manipulate the starting board to the goal state.

## User Inputs
The user will provide the following inputs
- a start state which will be the tile puzzle board 
- the goal state 
- the limit which controls how deep the program will search
