import pygame
import random
class Game:

    #main game dictionary that contains all the information about the current game
    current_game = {
        "difficulty" : "easy",
        "phaze" : 1, #current row
        "password": "RRRRR",
        "rows": 7*["WWWWW"],
        "pins": [],
        "current_click" : "W",
        "win" : False
    }

    def __init__(self,diff):
        self.current_game["difficulty"] = diff

    def cleanrows(self):
        self.current_game["phaze"] = 1
        self.current_game["rows"] = 7*["WWWWW"]
        self.current_game["pins"] = []
        self.current_game["current_click"] = "W"
        self.current_game["win"] = False

    def load_game(self):
        keys = list(self.current_game.keys())
        save_file = open('save_file.txt','r')
        save_data = save_file.read().split('\n')
        self.current_game[keys[0]] = save_data[0]
        self.current_game["phaze"] = int(save_data[1])
        #print( int(save_data[1]))
        self.current_game[keys[2]] = save_data[2]
        self.current_game[keys[3]] = save_data[3].replace('[', '').replace(']', '').replace('\'','').replace(',','').split(' ')
        if len(save_data[4].replace('[', '').replace(']', '')) != 0:
            temp2 = []
            for i in save_data[4]:
                if ord(i)>64 and ord(i)<91:
                    temp2.append(i)
                if i ==']':
                    self.current_game[keys[4]].append(temp2)
                    temp2 = []
        self.current_game[keys[5]] = save_data[5]
        self.current_game[keys[6]] = bool(save_data[6])


    def safe_game(self):
        keys = list(self.current_game.keys())
        save_file = open('save_file.txt','w')
        for i in range(len(keys)):
            save_file.write(str(self.current_game[keys[i]]))
            save_file.write('\n')
    def generete_password(self): #generating passoword
        colors = "ROYGBVP"
        password =""

        if self.current_game["difficulty"] == "hard": #if the hard is enabled there can be two pins of the same color
            colors = colors + colors

        for i in range(5):
            randm = random.randint(0, len(colors) - 1)
            password = password + colors[randm]
            colors = colors[0:randm] + colors[randm + 1:len(colors)] #making sure we dont pick the same color too many times

        print(password)
        self.current_game["password"] = password
    def end_of_tour(self): #checking if all the places are filled out
        #print(self.current_game["rows"][self.current_game["phaze"]-1],self.current_game["phaze"]-1 )
        if 'W' in self.current_game["rows"][self.current_game["phaze"]-1]:
            return False
        else:
            return True
    def round_score(self): #checking colors put in by the user
        pins = []
        copy = self.current_game["rows"][self.current_game["phaze"]-2] #making copy of the row we're checking to not change the actual row
        password_copy = self.current_game["password"]

        for i in range(5): #checking the colors that are in the exact place
            if self.current_game["rows"][self.current_game["phaze"]-2][i] == self.current_game["password"][i]:
                pins.append("R")
                copy = copy[0:i] + "W" + copy[i+1:5] #replacing in a copy of the row we're checking the color we're already checked and confirmed
                password_copy = password_copy[0:i] + "W" + password_copy[i + 1: 5]

        for i in range(5): #checking the colors that are right but in a wrong place
            for j in range(5):
                if copy[i] == password_copy[j] and copy[i] != "W":
                    pins.append("H")
                    copy = copy[0:i] + "W" + copy[i+1 : 5]
                    password_copy = password_copy[0:j] + "W" + password_copy[j+1 : 5]
        self.current_game["pins"].append(pins) #adding a new pinset to pins
        if pins == 5*["R"]:
            return True
        else:
            return False





