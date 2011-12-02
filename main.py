from map import TileGrid
from player import Player
import pygame
from pygame.locals import *
screen = pygame.display.set_mode((200,250))
grid = TileGrid(screen,4,4)
grid.loadMapData("map1")
player = Player((1,1),"player1.png",grid)
player.draw()
clock = pygame.time.Clock()

while 1:
    for event in pygame.event.get():
          if event.type == KEYDOWN and event.key == K_DOWN:
              player.move("s")
    grid.update()
    player.draw()
