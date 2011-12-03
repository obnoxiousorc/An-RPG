import pygame
from prefs import *

class Player():
    def __init__(self,screen,imagename="player"):
        self.frames = dict()
        self.loadFrames(imagename)
        self.screen = screen
        self.clock = pygame.time.Clock()

    def loadFrames(self,imageBase,num=4):
        path = dirs["sprites"]
        try:
            self.frames[1] = pygame.image.load(path+imageBase+"1.png")
            self.frames[2] = pygame.image.load(path+imageBase+"2.png")
            self.frames[3] = pygame.image.load(path+imageBase+"3.png")
            self.frames[4] = pygame.image.load(path+imageBase+"4.png")
        except:
            print "Error loading player sprites."



    def playAnim(self,duration): # Play animation for {duration} seconds.
        f = 1
        for frame in range(duration*8):
            self.screen.fill((0,0,0))
            self.screen.blit(self.frames[f],(0,0))
            pygame.display.update()
            print f
            if f < 4:
                f += 1
            else:
                f = 1
            self.clock.tick(8)
