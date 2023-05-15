import pygame

pygame.init()
menufont = pygame.font.Font(None, 50)

#colors
class Draw:
    gray = (115, 107, 146)
    nice_blue_body = (229, 190, 237)
    colors = {
        "R": (217, 37, 30),  # red
        "O": (222, 113, 40),  # orange
        "Y": (227, 200, 23),  # yellow
        "G": (71, 186, 58),  # green
        "B": (62, 93, 201),  # blue
        "V": (116, 56, 150),  # violet
        "P": (217, 80, 171),  # pink
        "W": (34, 34, 36),  # black
        "H": (237, 228, 229)  # white
    }


    easy_button = pygame.image.load("pngs/button_easy.png")
    hard_button = pygame.image.load("pngs/button_hard.png")

    win_pic = pygame.image.load("pngs/you_won.png")
    lose_pic = pygame.image.load("pngs/you_lost.png")

    returnmenu_button = pygame.image.load("pngs/button_menu.png")
    start_button = pygame.image.load("pngs/button_start.png")

    settings_button = pygame.image.load("pngs/button_settings.png")
    load_button = pygame.image.load("pngs/button_load.png")
    save_button = pygame.image.load("pngs/button_save_small.png")

    screen = []


    def draw_game(self,screen,curr,game,body):

        if curr == -1:
            self.draw_difficulty(screen,curr,game,body)
        elif curr == -2:
            self.draw_winscreen(screen,curr,game,body)
        elif curr == -3:
            self.draw_menu(screen,curr,game,body)
        elif curr == -4:
            self.draw_settings(screen,curr,game,body)
        else:
            self.draw_gameboard(screen,curr,game,body)

    def draw_menu(self,screen,curr,game,body):
        screen.fill(self.gray)
        screen.blit(self.start_button, (body.start_button.x, body.start_button.y))
        screen.blit(self.settings_button, (body.settings_button.x, body.settings_button.y))
    def draw_gameboard(self,screen,curr,game,body):
        y = 150
        x = 150
        screen.fill(self.gray)
        screen.blit(self.save_button, (body.save_button.x, body.save_button.y))
        pygame.draw.rect(screen, self.nice_blue_body, body.main_body, 0)
        for i in range(len(game.current_game["rows"])):  # going for each row
            counter = 0
            for j in game.current_game["rows"][i]:  # getting each letter in row ex. 'RRRVVV' j is R
                pygame.draw.rect(screen, self.colors[j], body.dic_buttons[i + 1][counter], 0)
                counter += 1
        for i in range(7):
            pygame.draw.rect(screen, self.colors[body.colors_names[i]], body.picker[i], 0)
        for i in range(len(game.current_game["pins"])):
            counter = 0
            for j in game.current_game["pins"][i]:
                pygame.draw.rect(screen, self.colors[j], body.dic_pins[i + 1][counter], 0)
                counter += 1

    def draw_winscreen(self,screen,curr,game,body):
        screen.fill(self.gray)
        #pygame.draw.rect(screen, (200, 200, 200), body.hard, 0)
        screen.blit(self.returnmenu_button, (body.menu_button.x, body.menu_button.y))
        if game.current_game["win"]:
            screen.blit(self.win_pic, (164, 100))
        else:
            screen.blit(self.lose_pic, (175, 100))

    def draw_difficulty(self,screen,curr,game,body):
        screen.fill(self.gray)
        screen.blit(self.easy_button,(body.easy_button.x,body.easy_button.y))
        screen.blit(self.hard_button, (body.hard.x,body.hard.y))

    def draw_settings(self, screen, curr, game, body):

        screen.fill(self.gray)
        screen.blit(self.returnmenu_button, (body.menu_button.x, body.menu_button.y))
        screen.blit(self.load_button, (body.load_button.x, body.load_button.y))



