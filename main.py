# author: Frazer Mills
# title: Conway's Game of Life
# date: 10.1.21

import pygame, sys, time
from random import randrange

def createCanvas(width, height, bgColour):
	global screen
	screen = pygame.display.set_mode((width, height))
	pygame.display.set_caption("Conway's game of life")
	screen.fill(bgColour)

	pygame.display.flip()

	running = True
	while not running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()

def make2DArray(cols, rows):
	arr = [None] * cols
	for i in range(len(arr)):
		arr[i] = [None] * rows
	return arr;

def drawCell(x, y, colour):
	pygame.draw.rect(screen, colour, (x, y, 10, 10))
	pygame.display.flip()

def countNeighbours(grid, x, y, cols, rows, neighbourSum):
	sum = 0
	for i in range(-1, 2):
		for j in range(-1, 2):
			col = (x + i + cols) % cols
			row = (y + j + rows) % rows
			neighbourSum += grid[col][row]

	neighbourSum -= grid[x][y]
	return neighbourSum


def setup(width, height, bgColour, resolution):
	createCanvas(width, height, bgColour)
	cols = width // resolution
	rows = height // resolution

	grid = make2DArray(cols, rows)
	for i in range(cols):
		for j in range(rows):
			grid[i][j] = randrange(2)
	return [grid, cols, rows]

def draw(grid, cols, rows, resolution, colour):
	for i in range(cols):
		for j in range(rows):
			x = i * resolution
			y = j * resolution

			if grid[i][j] == 1:
				drawCell(x, y, colour)

	nextArr = make2DArray(cols, rows)

	for i in range(cols):
		for j in range(rows):
			state = grid[i][j]

			neighbourSum = 0
			neighbours = countNeighbours(grid, i, j, cols, rows, neighbourSum)

			if state == 0 and neighbours == 3:
				nextArr[i][j] = 1
			elif state == 1 and (neighbours < 2 or neighbours > 3):
				nextArr[i][j] = 0
			else:
				nextArr[i][j] = state

	grid = nextArr

def main():
	grid = []
	cols = 0
	rows = 0
	resolution = 10
	width, height = 500, 500
	BLACK = (0, 0, 0)
	WHITE = (255, 255, 255)

	tempList = setup(width, height, BLACK, resolution)
	
	grid = tempList[0]
	cols = tempList[1]
	rows = tempList[2]

	draw(grid, cols, rows, resolution, WHITE)
	time.sleep(0.5)
	

for i in range(10):
	if __name__ == '__main__':
		main()
