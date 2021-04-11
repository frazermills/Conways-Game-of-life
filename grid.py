import pygame, random

class Grid:
    def __init__(self, screen, offset, scale, alive_colour, dead_colour):
        self.__scale = scale
        self.__screen = screen
        self.__offset = offset

        self.__alive_colour = alive_colour
        self.__dead_colour = dead_colour

        self.__cols = screen.get_height() // scale
        self.__rows = screen.get_width() // scale
        
        self.__size = (self.__rows, self.__cols)
        self.__arr = [[0 for i in range(self.__rows)] for i in range(self.__cols)]

        self.__neighbour_sum = 0

    @property
    def Arr(self):
        return self.__arr

    @Arr.setter
    def Arr(self, value):
        self.__arr = value

    def make_2d_array(self):
        for i in range(self.__cols):
            for j in range(self.__rows):
                self.__arr[i][j] = random.randrange(2)

    def draw_cell(self, x, y, size, colour):
        pygame.draw.rect(self.__screen, colour, (x, y, size, size))

    def count_neighbours(self, x, y):
        self.__neighbour_sum = 0
        
        for i in range(-1, 2):
            for j in range(-1, 2):
                x_edge = (x + i + self.__rows) % self.__rows
                y_edge = (y + j + self.__cols) % self.__cols
                self.__neighbour_sum += self.__arr[x_edge][y_edge]

        self.__neighbour_sum -= self.__arr[x][y]

    def display_grid(self):
        for x in range(self.__rows):
            for y in range(self.__cols):
                cell_x = x * self.__scale
                cell_y = y * self.__scale
                cell_size = self.__scale - self.__offset
                
                if self.__arr[x][y] == 1:
                    colour = self.__alive_colour     
                else:
                    colour = self.__dead_colour

                self.draw_cell(cell_x, cell_y, cell_size, colour)

    def check_rules(self):
        nextArr = [[0 for i in range(self.__rows)] for i in range(self.__cols)]

        for x in range(self.__rows):
            
            for y in range(self.__cols):
                
                state = self.__arr[x][y]
                self.count_neighbours(x, y)
                neighbours = self.__neighbour_sum
                
                if state == 0 and neighbours == 3:
                    nextArr[x][y] = 1
                elif state == 1 and (neighbours < 2 or neighbours > 3):
                    nextArr[x][y] = 0
                else:
                    nextArr[x][y] = state

        self.__arr = nextArr
