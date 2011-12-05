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
        for img in range(16):
            self.sprite[img+1] = pygame.image.load(path+fNameBase+str(img+1)+".png")
        

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
        key = self.currentFrame+(self.direction*4)
        return self.sprite[key]

    def move(self,direction):
        if direction == "n":
            newLoc = (self.currentLoc[0],self.currentLoc[1]-3)
            if self.currentLoc[1] > 1: 
                if self.grid.isWalkable(newLoc):
                    self.currentLoc = newLoc
                    self.setDirection("n")
        elif direction == "s":
            newLoc = (self.currentLoc[0],self.currentLoc[1]+3)
            if self.currentLoc[1] < self.grid.ySize*25: 
                if self.grid.isWalkable(newLoc):
                    self.setDirection("s")
                    self.currentLoc = newLoc
        elif direction == "w":
            newLoc = (self.currentLoc[0]-3,self.currentLoc[1])
            if self.currentLoc[0] > 1: 
                if self.grid.isWalkable(newLoc): 
                    self.setDirection("w")
                    self.currentLoc = newLoc
        elif direction == "e":
            newLoc = (self.currentLoc[0]+3,self.currentLoc[1])
            if (self.currentLoc[0] < self.grid.xSize*25): 
                if self.grid.isWalkable(newLoc): 
                    self.setDirection("e")
                    self.currentLoc = newLoc

    def setDirection(self,direction):
        if direction == "s":
            self.direction = 0
        elif direction == "n":
            self.direction = 1
        elif direction == "w":
            self.direction = 2
        elif direction == "e":
            self.direction = 3

    def getLoc(self):
        return self.currentLoc

    def draw(self):
        if self.oldLoc != self.currentLoc: self.currentFrameImg = self.getNextFrame()
        self.grid.screen.blit(self.currentFrameImg,self.currentLoc)
        pygame.display.update()
        self.oldLoc = self.currentLoc
