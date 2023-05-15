import pygame

class BodyAndMind: #class consisting of clickable buttons (body) and fuctions handling clicking (mind)

    colors_names = "ROYGBVP"
    # text and buttons
    easy_button = pygame.Rect(269, 100, 265, 100)
    hard = pygame.Rect(269, 300, 250, 100)
    settings_button = pygame.Rect(227, 300, 350, 100)
    start_button = pygame.Rect(269, 100, 270, 100)
    menu_button = pygame.Rect(274, 300, 250, 100)
    main_body = pygame.Rect(100, 100, 500, 800)
    load_button = pygame.Rect(280, 100, 241, 100)
    save_button = pygame.Rect(610, 820, 100, 100)
    #structure
    picker = []
    dic_buttons = {
        -4: [load_button,menu_button],
        -3: [easy_button,hard],
        -1: [easy_button,hard],
        -2: [menu_button]
    }
    dic_pins = {}
    
    def generate_buttons(self): #generating pygame recs for places where we can put the pins and pinbords
        for i in range(9):
            self.dic_buttons[i] = []
            self.dic_pins[i] = []
            for j in range(5):
                self.dic_buttons[i].append(pygame.Rect(150+50*j,50+100*i,25,25))
                self.dic_pins[i].append(pygame.Rect(450 + 25 * j, 50 + 100 * i, 10, 10))
            if i<7:
                self.picker.append(pygame.Rect(650, 100 +75*i,50,50))
                
    def handle_clicks(self,mouse,buttons): #basic function returning number of what was clicked
        for i in range(len(buttons)):
            if pygame.Rect.colliderect(mouse,buttons[i]):
                #print("click",i)
                return [True,i]
        return [False,-1]
    
    def it_clicked(self,what, phaze,game): #takes in id of what buttons was clicked and depending on the current phaze does what the button is supposed to be doing
        if phaze<0:
            if what>0:
                return "hard"
            else:
                return "easy"
        else:
            if what<5: #0-4 are the places we can place the pin, numbers above are the color pickers and save
                game.current_game["rows"][phaze-1] = game.current_game["rows"][phaze-1][0:what] + game.current_game["current_click"] + game.current_game["rows"][phaze-1][what+1:5]
                #for example if current row is WWWWW, we want to change the second one and current click is R (meaning red) then it will merge W + R + WWW
            else:
                if what<12:
                    game.current_game["current_click"] = self.colors_names[what-5]
                else:
                    game.safe_game()