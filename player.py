import pygame
from prefs import *

# Planned sprite dict format: ["back": {1: img, 2: img, 3: img}, "left": {1: img, 2: img, 3: img}, etc.
#                                       ^       ^       ^--- Frames for animation

class Player():
    HP = None
    MP = None
    level = 1
    currentLoc = (1,1)
    def __init__(self,loc,sprite,gridx):
        self.grid = gridx
        self.HP = playerStats[self.level]["HP"]
        self.MP = playerStats[self.level]["MP"]
        self.loadSprites(sprite)
        self.currentLoc = loc

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
            if self.currentLoc[1] > 1: self.currentLoc = (self.currentLoc[0],self.currentLoc[1]-1)
        elif direction == "s":
            if self.currentLoc[1] <= self.grid.ySize: self.currentLoc = (self.currentLoc[0],self.currentLoc[1]+1)
        elif direction == "w":
            if self.currentLoc[0] > 1: self.currentLoc = (self.currentLoc[0]-1,self.currentLoc[1])
        elif direction == "e":
            if (self.currentLoc[0] <= self.grid.xSize): self.currentLoc = (self.currentLoc[0]+1,self.currentLoc[1])

    def getLoc(self):
        return self.currentLoc

    def draw(self):
        coords = self.grid.getCoords(self.currentLoc)
        self.grid.screen.blit(self.sprite,coords)
        pygame.display.update()

class Animator():
    def __init__(self):
        pass
