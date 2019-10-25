from tkinter import *
from random import randrange as rnd, choice
from time import *
root = Tk()
root.geometry('800x600')

canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

textt = canv.create_text(400, 250,
                         text="Click Right Mouse Button to\nSTART THE GAME",
                         justify=CENTER, font="Impact 40")

textt = canv.create_text(400, 350, text="tap on circles = 1",
                         justify=CENTER, font="Impact 20", fill="grey")

textt = canv.create_text(400, 400, text="tap on rectangle = 20",
                         justify=CENTER, font="Impact 20", fill="grey")

textt = canv.create_text(400, 450, text="<Esc> to stop the game",
                         justify=CENTER, font="Impact 20", fill="black")

balls = []

def delete_ball():
#    balls.reverse()
    canv.delete(balls[0])
    balls.remove(balls[0])
#    balls.reverse()

def new_ball():
    #canv.delete(ALL)
    b = {'x': rnd(100,700), 'y': rnd(100,500), 'r': rnd(30,50),
             'x_velocity': rnd(-5, 5), 'y_velocity': rnd(-5, 5),
             'x_acceleration': rnd(-2, 2), 'y_acceleration': rnd(-1, 1),
             'clicked': False}
    ball = canv.create_oval(b['x'] - b['r'],
                            b['y'] - b['r'],
                            b['x'] + b['r'],
                            b['y'] + b['r'],
                            fill=choice(colors), width=0)
    balls.append(ball)

    root.after(5000, delete_ball)
    root.after(500, new_ball)



def click(event):
    print('click')

new_ball()
canv.bind('<Button-1>', click)
mainloop()