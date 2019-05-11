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
dx=1
dy=1
y=10
x=10
def make_oval(x,y,dx,dy):
    canvas.create_oval(x, y, x+140, y+140, fill="red",tag="oval")
    return 1

while 1:
    time.sleep(1/500)
    x=x+dx
    y=y+dy
    canvas.create_oval(x, y, x+140, y+140, fill="red",tag="oval")
    if x>=width-140:
        dx=random.uniform(-1,-9)
    if x<=10:
        dx=random.uniform(1,9)
    if y>=height-140:
        dy=random.uniform(-1,-9)
    if y<=10:
        dx=random.uniform(1,9)
    root.update()
    canvas.delete("oval")

root.mainloop()
