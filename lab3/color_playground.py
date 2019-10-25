from graph import*
from math import*

def distance(x1, y1, x2, y2):
    return ((x2-x1)**2 + (y2-y1)**2)**0.5

def ellipse(x1, y1, x2, y2, a, color_name):
    for i in range( ceil( (x1+x2)*0.5 - a*0.5  ), ceil( (x1+x2)*0.5 + a*0.5 ) ):
        for j in range( ceil( (y1+y2)*0.5 - a*0.5 ), ceil( (y1+y2)*0.5 + a*0.5 ) ):
            if ( (distance(x1, y1, i, j) + distance(x2, y2, i, j)) <= a ):
                point(i, j, color_name)

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

windowSize(1000, 800)
canvasSize(1000, 800)

ellipse(500, 500, 600, 600, 150, 'purple')

pos = [[100, 100], [200, 100], [300, 150], [200, 200], [100, 200], [0, 150]]
link = polygon(pos)
deleteObject(link)

run()