# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 22:16:17 2016

@author: Kendrick Kwok

Mardrick Game: 
    Adventurer is created. Will be sent to battle 
"""

#import monsters
#import buildings
import adventure

class Player(Adventure):
    #player goes on an adventure add new functions
    def __init__(self, hitpoints = 30, level = 1, attack = 4, coins=0, exp=0):
        #super().__init__(self)
        self.hitpoints = hitpoints
        self.level = level
        self.attack = attack
        self.coins = coins
        self.exp = exp

#declarations
start = True
player1 = Player()

while start:

    if (player1.hitpoints <= 0):
        print("You died")
        start = False
        break
        
    player1.menu()
    
    choice = input()
    
    if (choice == '5'):
        start = False
    else:
        player1.selection(choice)
        start = True
             
        
        