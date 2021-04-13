# Conways-Game-of-life:
---

## This project is an simulation of Conway's Game of Life
[A demonstration of the project](https://www.youtube.com/watch?v=Onq-GCmSuPU)

## Rules of the game:

* The game is operated on an infinite, two-dimensional, orthogonal grid of square cells. 
* Each one of these cells have two states (alive or dead). The cells follow these rules: 
    1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.
    2. Any live cell with two or three live neighbours lives on to the next generation.
    3. Any live cell with more than three live neighbours dies, as if by overpopulation.
    4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
* The oportunities for the game are more complicated that, so I recomend [this for further reading](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life#Rules)
---

## What I plan to do with this project:

* [x] To create a simple version that initialises each cell as either dead or alive

* [x] Display this data visually using pygame

* [x] Implement the rules of the game and change each cell's values accordingly 

* [x] Add in a custom starting screen with:

	* [ ] The ability to set custom values for the number of columns and rows

	* [ ] The ability to change all of the settings

	* [ ] Credits
	
* [ ] An interactive mode that allows for each cell to be modified by the user

## Requirements:
* python 3
* pygame
