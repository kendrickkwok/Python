# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 22:16:17 2016

@author: Kendrick Kwok

Mardrick Game: 
    Adventurer is created. Will be sent to battle 
"""

class Monster(object):
    #player oes on an adventure add new functions
    def __init__(self, hitpoints = 20, level = 1, attack = 2, coins = 50):
        #super().__init__(self)
        self.hitpoints = hitpoints
        self.level = level
        self.attack = attack
    

class Boss(Monster):
    #player oes on an adventure add new functions
    def __init__(self, hitpoints = 60, level = 5, attack = 3, coins = 100, exp = 50):
        #super().__init__(self)
        self.hitpoints = hitpoints
        self.level = level
        self.attack = attack
        self.coins = coins
        self.exp = exp
        
class Goblins(Monster):
    #Low leve goblin
    def __init__(self, hitpoints = 10, level = 0, attack = 1, coins = 5, exp = 20):
        self.hitpoints=hitpoints
        self.level= level
        self.attack = attack
        self.coins = coins
        self.exp = exp
    

#rawrxD = Monster()