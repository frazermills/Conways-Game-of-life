import pygame, random

class Grid:
    def __init__(self, screen, offset, scale, alive_colour, dead_colour):
        self.scale = scale
        self.screen = screen
        self.offset = offset

        self.alive_colour = alive_colour
        self.dead_colour = dead_colour

        self.cols = screen.get_height() // scale
        self.rows = screen.get_width() // scale
        
        self.size = (self.rows, self.cols)
        self.arr = [[None for i in range(self.rows)] for i in range(self.cols)]

    def make_2d_array(self):
        for i in range(self.cols):
            for j in range(self.rows):
                self.arr[i][j] = random.randrange(2)

    def draw_cell(self, x, y, size, colour):
        pygame.draw.rect(self.screen, colour, (x, y, size, size))

    def count_neighbours(self, x, y):
        neighbour_sum = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                x_edge = (x + i + self.rows) % self.rows
                y_edge = (y + j + self.cols) % self.cols
                neighbour_sum += self.arr[x_edge][y_edge]

        neighbour_sum -= self.arr[x][y]
        return neighbour_sum

    def conway(self):
        for x in range(self.rows):
            for y in range(self.cols):
                cell_x = x * self.scale
                cell_y = y * self.scale
                cell_size = self.scale - self.offset
                
                if self.arr[x][y] == 1:
                    colour = self.alive_colour     
                else:
                    colour = self.dead_colour

                self.draw_cell(cell_x, cell_y, cell_size, colour)

    def check_rules(self):
        nextArr = [[None for i in range(self.rows)] for i in range(self.cols)]

        for x in range(self.rows):
            for y in range(self.cols):
                state = self.arr[x][y]
                neighbours = self.count_neighbours(x, y)
                if state == 0 and neighbours == 3:
                    nextArr[x][y] = 1
                elif state == 1 and (neighbours < 2 or neighbours > 3):
                    nextArr[x][y] = 0
                else:
                    nextArr[x][y] = state

        self.arr = nextArr
