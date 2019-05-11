import tkinter as tk
import os, sys, time
import random

width=1280
height=720
root=tk.Tk()
root.geometry("1280x700")
# キャンバス
canvas = tk.Canvas(root,bg="white", width = 1279, height = 691)
canvas.place(x=0, y=0)
# オブジェクト
"""
canvas.create_oval(10, 10, 140, 140, fill="red",tag="oval")
"""
# 動かす
y=10
x=10
dx=1
dy=1
log_dx=dx
log_dy=dy
#unit_dx,unit_dy=dx/(dx**2+dy**2)**0.5,dy/(dx**2+dy**2)**0.5
size=140

while 1:
    time.sleep(1/500)
    x=x+dx
    y=y+dy
    canvas.create_oval(x, y, x+ size, y+ size, fill="red",tag="oval")
    if x>=width-size or x<=10:
        dx=-dx/abs(dx)
        dx=random.uniform(1,9)*dx
    if y>=height-size or y<=10:
        dy=-dy/abs(dy)
        dy=random.uniform(1,9)*dy
    # fix_me
    if dx!=log_dx or dy!=log_dy:
        unit_dx,unit_dy=dx/(dx**2+dy**2)**0.5,dy/(dx**2+dy**2)**0.5
        dx=dx/unit_dx
        dy=dy/unit_dy
        log_dx=dx
        log_dy=dy

    root.update()
    canvas.delete("oval")

root.mainloop()
