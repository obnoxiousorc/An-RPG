from map import TileGrid
import pygame
screen = pygame.display.set_mode((200,200))
grid = TileGrid(screen,4,4)
null = grid.loadImage("null.png")
tree = grid.loadImage("tree.png")
x = grid.loadImage("x.png")
grid.setTile(tree,2,(1,1),(3,1))
grid.setTile(x,1,(1,1),(2,1),(3,1),(4,1))
grid.update()
