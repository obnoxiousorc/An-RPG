import pygame, sys
from map import TileGrid
from player import Player
from pygame.locals import *
screen = pygame.display.set_mode((200,250))
grid = TileGrid(screen)
grid.loadMapData("map1")
player = Player((26,26),"player",grid)
player.draw()
clock = pygame.time.Clock()
pressed = dict()
pressed["up"] = False
pressed["left"] = False
pressed["right"] = False
pressed["down"] = False

def game():
    while 1: 
        for event in pygame.event.get():
              if event.type == KEYDOWN:
                  if event.key in [K_UP, K_k]:
                      pressed["up"] = True
                  elif event.key in [K_LEFT, K_h]:
                      pressed["left"] = True
                  elif event.key in [K_RIGHT, K_l]:
                      pressed["right"] = True
                  elif event.key in [K_DOWN, K_j]:
                      pressed["down"] = True
                  elif event.key == K_ESCAPE:
                      print "Exit"
                      sys.exit()
              elif event.type == KEYUP:
                  if event.key in [K_UP, K_k]:
                      pressed["up"] = False
                  elif event.key in [K_LEFT, K_h]:
                      pressed["left"] = False
                  elif event.key in [K_RIGHT, K_l]:
                      pressed["right"] = False
                  elif event.key in [K_DOWN, K_j]:
                      pressed["down"] = False
        
        if pressed["up"]:
            player.move("n")
        if pressed["left"]:
            player.move("w")
        if pressed["right"]:
            player.move("e")
        if pressed["down"]:
            player.move("s")
                  
        grid.update()
        player.draw()
        pygame.display.update()
        clock.tick(10)
