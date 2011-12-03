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
nullTile = None
screen = None

class MapData():
    def __init__(self):
        pass

class TileGrid(MapData):
    def __init__(self, scr, sX=8, sY=8):
        global xSize,ySize,nullTile
        nullTile = self.loadImage("null.png")
        self.grid = dict()
        self.ySize = sY
        self.xSize = sX
        self.screen = scr
        x = 1
        y = 1
        for i in range(sX):
            for i in range(sY):
                self.grid[(x,y)] = dict()
                self.grid[(x,y)][1] = nullTile
                self.grid[(x,y)][2] = nullTile
                self.grid[(x,y)][3] = nullTile
                self.setWalkable(True,(x,y))
                self.grid[(x,y)]["coords"] = ((x*tileSize)-25,(y*tileSize)-25)
                y += 1
            y = 1
            x += 1

    def getCoords(self,loc):
        return self.grid[loc]["coords"]

    def setWalkable(self,value,loc,*args):
        self.grid[loc]["walkable"] = value
        if len(args) > 0:
            for loc1 in args:
                self.grid[loc1]["walkable"] = value

    def isWalkable(self,coords):
        for loc in self.grid:
            if coords[0] < (self.grid[loc]["coords"][0]+25) and coords[0] >= self.grid[loc]["coords"][0]:   # Check if current coordinates are within this block.
                if coords[1] < (self.grid[loc]["coords"][1]+25) and coords[1] >= self.grid[loc]["coords"][1]: 
                    return self.grid[loc]["walkable"]

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
        for tile in self.grid:
            imagename = globals()[id(self.grid[tile][1])]
            savedGrid[tile] = self.grid[tile]
            savedGrid[tile][1] = globals()[id(self.grid[tile][1])]
            savedGrid[tile][2] = globals()[id(self.grid[tile][2])]
            savedGrid[tile][3] = globals()[id(self.grid[tile][3])]
        mapFile = open(dirs["maps"] + mapname + ".py", 'w')
        mapFile.write('grid = ' + repr(savedGrid) + '\n')
        mapFile.write('size = ' + str((self.xSize,self.ySize)) + '\n')
        mapFile.close()
        print "Map saved."

    def loadMapData(self,mapname):
        if not os.path.exists(dirs["maps"] + mapname + ".py"):
            print "No such map."
            return
        try:
            sys.path.insert(0, dirs["maps"])
            mapImport = __import__(mapname)
        except:
            print "ERROR; import of " + mapname + " failed."
            return
        self.grid = mapImport.grid
        for tile in self.grid:
            self.grid[tile][1] = self.loadImage(self.grid[tile][1])
            self.grid[tile][2] = self.loadImage(self.grid[tile][2])
            self.grid[tile][3] = self.loadImage(self.grid[tile][3])
        self.update()
            

    def setTile(self,image,layer=2,firstLoc=(1,1),*args):
        self.grid[firstLoc][layer] = image
        if len(args) > 0:
            for loc in args:
                self.grid[loc][layer] = image
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
        for tile in grid:
            self.grid[tile][layer] = image
        self.update()

    def update(self):
        for tile in self.grid:
            loc = self.getCoords(tile)
            self.screen.blit(self.grid[tile][1],loc)
            self.screen.blit(self.grid[tile][2],loc)
            self.screen.blit(self.grid[tile][3],loc)
