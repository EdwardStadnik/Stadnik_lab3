from tkinter import *
from random import randrange as rnd, choice
from time import *

root = Tk()
root.geometry('800x600')

canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)

textt = canv.create_text(400, 250,
                         text="Click Right Mouse Button to\nSTART THE GAME",
                         justify=CENTER, font="Impact 40")
textt = canv.create_text(400, 450, text="<Esc> to stop the game",
                         justify=CENTER, font="Impact 20", fill="black")



colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

balls = []
balls_info = []
start = False
finish = False
points = 0


def delete_ball():
    canv.delete(balls[0])
    balls.remove(balls[0])
    print(balls_info[0])
    balls_info.remove(balls_info[0])

def new_ball():
    global balls
    global balls_info
    b = {'x': rnd(100,700), 'y': rnd(100,500), 'r': rnd(30,50),
             'x_velocity': rnd(-20, 20), 'y_velocity': rnd(-15, 15),
             'x_acceleration': 0, 'y_acceleration': 0}
    ball = canv.create_oval(b['x'] - b['r'],
                            b['y'] - b['r'],
                            b['x'] + b['r'],
                            b['y'] + b['r'],
                            fill=choice(colors), width=0)
    balls.append(ball)
    balls_info.append(b)
    if not finish:
        root.after(5000, delete_ball)
        root.after(1000, new_ball)

def click(event):
    print('click')

def movement_cycle():
    global start
    global balls
    global balls_info
    if start:
        for i in range(1, len(balls)):
            canv.move(balls[i], balls_info[i]['x_velocity'], balls_info[i]['y_velocity'])
            balls_info[i]['x'] += balls_info[i]['x_velocity']
            balls_info[i]['y'] += balls_info[i]['y_velocity']
            balls_info[i]['x_velocity'] += balls_info[i]['x_acceleration']
            balls_info[i]['y_velocity'] += balls_info[i]['y_acceleration']
    if not finish:
        root.after(50, movement_cycle)

def hit_check():
    global finish
    for i in range(0, len(balls_info)):
        if ((balls_info[i]['x'] > 0) and (balls_info[i]['x'] - balls_info[i]['r'] < 0)) or ((balls_info[i]['x'] < 800) and (balls_info[i]['x'] + balls_info[i]['r'] > 800)):
            balls_info[i]['x_velocity'] = -balls_info[i]['x_velocity']
            balls_info[i]['x_acceleration'] = -balls_info[i]['x_acceleration']
        if ((balls_info[i]['y'] > 0) and (balls_info[i]['y'] - balls_info[i]['r'] < 0)) or ((balls_info[i]['y'] < 600) and (balls_info[i]['y'] + balls_info[i]['r'] > 600)):
            balls_info[i]['y_velocity'] = -balls_info[i]['y_velocity']
            balls_info[i]['y_acceleration'] = -balls_info[i]['y_acceleration']
    if not finish:
        root.after(20, hit_check)

def click(event):
    global points, finish
    if not finish:
        for i in range(0, len(balls_info)):
            if (((balls_info[i]['x'] - event.x) ** 2 + (balls_info[i]['y'] - event.y) ** 2) ** 0.5 <= balls_info[i]['r']):
                points += 1
                canv.delete(balls[i])
                balls.remove(balls[i])
                balls_info.remove(balls_info[i])

def Game_start(event):
    global start
    if not start :
        start = True
        if not finish:
            canv.delete(ALL)
            new_ball()
            movement_cycle()
            hit_check()

def Game_stop(event):
    global finish
    if not finish :
        finish = True
        root.after(100, canv.delete(ALL))
        textt = canv.create_text(400, 250, text="GAME OVER", justify=CENTER, font="Impact 40")



canv.bind('<Button-3>', Game_start)
canv.bind('<Button-1>', click)
root.bind('<Escape>', Game_stop)

mainloop()