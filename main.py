from map import TileGrid
from player import Player
import pygame
screen = pygame.display.set_mode((200,250))
grid = TileGrid(screen,4,4)
grid.loadMapData("map1")
player = Player((1,1),"player1.png",grid)

