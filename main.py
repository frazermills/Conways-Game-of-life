# author: Frazer Mills
# title: Conway's Game of Life
# date: 10/04/21

import pygame
import grid
import menu_system

def menu_handler(menu_mode, screen, text_font, text_colour, button_colour):
    in_menu = True

    while in_menu:

        if menu_mode == "start":
            start_menu = menu_system.StartMenu(screen, text_font, text_colour, button_colour)
            start_menu.setup()
            while start_menu.Option == None:
                start_menu.get_button_objects()
                start_menu.check_collisions()
                start_menu.display_buttons()
                start_menu.is_clicked()

                if start_menu.Option == "start game":
                    in_menu = False
                    
                elif start_menu.Option == "settings":
                    menu_mode = "settings"

                elif start_menu.Option == "quit game":
                    pygame.quit()
                    quit()

def main():
    pygame.init()
    pygame.display.set_caption("Conway's game of life - by Frazer Mills")

    HEIGHT = 800
    WIDTH = 800
    size = (WIDTH, HEIGHT)

    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    text_font = pygame.font.SysFont("Arial", 20)
    fps = 30

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)

    text_colour = WHITE
    button_colour = RED
    menu_mode = "start"

    scale = 8
    offset = 1

    settings_options = menu_handler(menu_mode, screen, text_font, text_colour, button_colour)

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
