# author: Frazer Mills
# title: Conway's Game of Life
# date: 11/04/21

import pygame
import grid
import menu_system

def menu_handler(menu_mode, screen, text_font, text_colour, button_colour):
    game_mode = "default_game" 
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
                    
                elif start_menu.Option == "iterative mode":
                    game_mode = "iterative_game"
                    in_menu = False

                elif start_menu.Option == "quit game":
                    pygame.quit()
                    quit()

    return game_mode

def main():
    pygame.init()
    pygame.display.set_caption("Conway's game of life - by Frazer Mills")

    HEIGHT = 800
    WIDTH = 800
    size = (WIDTH, HEIGHT)

    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    text_font = pygame.font.SysFont("Arial", 20)

    colours = {
        "BLACK": (0, 0, 0),
        "WHITE": (255, 255, 255),
        "GREY": (105,105,105),
        "LIGHT_GREY": (211,211,211),
        "RED":(255, 0, 0),
        "GREEN": (0, 255, 0),
        "YELLOW": (255, 255, 0)
    }

    settings = {
        "text_colour": colours["WHITE"],
        "button_colour": colours["RED"],
        "alive_cell_colour": colours["YELLOW"],
        "dead_cell_colour": colours["GREY"],
        "grid_line_colour": colours["BLACK"],
        "menu_mode": "start",
        "fps": 30
    }

    scale = 8
    offset = 1

    game_mode = menu_handler(settings["menu_mode"], screen, text_font, settings["text_colour"], settings["button_colour"])

    game_grid = grid.Grid(screen, offset, scale, settings["alive_cell_colour"], settings["dead_cell_colour"])
    game_grid.make_2d_array()

    if game_mode == "iterative_game":
        iterative_game(settings, game_grid, clock, screen)

    elif game_mode == "default_game":
        default_game(settings, game_grid, clock, screen)

    else:
        raise Exception("Invalid game mode.")

def iterative_game(settings, game_grid, clock, screen):

    while True:
        mouse_clicked = event_handler(game_grid)

        if mouse_clicked:
            game_grid.display_grid()
            game_grid.check_rules()
            pygame.display.update()
            clock.tick(settings["fps"])
            screen.fill(settings["grid_line_colour"])

def default_game(settings, game_grid, clock, screen):
    
    while True:
        
        event_handler(game_grid)
        game_grid.display_grid()
        game_grid.check_rules()
        pygame.display.update()
        clock.tick(settings["fps"])
        screen.fill(settings["grid_line_colour"])

def event_handler(game_grid):
    mouse_clicked = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_clicked = True

    return mouse_clicked

if __name__ == "__main__":
    main()
