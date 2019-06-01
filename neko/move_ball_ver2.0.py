import tkinter as tk
import os, sys, time
import random
import math


# 処理部分
def calc_canvas():

    return anko

# 描画画面キャンバス
def main_screen(root,x_now,y_now,*,width=800,height=450):
    canvas1=tk.Canvas(root,bg="red", width=width//3*2, height=height)
    canvas1.place(x=0,y=0)
    return 0

# 速さ
def speed_value(n):
    return 0


# 設定画面キャンバス
def setting_screen(root,*,width=800,height=450):

    canvas2=tk.Canvas(root,bg="red", width=width//3-1, height=height)
    canvas2.place(x=width//3*2+1,y=0)
    speed_scale=tk.Scale(root, label='speed', orient='h', from_=1/5, to=10, command=speed_value)
    speed_scale.pack(padx=width//4)
    return 0


# 変更の際にアップデート

# スタート
root=tk.Tk()
width_size=1280
height_size=720
root.geometry("{0}x{1}".format(width_size,height_size))
root.title("move ball")
"""
while 1:
    root.update()

"""
setting_screen(root,width=width_size,height=height_size)
root.mainloop()
