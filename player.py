import pygame
from prefs import *

# Planned sprite dict format: ["back": {1: img, 2: img, 3: img, 4: img}, "left": {1: img, 2: img, 3: img, 4: img}, etc.
#                                       ^       ^       ^--- Frames for animation

class Player():
    HP = None
    MP = None
    level = 1
    def __init__(self,loc,sprite,gridx):
        self.grid = gridx
        self.HP = playerStats[self.level]["HP"]
        self.MP = playerStats[self.level]["MP"]
        self.sprite = dict()
        self.loadSprites(sprite)
        self.currentLoc = loc
        self.oldLoc = loc
        self.currentFrame = 1
        self.currentFrameImg = self.sprite[1]
        self.clock = pygame.time.Clock()

    def loadSprites(self,fNameBase):
        path = dirs["sprites"]
        self.sprite[1] = pygame.image.load(path+fNameBase+"1.png")
        self.sprite[2] = pygame.image.load(path+fNameBase+"2.png")
        self.sprite[3] = pygame.image.load(path+fNameBase+"3.png")
        self.sprite[4] = pygame.image.load(path+fNameBase+"4.png")

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

    def getNextFrame(self):
        if self.currentFrame < 4:
            self.currentFrame += 1
        else:
            self.currentFrame = 1
        return self.sprite[self.currentFrame]

    def move(self,direction):
        if direction == "n":
            newLoc = (self.currentLoc[0],self.currentLoc[1]-3)
            if self.currentLoc[1] > 1: 
                if self.grid.isWalkable(newLoc):
                    self.currentLoc = newLoc
        elif direction == "s":
            newLoc = (self.currentLoc[0],self.currentLoc[1]+3)
            if self.currentLoc[1] < self.grid.ySize*25: 
                if self.grid.isWalkable(newLoc):
                    self.currentLoc = newLoc
        elif direction == "w":
            newLoc = (self.currentLoc[0]-3,self.currentLoc[1])
            if self.currentLoc[0] > 1: 
                if self.grid.isWalkable(newLoc): 
                    self.currentLoc = newLoc
        elif direction == "e":
            newLoc = (self.currentLoc[0]+3,self.currentLoc[1])
            if (self.currentLoc[0] < self.grid.xSize*25): 
                if self.grid.isWalkable(newLoc): 
                    self.currentLoc = newLoc

    def getLoc(self):
        return self.currentLoc

    def draw(self):
        if self.oldLoc != self.currentLoc: self.currentFrameImg = self.getNextFrame()
        self.grid.screen.blit(self.currentFrameImg,self.currentLoc)
        pygame.display.update()
        self.oldLoc = self.currentLoc
