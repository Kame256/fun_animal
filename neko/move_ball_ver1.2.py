import tkinter as tk
import os, sys, time
import random
import math

width=1280
height=720
root=tk.Tk()
root.geometry("1280x700")
root.title("move ball")
# キャンバス
canvas = tk.Canvas(root,bg="white", width = 1279, height = 691)
canvas.place(x=0, y=0)
# オブジェクト

#初期値
y=10
x=10
dx=1
dy=1
log_dx=dx
log_dy=dy
size=140
speed=1
random_angle=log_angle=45
rand_list=[x for x in range(1,180) if x%10==0]
#動かす
while 1:
    time.sleep(1/500)
    x=x+math.sin(math.radians(random_angle))*speed
    y=y+math.cos(math.radians(random_angle))*speed
    canvas.create_oval(x, y, x+ size, y+ size, fill="red",tag="oval")
    if x>=width-size or x<=0:
        dx=-dx/abs(dx)
        if x>=width-size:x=width-size
        elif x<=0: x=0
        random_angle=random.choice(rand_list)*dx
    if y>=height-size or y<=0:
        dy=-dy/abs(dy)
        if y>=height-size:y=height-size
        elif y<=0: y=0
        random_angle=random.choice(rand_list)*dy
    if random_angle!=log_angle:
        log_angle=random_angle
        speed=random.uniform(1,6)
    root.update()
    canvas.delete("oval")

root.mainloop()
