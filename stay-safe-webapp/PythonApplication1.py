import json
import sys
from graphics import *

RESO = 0.1                  #Lat Long resolution
MAP_SIZE = 30               #Sq of map size displayed
LAT = 33.00                 #Latitude of Map visual
LONG = -118.00              #Longitude of Map Visual
SCREEN_RESOLUTION = 1000    #Size of screen visualization
arg = ['1','1','0','0']     #Arguments to control what needs will be shown

def main():
    json_data=open("Data2.json").read()

    data = json.loads(json_data)

    win = intialMap(MAP_SIZE)
    grid = fillGrid(LAT,LONG,MAP_SIZE,data)
    map(win, LAT, LONG, MAP_SIZE, grid,"red")

    win.getMouse()
    win.close()


def fillGrid(lat, long, size, data):

    grid = [[0 for x in range(size)] for y in range(size) ]

    for x in range(size):
        for y in range(size):
            fdic = float(Jmap("Food", lat+RESO*x, long+RESO*y,data))/float(Jsearch("Food", data, size, lat, long))
            wdic = float(Jmap("Water", lat+RESO*x, long+RESO*y,data))/float(Jsearch("Water", data, size, lat, long))
            pdic = float(Jmap("Power", lat+RESO*x, long+RESO*y,data))/float(Jsearch("Power", data, size, lat, long))
            sdic = float(Jmap("Shelter", lat+RESO*x, long+RESO*y,data))/float(Jsearch("Shelter", data, size, lat, long))
            grid[x][y] = {"Food": fdic, "Water": wdic, "Power": pdic, "Shelter": sdic}

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
            if grid[x][y]["Food"] >= 0.00001 and arg[0] == '1':
                square = Rectangle(Point(x,y), Point(x+0.5,y+0.5))
                square.draw(win)
                square.setFill("red")

            if grid[x][y]["Water"] >= 0.00001 and arg[1] == '1':
                square = Rectangle(Point(x+0.5,y), Point(x+1,y+0.5))
                square.draw(win)
                square.setFill("blue")

            if grid[x][y]["Power"] >= 0.00001 and arg[2] == '1':
                square = Rectangle(Point(x,y+0.5), Point(x+0.5,y+1))
                square.draw(win)
                square.setFill("yellow")

            if grid[x][y]["Shelter"] >= 0.00001 and arg[3] == '1':
                square = Rectangle(Point(x+0.5,y+0.5), Point(x+1,y+1))
                square.draw(win)
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