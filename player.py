import pygame
from prefs import *

# Planned sprite dict format: ["back": {1: img, 2: img, 3: img}, "left": {1: img, 2: img, 3: img}, etc.
#                                       ^       ^       ^--- Frames for animation

class Player():
    HP = None
    MP = None
    level = 1
    currentLoc = (0,0)
    def __init__(self,loc,sprite="player1.png"):
        self.HP = playerStats[self.level]["HP"]
        self.MP = playerStats[self.level]["MP"]
        self.loadSprites(sprite)
        currentLoc = loc

    def loadSprites(self,filenameT):
        global sprite
        self.sprite = pygame.image.load(dirs["sprites"] + filenameT)

    def dealDamage(self,damage,type="HP"):
        if type == "HP":
            self.HP[1] = (self.HP[1] - damage)
        else:
            return

    def isDead(self):
        if self.HP[1] < 1:
            return True
        else:
            return False

    def getStats(self): # Return the player's stats, as {"HP":(max,current),"MP":(max,current),} and more when there's more, like skill levels
        stats = {"HP": self.HP, "MP": self.MP}
        return stats

    def move(self,direction):
        if direction == "n":
            # Put animation function here
            self.currentLoc = (self.currentLoc[0],self.currentLoc[1]+1)

class Animator():
    def __init__(self):
        pass
