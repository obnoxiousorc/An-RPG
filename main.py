import pygame, sys
from map import TileGrid
from player import Player
from pygame.locals import *
screen = pygame.display.set_mode((200,250))
grid = TileGrid(screen)
grid.loadMapData("map1")
player = Player((2,2),"player1.png",grid)
player.draw()
clock = pygame.time.Clock()

def game():
    while 1:
        for event in pygame.event.get():
              if event.type == KEYDOWN:
                  if event.key == K_UP:
                      player.move("n")
                  elif event.key == K_LEFT:
                      player.move("w")
                  elif event.key == K_RIGHT:
                      player.move("e")
                  elif event.key == K_DOWN:
                      player.move("s")
                  elif event.key == K_ESCAPE:
                      sys.exit()
        grid.update()
        player.draw()
        pygame.display.update()
        clock.tick(30)
