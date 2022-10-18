#! /usr/bin/env python3

import random
from player import Player
from slot_machine import SlotMachine 
from game import Game
import re

def request_int(prompt):
    while(True):
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Please, insert a number")
        
if __name__ == "__main__":
    print('''
      /$$$$$$  /$$        /$$$$$$  /$$$$$$$$       /$$      /$$  /$$$$$$   /$$$$$$  /$$   /$$ /$$$$$$ /$$   /$$ /$$$$$$$$
     /$$__  $$| $$       /$$__  $$|__  $$__/      | $$$    /$$$ /$$__  $$ /$$__  $$| $$  | $$|_  $$_/| $$$ | $$| $$_____/
    | $$  \__/| $$      | $$  \ $$   | $$         | $$$$  /$$$$| $$  \ $$| $$  \__/| $$  | $$  | $$  | $$$$| $$| $$      
    |  $$$$$$ | $$      | $$  | $$   | $$         | $$ $$/$$ $$| $$$$$$$$| $$      | $$$$$$$$  | $$  | $$ $$ $$| $$$$$   
     \____  $$| $$      | $$  | $$   | $$         | $$  $$$| $$| $$__  $$| $$      | $$__  $$  | $$  | $$  $$$$| $$__/   
     /$$  \ $$| $$      | $$  | $$   | $$         | $$\  $ | $$| $$  | $$| $$    $$| $$  | $$  | $$  | $$\  $$$| $$      
    |  $$$$$$/| $$$$$$$$|  $$$$$$/   | $$         | $$ \/  | $$| $$  | $$|  $$$$$$/| $$  | $$ /$$$$$$| $$ \  $$| $$$$$$$$
     \______/ |________/ \______/    |__/         |__/     |__/|__/  |__/ \______/ |__/  |__/|______/|__/  \__/|________/
    ''')
    #prompt user initial deposit 
    credits = request_int("How many credits do you want to deposit? ")

    # start game
    game = Game(Player(credits), SlotMachine())

    game.display_info()
    while not game.is_over():
        option = input("Play? [y/N] ")
        # exit if user wants to leave
        if re.match("n|q|e", option.lower()):
            break
        # request bet untill a valid one is given (sufficient credits)
        while True:
            bet = request_int("Place your bet: ")
            try:
                game.play_round(bet)
                break
            # if insufficient funds
            except AssertionError as e:
                print(e)

        # display slot and player info 
        print(game)
