import json
from graphics import *

RESO = 0.1 #Lat Long resolution
NEED = "Power"
MAP_SIZE = 30
LAT = 33.00
LONG = -118.00
SCREEN_RESOLUTION = 1000

def main():
    json_data=open("Data2.json").read()

    data = json.loads(json_data)
    #print(data) 
    win = intialMap(MAP_SIZE)
    grid = fillGrid(LAT,LONG,MAP_SIZE,data, "Food")
    map(win, LAT, LONG, MAP_SIZE, grid,"red")
    #grid = fillGrid(LAT,LONG,MAP_SIZE,data, "Water")
    #map(win, LAT, LONG, MAP_SIZE, grid,"blue")

    win.getMouse()
    win.close()


def fillGrid(lat, long, size, data, need):

    #org = {"severe": 0.00}
    grid = [[0 for x in range(size)] for y in range(size) ]
    # Java syntax --- int[][] grid = new int[size][size];
    #grid = [[org for x in range(size)] for y in range(size) ]

    for x in range(size):
        for y in range(size):
            fdic = float(Jmap("Food", lat+RESO*x, long+RESO*y,data))/float(Jsearch("Food", data, size, lat, long))
            wdic = float(Jmap("Water", lat+RESO*x, long+RESO*y,data))/float(Jsearch("Water", data, size, lat, long))
            pdic = float(Jmap("Power", lat+RESO*x, long+RESO*y,data))/float(Jsearch("Power", data, size, lat, long))
            sdic = float(Jmap("Shelter", lat+RESO*x, long+RESO*y,data))/float(Jsearch("Shelter", data, size, lat, long))
            grid[x][y] = {"Food": fdic, "Water": wdic, "Power": pdic, "Shelter": sdic}

           # grid[x][y] = float(Jmap(need, lat+RESO*x, long+RESO*y,data))/float(total)
    return grid

def intialMap(size):
    win = GraphWin('Floor', SCREEN_RESOLUTION, SCREEN_RESOLUTION)
    myImage = Image(Point(15,15), 'map.PNG')
    myImage.draw(win)
    win.setCoords(0.0, 0.0, size, size)
    win.setBackground(color_rgb(255,255,255))

    # draw grid
    #for x in range(size):
        #for y in range(size):
            #win.plotPixel(x*SCREEN_RESOLUTION/size, y*SCREEN_RESOLUTION/size, "blue")
            #square = Rectangle(Point(x,y), Point(x+1,y+1))
            #square.draw(win)
            #square.setFill("white")
    return win


def map(win, lat, long, size, grid, color):
    for x in range(size):
        for y in range(size):
            if grid[x][y]["Food"] >= 0.00001:
                square = Rectangle(Point(x,y), Point(x+0.5,y+0.5))
                square.draw(win)
                #square.setFill(color_rgb(255,int(127*grid[x][y])+128,int(127*grid[x][y])+128))
                square.setFill("red")
            if grid[x][y]["Water"] >= 0.00001:
                square = Rectangle(Point(x+0.5,y+0.5), Point(x+1,y+1))
                square.draw(win)
                #square.setFill(color_rgb(255,int(127*grid[x][y])+128,int(127*grid[x][y])+128))
                square.setFill("blue")
            if grid[x][y]["Power"] >= 0.00001:
                square = Rectangle(Point(x,y+0.5), Point(x+0.5,y+1))
                square.draw(win)
                #square.setFill(color_rgb(255,int(127*grid[x][y])+128,int(127*grid[x][y])+128))
                square.setFill("yellow")
            if grid[x][y]["Shelter"] >= 0.00001:
                square = Rectangle(Point(x+0.5,y), Point(x+1,y+0.5))
                square.draw(win)
                #square.setFill(color_rgb(255,int(127*grid[x][y])+128,int(127*grid[x][y])+128))
                square.setFill("green")





def Jsearch(resource, data, size, lat, long):
    m = 0
    for ka, va in data.items():
        for inf in va:
            if (inf["Latitude"] > lat and inf["Latitude"] < lat + RESO*size) and (inf["Longitude"] > long and inf["Longitude"] < long + RESO*size):
                if inf[resource]:
                    m = m + 1
    return m

def Jmap(resource, lat, long, data):
    m = 0
    for ka, va in data.items():
        for inf in va:
            if (inf["Latitude"] > lat and inf["Latitude"] < lat + RESO) and (inf["Longitude"] > long and inf["Longitude"] < long + RESO):
                if inf[resource] == True:
                    m = m + 1
    return m

main()