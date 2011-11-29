# Grid tile format: {"coords": (0,0), 1: grass, 2: tree, 3: None, "walkable": False}
#                    ^ X and Y location on the screen
#                                     ^ tile to be drawn first
#                                               ^ tile to be drawn second
#                                                        ^ tile to be drawn last. Should mostly be either small overhangs, backs of buildings, fog, etc.
#                                                                 ^ Whether the player can walk on this location.
# Note: "grass" and "tree" should be links to the actual image object.

import pygame,os,sys
from prefs import *
tileSize = 25
grid = {}
nullTile = None
screen = None

class MapData():
    def __init__(self):
        pass

class TileGrid(MapData):
    def __init__(self, scr, sX=8, sY=8):
        global grid,xSize,ySize,screen,nullTile
        nullTile = self.loadImage("null.png")
        self.ySize = sY
        self.xSize = sX
        screen = scr
        x = 1
        y = 1
        for i in range(sX):
            for i in range(sY):
                grid[(x,y)] = dict()
                grid[(x,y)][1] = nullTile
                grid[(x,y)][2] = nullTile
                grid[(x,y)][3] = nullTile
                grid[(x,y)]["walkable"] = True
                grid[(x,y)]["coords"] = ((x*tileSize)-25,(y*tileSize)-25)
                y += 1
            y = 1
            x += 1

    def getCoords(self,loc):
        return grid[loc]["coords"]

    def loadImage(self,imagename):
        if not os.path.exists(dirs["tiles"] + imagename):
            print "Error: image does not exist."
            return
        try:
            image = pygame.image.load(dirs["tiles"] + imagename)
            globals()[id(image)] = imagename
        except:
            print "Error loading image."
            return
        return image

    def saveMapData(self,mapname):
        if os.path.exists(dirs["maps"] + mapname + ".py"):
            print "File exists. Write anyway?"
            answer = raw_input()
            if not answer.startswith(("y","Y")):
                print "Map not saved."
                return
        savedGrid = {}
        for tile in grid:
            imagename = globals()[id(grid[tile][1])]
            savedGrid[tile] = grid[tile]
            savedGrid[tile][1] = globals()[id(grid[tile][1])]
            savedGrid[tile][2] = globals()[id(grid[tile][2])]
            savedGrid[tile][3] = globals()[id(grid[tile][3])]
        mapFile = open(dirs["maps"] + mapname + ".py", 'w')
        mapFile.write('grid = ' + repr(savedGrid) + '\n')
        mapFile.write('size = ' + str((xSize,ySize)) + '\n')
        mapFile.close()
        print "Map saved."

    def getWalkable(self,tile):
        return grid[tile]["walkable"]

    def loadMapData(self,mapname):
        global grid, screen
        if not os.path.exists(dirs["maps"] + mapname + ".py"):
            print "No such map."
            return
        try:
            sys.path.insert(0, dirs["maps"])
            mapImport = __import__(mapname)
        except:
            print "ERROR; import of " + mapname + " failed."
            return
        grid = mapImport.grid
        for tile in grid:
            grid[tile][1] = self.loadImage(grid[tile][1])
            grid[tile][2] = self.loadImage(grid[tile][2])
            grid[tile][3] = self.loadImage(grid[tile][3])
        self.update()
            

    def setTile(self,image,layer=2,firstLoc=(1,1),*args):
        global screen,grid
        grid[firstLoc][layer] = image
        if len(args) > 0:
            for loc in args:
                grid[loc][layer] = image
        self.update()

    def drawLine(self,image,axis,value):
        if axis == "x":
            for x in range(xSize):
                self.setTile(image,value,x+1)
        elif axis =="y":
            for y in range(ySize):
                self.setTile(image,y+1,value)
        else: print "ERROR"

    def fill(self,image,layer):
        global screen
        for tile in grid:
            grid[tile][layer] = image
        self.update()

    def update(self):
        global screen
        screen.fill((0,0,0))
        for tile in grid:
            loc = self.getCoords(tile)
            screen.blit(grid[tile][1],loc)
            screen.blit(grid[tile][2],loc)
            screen.blit(grid[tile][3],loc)
        pygame.display.update()
