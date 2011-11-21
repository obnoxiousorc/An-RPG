from map import TileGrid
import pygame
screen = pygame.display.set_mode((200,250))
grid = TileGrid(screen,4,4)
grid.loadMapData("map1")
