import pygame

import mechanics
import scripts
import game

#initializing things
FPS = 60
fpsClock = pygame.time.Clock()
pygame.init()

#screen
screen = pygame.display.set_mode((800, 1000))


#variables
current_phaze = -3
chosen = True


def main():
    global ifmenu, current_phaze

    #generating objects
    currentGAME = game.Game("easy")
    MainDraw = scripts.Draw()
    Mind = mechanics.BodyAndMind()
    Mind.generate_buttons()

    # starting up the screen
    screen.fill(MainDraw.gray)
    pygame.display.flip()
    running = True
    
    while running: #main game loop

        #print(current_phaze)
        mouse = pygame.Rect(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1],10,10) #getting mouse position

        if current_phaze < 0:
            objects = Mind.dic_buttons[current_phaze]
        else:
            objects = Mind.dic_buttons[current_phaze] + Mind.picker + [Mind.save_button]

        MainDraw.draw_game(screen,current_phaze,currentGAME,Mind)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_l: # autolosing debug
                    current_phaze = 8
                    currentGAME.current_game["phaze"] = 7

            if event.type == pygame.MOUSEBUTTONUP: #checking if anything is clicked
                what_clicked = Mind.handle_clicks(mouse,objects) #returns [ true/false if anything clickable was clicked, and number of what was clicked]
                if what_clicked[0]: #checks if anything actually clickable was clicked
                    if current_phaze <0:
                        if current_phaze == -3:  # menu is still opened
                            if what_clicked[1] == 0:  # start was clicked
                                current_phaze = -1
                            else:
                                current_phaze = -4
                        elif current_phaze == -4:  # settings
                            if what_clicked[1] == 0:
                                currentGAME.load_game()
                                current_phaze = currentGAME.current_game["phaze"]
                            else:
                                current_phaze = -3
                        elif current_phaze == -1: #current phaze -1 is when we're still in the menu/difficulty was not picked yet
                            #picking the difficulty
                            clicking = Mind.it_clicked(what_clicked[1],current_phaze,currentGAME)
                            currentGAME.current_game["difficulty"] = clicking
                            current_phaze = 1
                            currentGAME.generete_password()
                        elif current_phaze == -2:
                            current_phaze = -3
                    else:
                        if current_phaze<8:
                            #actual game
                            clicking = Mind.it_clicked(what_clicked[1], current_phaze, currentGAME)
                            if currentGAME.end_of_tour(): #checks if all the places in current row were filled out
                                currentGAME.current_game["phaze"] += 1 #changes current row
                                current_phaze += 1
                                if currentGAME.round_score():
                                    currentGAME.cleanrows()
                                    currentGAME.current_game["win"] = True
                                    current_phaze = -2  # ends game
                        else:
                            currentGAME.cleanrows()
                            current_phaze = -2  # ends game


        pygame.display.update() #updating the screen
        fpsClock.tick(FPS)

main()