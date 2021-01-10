# author: Frazer Mills
# title: Conway's Game of Life
# date: 10.1.21

import pygame, sys
from random import randrange

def createCanvas(width, height, bgColour):
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

def setup(width, height, bgColour, resolution):
	createCanvas(width, height, bgColour)
	cols = width // resolution
	rows = height // resolution

	grid = make2DArray(cols, rows)
	for i in range(cols):
		for j in range(rows):
			grid[i][j] = randrange(2)
	return [grid, cols, rows]

def draw(grid, cols, rows, resolution):
	for i in range(cols):
		for j in range(rows):
			x = i * resolution
			y = j * resolution

			if grid[i][j] == 1:
				print("alive")
			else:
				print("dead")

def main():
	grid = []
	cols = 0
	rows = 0
	resolution = 10
	width, height = 600, 400
	BLACK = (0, 0, 0)
	WHITE = (255, 255, 255)

	tempList = setup(width, height, BLACK, resolution)
	
	grid = tempList[0]
	cols = tempList[1]
	rows = tempList[2]

	draw(grid, cols, rows, resolution)

if __name__ == '__main__':
	main()
