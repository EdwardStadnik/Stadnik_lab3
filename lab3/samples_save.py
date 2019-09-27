from graph import*
from math import*

def distance(x1, y1, x2, y2):
    return ((x2-x1)**2 + (y2-y1)**2)**0.5

def ellipse(x1, y1, x2, y2, a, color_name):
    l = distance(x1, y1, x2, y2)
    for i in range( ceil( (x1+x2)*0.5 - a*0.5  ), ceil( (x1+x2)*0.5 + a*0.5 ) ):
        for j in range( ceil( (y1+y2)*0.5 - a*0.5 ), ceil( (y1+y2)*0.5 + a*0.5 ) ):
            if ( (distance(x1, y1, i, j) + distance(x2, y2, i, j)) <= a ):
                point(i, j, color_name)

def right_wing(x1, y1, k):
    x2 = x1 + 5*k
    y2 = y1 + 4*k
    x3 = x2 + 4*k
    y3 = y2 + 2*k
    x4 = x3 + 7*k
    y4 = y3 + 1*k
    x5 = x4 + 8*k
    y5 = y4 - 2*k
    x6 = x5 + 5*k
    y6 = y5 + 4*k
    x7 = x6 + 3*k
    y7 = y6 + 7*k
    x8 = x7 - 8*k
    y8 = y7 + 5*k
    x9 = x8 - 4*k
    y9 = y8 - 2*k
    x10 = x9 - 2*k
    y10 = y9 - 5*k
    x11 = x10 - 12*k
    y11 = y10 - 4*k
    points = [[x1, y1], [x2, y2], [x3, y3], [x4, y4], [x5, y5], [x6, y6], [x7, y7], [x8, y8], [x9, y9], [x10, y10], [x11, y11]]
    polygon(points)

def left_wing(x1, y1, k):
    x2 = x1 + 1*k
    y2 = y1 + 5*k
    x3 = x2 + 3*k
    y3 = y2 + 4*k
    x4 = x3 + 6*k
    y4 = y3 + 4*k
    x5 = x4 + 8*k
    y5 = y4 + 2*k
    x6 = x5 + 3*k
    y6 = y5 + 5*k
    x7 = x6 - 1*k
    y7 = y6 + 8*k
    x8 = x7 - 9*k
    y8 = y7 + 0*k
    x9 = x8 - 3*k
    y9 = y8 - 3*k
    x10 = x9 - 0*k
    y10 = y9 - 5*k
    x11 = x10 - 9*k
    y11 = y10 - 9*k
    points = [[x1, y1], [x2, y2], [x3, y3], [x4, y4], [x5, y5], [x6, y6], [x7, y7], [x8, y8], [x9, y9], [x10, y10], [x11, y11]]
    polygon(points)

def tale(x1, y1, k):
    points = [[x1+14*k, y1+15*k], [x1+25*k, y1+25*k], [x1+10*k, y1+23*k]]
    polygon(points)

def leg(x1, y1, k):
    ellipse(x1, y1, x1+5*k, y1+8*k, 1.3*distance(x1, y1, x1+5*k, y1+8*k), 'white')
    ellipse(x1+5*k, y1+8*k, x1+3*k+11*k, y1+6*k+3*k, 1.2*distance(x1+5*k, y1+8*k, x1+3*k+11*k, y1+6*k+3*k), 'white')
    points = [[(x1+14*k), (y1+9*k)], [(x1+22*k), (y1+8*k)], [(x1+17*k), (y1+6*k)], [(x1+23*k), (y1+7*k)], [(x1+17*k), (y1+7*k)], [(x1+21*k), (y1+10*k)], [(x1+16*k), (y1+7*k)], [(x1+12*k), (y1+10*k)]]
    polygon(points)

def albatros_suka(x1, y1, k):
    brushColor('white')
    left_wing(x1 + 17 * k, y1 - 9 * k, k)
    right_wing(x1, y1, k)
    tale(x1, y1, k)
    leg(x1+32*k, y1+28*k, k)
    ellipse(x1+22*k, y1+22*k, x1+22*k+26*k, y1+22*k, 29*k, 'white')
    ellipse(x1+22*k+26*k, y1+22*k, x1+22*k+26*k+8*k, y1+22*k, 10*k, 'white')

windowSize(500, 600)

penSize(0)

#Фон рисунка
brushColor(25, 25, 112)
rectangle(0, 0, 500, 90)
brushColor(123, 104, 238)
rectangle(0, 0+90, 500, 90+40)
brushColor(221, 160, 221)
rectangle(0, 0+90+40, 500, 90+40+70)
brushColor(238, 130, 238)
rectangle(0, 0+90+40+70, 500, 90+40+70+100)
brushColor(255, 160, 122)
rectangle(0, 0+90+40+70+100, 500, 90+40+70+100+50)
brushColor(70, 130, 180)
rectangle(0, 0+90+40+70+100+50, 500, 90+40+70+100+50+250)

albatros_suka(40, 350, 5)

run()