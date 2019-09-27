from graph import *
from math import*

xSize=400
ySize=565
windowSize(xSize,ySize)


new_i = 0
new_z = 255

def animalLeg(k, r, x0, y0):
    ellyps(x0-13*k*r, y0+0*k, x0+13*k*r, y0+60*k)
    ellyps(x0-13*k*r, y0+55*k, x0+13*k*r, y0+115*k)
    ellyps(x0-5*k*r, y0+110*k, x0+25*k*r, y0+130*k)

def animal(k, r, x0, y0, i, j, z):
    xmid=97
    ymid=371
    i = int(i)
    j = int(j)
    z = int(z)
    penColor(i,j,z)
    brushColor(i,j,z)
    ellyps(x0+100*k*r, y0+40*k, x0-100*k*r, y0-40*k)
    ellyps(x0+75*k*r, y0-5*k, x0+115*k*r, y0-120*k)
    ellyps(x0+85*k*r, y0-145*k, x0+135*k*r, y0-115*k)
    penColor(229,128,255)
    brushColor(229,128,255)
    circle(x0+105*k*r, y0-132*k, 10*k)
    penColor(255 - i,255 - j,255 - z)
    brushColor(255 - i,255 - j,255 - z)
    circle(x0+108*k*r, y0-132*k, 5*k)
    penColor(i,j,z)
    brushColor(i,j,z)
    ellyps(x0+98*k*r, y0-140*k, x0+108*k*r, y0-136*k)
    penSize(6*k)
    line(x0+90*k*r, y0-130*k, x0+70*k*r, y0-153*k)
    line(x0+95*k*r, y0-135*k, x0+78*k*r, y0-158*k)
    penSize(1)
    penColor(i,j,z)
    brushColor(i,j,z)
    animalLeg(k, r, x0+80*k*r, y0+20*k)
    animalLeg(k, r, x0+50*k*r, y0-10*k)
    animalLeg(k, r, x0-40*k*r, y0+20*k)
    animalLeg(k, r, x0-80*k*r, y0-10*k)

def progressive_animal_painting():
    j = 0
    k = 0.55
    r = -1
    x0 = 94
    y0 = 363
    global new_i
    global new_z
    if new_i < 255:
        new_i += 1
    if new_z > 0:
        new_z -= 1
    animal(k, r, x0, y0, new_i, j, new_z)


def flower(k, r, x0, y0, delta_y):
    penColor(150,150,150)
    brushColor(255,255,255)
    tmpx=-1
    tmpy=-7
    ellyps(x0+(10+tmpx)*k*r, y0+(delta_y+tmpy)*k, x0-(10-tmpx)*k*r, y0-(delta_y-tmpy)*k)
    tmpx=-10
    tmpy=-4
    ellyps(x0+(10+tmpx)*k*r, y0+(delta_y+tmpy)*k, x0-(10-tmpx)*k*r, y0-(delta_y-tmpy)*k)
    tmpx=10
    tmpy=-5
    ellyps(x0+(10+tmpx)*k*r, y0+(delta_y+tmpy)*k, x0-(10-tmpx)*k*r, y0-(delta_y-tmpy)*k)
    penColor(255,255,0)
    brushColor(255,255,0)
    tmpx=0
    tmpy=0
    ellyps(x0+(10+tmpx)*k*r, y0+(delta_y+tmpy)*k, x0-(10-tmpx)*k*r, y0-(delta_y-tmpy)*k)
    penColor(150,150,150)
    brushColor(255,255,255)
    tmpx=13
    tmpy=0
    ellyps(x0+(10+tmpx)*k*r, y0+(delta_y+tmpy)*k, x0-(10-tmpx)*k*r, y0-(delta_y-tmpy)*k)
    tmpx=-15
    tmpy=2
    ellyps(x0+(10+tmpx)*k*r, y0+(delta_y+tmpy)*k, x0-(10-tmpx)*k*r, y0-(delta_y-tmpy)*k)
    tmpx=-7
    tmpy=5
    ellyps(x0+(10+tmpx)*k*r, y0+(delta_y+tmpy)*k, x0-(10-tmpx)*k*r, y0-(delta_y-tmpy)*k)
    tmpx=7
    tmpy=6
    ellyps(x0+(10+tmpx)*k*r, y0+(delta_y+tmpy)*k, x0-(10-tmpx)*k*r, y0-(delta_y-tmpy)*k)

def kustik(k, r, x0, y0):
    penColor(113,200,55)
    brushColor(113,200,55)
    circle(x0, y0, 75*k)
    c1=3/6
    c2=4/6
    c3=5/6
    flower(k*c2, r, x0+5*k*r, y0-55*k, 5)
    flower(k*c1, -r, x0-40*k*r, y0-43*k, 5)
    flower(k*c2, -r, x0-28*k*r, y0-14*k, 5)
    flower(k*c3, r, x0+40*k*r, y0-26*k, 5)
    flower(k*c3, r, x0+6*k*r, y0+19*k, 5)
    flower(k*c2, r, x0+50*k*r, y0+16*k, 5)



def mountains():
    penColor(175,221,233)
    brushColor(175,221,233)
    rectangle(0, 0, xSize, ySize)
    
    penColor(0,0,0)
    brushColor(179,179,179)
    polygon([(0,174), (49,58), (83,138), (137,75), (238,226), (311,70), (335,98), (400,21), (xSize,ySize), (0,ySize)])
    
    penColor(0,0,0)
    brushColor(170,222,135)
    polygon([(0,300), (20,290), (35,289), (49,289), (86,283), (210,283), (212,284), (217,284), (221,290), (221,300), (224,302), (224,330), (233,333), (xSize,333), (xSize,ySize), (0,ySize)])

    global new_i

mountains()

kustik(1.05, 1, 335, 460)

onTimer(progressive_animal_painting, 10)

flower(1, 1, 100, 500, 2)
flower(1, 1, 160, 500, 2)
flower(1, 1, 200, 500, 2)


run()