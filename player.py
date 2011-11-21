import pygame,os
from pygame.locals import *
from main import *

playerStats = {
1: {
    "HP": [20,20],
    "MP": [15,15]
    },
2: {
    "HP": [25,25],
    "MP": [19,19]
    }
               }

# Sprite dict format: ["back": {1: img, 2: img, 3: img}, "left": {1: img, 2: img, 3: img}, 

class Player():
    HP = None
    MP = None
    def __init__(self,loc,sprite="player*png"):
        self.HP = playerStats[self.level]["HP"]
        self.MP = playerStats[self.level]["MP"]
        

    def loadSprites(self,filenameT):
        global sprite

    def dealDamage(self,damage,type="HP"):
        if type == "HP":
            self.HP = (self.HP - damage)
        else:
            return

    def isDead(self):
        if self.HP < 1:
            return True
        else:
            return False


class Anim():
    def __init__(self):
        pass
