import pygame

class StartMenu:
    def __init__(self, screen, font, text_colour, button_colour):
        self.__screen = screen
        self.__font = font
        self.__text_colour = text_colour
        self.__button_colour = button_colour
        self.__click = False
        self.__button_width = 150
        self.__button_height = 75
        self.__option = None
        self.__buttons_xy = None
        self.__button_objects = None
        self.__button_command = ["start game", "option 1", "quit game"]
        self.__title = "Conway's Game of Life - by Frazer Mills"

    @property
    def Option(self):
        return self.__option

    def setup(self):
        pygame.display.set_caption(f"{self.__title}")
        self.__screen.fill((0,0,0))
        
    def draw_text(self, text, x, y):
        textobj = self.__font.render(text, 1, self.__text_colour)
        textrect = textobj.get_rect()
        textrect.center = (x, y)
        self.__screen.blit(textobj, textrect)

    def get_button_objects(self):
        self.__buttons_xy = [
            ((self.__screen.get_width() // 2) - (self.__button_width // 2), (self.__screen.get_width() // 2) - i)
            for i in reversed(range(-100, 200, 100))
        ]

        self.__button_objects = {
            f"button {i}": pygame.Rect(self.__buttons_xy[i][0], self.__buttons_xy[i][1], self.__button_width, self.__button_height)
            for i, button in enumerate(self.__buttons_xy)
        }

    def check_collisions(self):
        mousex, mousey = pygame.mouse.get_pos()
        
        if self.__button_objects[f"button 0"].collidepoint((mousex, mousey)):
            if self.__click:
                self.__option = self.__button_command[0]
                
        elif self.__button_objects[f"button 1"].collidepoint((mousex, mousey)):
            if self.__click:
                self.__option = self.__button_command[1]
                
        elif self.__button_objects[f"button 2"].collidepoint((mousex, mousey)):
            if self.__click:
                self.__option = self.__button_command[2]
        
    def display_buttons(self):
        
        for i, button_object in enumerate(self.__button_objects):
            pygame.draw.rect(self.__screen, self.__button_colour, self.__button_objects[button_object])
        
        self.draw_text(f"{self.__title}", self.__screen.get_width() // 2, self.__screen.get_height() // 4)
        self.draw_text(f"{self.__button_command[0]}", self.__buttons_xy[0][0] + 75, self.__buttons_xy[0][1] + 35)
        self.draw_text(f"{self.__button_command[1]}", self.__buttons_xy[1][0] + 75, self.__buttons_xy[1][1] + 35)
        self.draw_text(f"{self.__button_command[2]}", self.__buttons_xy[2][0] + 75, self.__buttons_xy[2][1] + 35)

        pygame.display.update()

    def is_clicked(self):
        self.__click = False
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                    
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == True:
                    self.__click = True
