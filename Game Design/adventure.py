# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 22:16:17 2016

@author: Kendrick Kwok

Mardrick Game: 
    Adventurer is created. Will be sent to battle 
"""
import monsters

class Adventure(object):
    #constructor that creates player 
    def __init__(self, hitpoints, level, attack, coins):
        print("Hello Adventurer!")
        self.hitpoints = hitpoints
        self.level = level
        self.attack = attack
        self.coins = coins
        
    def menu(self):
        print("Hello Adventure! Make a selection:")
        print("1. Go Dungeon")
        print("2. Go Nurse")
        print("3. Show Status")
        print("4. Go purchase the god sword (+20 Attack)")
        print("5. Exit")
        print("-->")
        
    #dictionary
    def selection(self, x):
        if(x == '1'): 
            self.goDungeon()
        elif(x == '2'): 
            self.heal()
        elif(x == '3'):
            self.showStatus()
        else: 
            print(x)
            self.purchaseGodSword() 
        
    
    def goDungeon(self):
        print("Which monster did you want to fight?")
        print("1. Goblins")
        print("2. BOSS")
        choice = input()
        if(choice == '1'):
            print("Off to battle...")
            print("Prepare yourself!!")                
            self.goGoblin()
        else:
            print("Off to battle...")
            print("Prepare yourself!!")
            self.goBoss()
    
    def goGoblin(self):
        goblin = monsters.Goblins()
        print()
        while(goblin.hitpoints > 0 and self.hitpoints > 0):
            self.hitpoints = self.hitpoints - goblin.attack
            print("You got attacked by a goblin with " + str(goblin.attack) + " damage")
            print("You have " + str(self.hitpoints) + " left")
            goblin.hitpoints = goblin.hitpoints - self.attack
            print("You attacked a goblin with " + str(self.attack) + " damage")
            print("The goblin has " + str(goblin.hitpoints) + " left")        

        if (self.hitpoints > 0):
            print("\nGoblin fainted")
            print("You gained " + str(goblin.coins) + " coins")
            print ("You gained " + str(goblin.exp)+ " exp")
            self.exp = self.exp + goblin.exp
            self.levelUp()
            self.coins = self.coins + goblin.coins
    
    
    def goBoss(self):
        boss = monsters.Boss()
        print()
        
        while(boss.hitpoints > 0 and self.hitpoints > 0):
            self.hitpoints = self.hitpoints - boss.attack
            print("You got attacked by the boss with " + str(boss.attack) + " damage")
            print("You have " + str(self.hitpoints) + " left")
            boss.hitpoints = boss.hitpoints - self.attack
            print("You attacked the boss with " + str(self.attack) + " damage")
            print("The boss has " + str(boss.hitpoints) + " left")        

        if (self.hitpoints > 0):
            print("\nBoss fainted")
            print("You gained " + str(boss.coins) + " coins")
            print ("You gained " + str(boss.exp)+ " exp")
            self.exp = self.exp + boss.exp
            self.levelUp()
            self.coins = self.coins + boss.coins
    
    def heal(self):
        print("\nHello Adventurer!")
        print ("I am the nurse! You seemed injured. Let me heal you!")
        self.hitpoints = self.hitpoints + 10
        print("Your health now is " + str(self.hitpoints))
        print()
        
    def purchaseGodSword(self):
        print("\nHello Adventurer!")
        print ("Welcome! Did you wanna purchase the godsword?")
        
        if(self.coins > 100):
            print("You bought the god sword!")
            self.attack + 20
        else: print("You do not have enough. Leave.\n")
    
    def showStatus(self):
        print("Your status is as of follows")
        print("\nLevel:" + str(self.level))
        print("Health:" + str(self.hitpoints))
        print("Attack:" + str(self.attack))
        print("Coins:" + str(self.coins))
        print()

    def levelUp(self):
        if (self.exp > 100):
            print("You leveled up!")
            self.exp = 0
            self.level = self.level + 1 
            self.attack = self.attack + 5
            self.hitpoints = self.hitpoints + 10 
