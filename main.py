# author: Frazer Mills
# title: Conway's Game of Life
# date: 9.3.21

import pygame, random, grid

def main():
    pygame.init()
    pygame.display.set_caption("Conway's game of life - by Frazer Mills")

    HEIGHT = 800
    WIDTH = 800
    size = (WIDTH, HEIGHT)

    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    fps = 30

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    scale = 20
    offset = 1

    game_grid = grid.Grid(screen, offset, scale, WHITE, BLACK)
    game_grid.make_2d_array()

    while True:
        event_handler()
        game_grid.conway()
        game_grid.check_rules()
        
        pygame.display.update()
        clock.tick(fps)
        screen.fill(BLACK)

def event_handler():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

if __name__ == "__main__":
    main()
