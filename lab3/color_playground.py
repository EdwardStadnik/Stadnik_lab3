from graph import*
from math import*

def distance(x1, y1, x2, y2):
    return ((x2-x1)**2 + (y2-y1)**2)**0.5

def ellipse(x1, y1, x2, y2, a, color_name):
    for i in range( ceil( (x1+x2)*0.5 - a*0.5  ), ceil( (x1+x2)*0.5 + a*0.5 ) ):
        for j in range( ceil( (y1+y2)*0.5 - a*0.5 ), ceil( (y1+y2)*0.5 + a*0.5 ) ):
            if ( (distance(x1, y1, i, j) + distance(x2, y2, i, j)) <= a ):
                point(i, j, color_name)

windowSize(500, 600)

def ellipse_color_gradient():
    ellipse(100, 100, 200, 200, 150,(i,j,k) )




run()