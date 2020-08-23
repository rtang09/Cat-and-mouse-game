from tkinter import *
import tkinter
from tkinter import messagebox
import math
import time
from random import randint
from PIL import Image, ImageTk

def right(event):
    touch()
    touchwall()
    if mousecords[0] < 950 and walltouchmouse == False:
        paper.move(mouse, 10, 0)
def left(event):
    touch()
    touchwall()
    if mousecords[0] > 0 and walltouchmouse == False:
        paper.move(mouse, -10, 0)
def up(event):
    touch()
    touchwall()
    if mousecords[1] > 0 and walltouchmouse == False:
        paper.move(mouse, 0, -10)
def down(event):
    touch()
    touchwall()
    if mousecords[1] < 750 and walltouchmouse == False:
        paper.move(mouse, 0, 10)
def d(event):
    touch()
    touchwall()
    if catcords[0] < 950 and walltouchcat == False:
        paper.move(cat, 11, 0)
def a(event):
    touch()
    touchwall()
    if catcords[0] > 0 and walltouchcat == False:
        paper.move(cat, -11, 0)
def w(event):
    touch()
    touchwall()
    if catcords[1] > 0 and walltouchcat == False:
        paper.move(cat, 0, -11)
def s(event):
    touch()
    touchwall()
    if catcords[1] < 750 and walltouchcat == False:
        paper.move(cat, 0, 11)
def touch():
    global mousecords
    global catcords
    global amazon
    mousecords = paper.coords(mouse)
    catcords = paper.coords(cat)
    diffx = abs(mousecords[0] - catcords[0])
    diffy = abs(mousecords[1] - catcords[1])
    distance = math.sqrt(diffx*diffx + diffy*diffy)
    if distance <= 15:
        amazon = True
        messagebox.showinfo("Game over", "cat wins") 
        quit()
def touchwall():
    global wallcords
    global walltouchcat
    global walltouchmouse
    
    for i in (wall1, wall2, wall3, wall4, wall5, wall6, wall7, wall8):
        cordwall = paper.coords(i)
        diffcaty = abs(cordwall[1] - catcords[1])
        diffcatx = abs(cordwall[0] - catcords[0])
        diffcat = math.sqrt(diffcatx**2 + diffcaty**2)
        if diffcat <= 50:
            walltouchcat = True

    for i in (wall1, wall2, wall3, wall4, wall5, wall6, wall7, wall8):
        cordwall = paper.coords(i)
        diffmousey = abs(cordwall[1] - mousecords[1])
        diffmousex = abs(cordwall[0] - mousecords[0])
        diffmouse = math.sqrt(diffmousex**2 + diffmousey**2)
        if diffmouse <= 50:
            walltouchmouse = True
def checktime():
    left = leftover_time - (time.time()-starttime)
    tk.title('{:.0f}'.format(left))
    if left <=0:
        messagebox.showinfo( "Game over", "mouse wins")
        quit()
    if left > 0 and amazon==False:
        tk.after(100, checktime)
def check_in_wall(x, y):

    for i in (wall1, wall2, wall3, wall4, wall5, wall6, wall7, wall8):
        cordwall = paper.coords(i)
        dx = abs(x-cordwall[0])
        dy = abs(y-cordwall[1])
        dist = math.sqrt(dx**2 + dy**2)
        if dist <= 50:
            return True
    return False
def set_animal_not_in_wall():

    x = randint(500, 800)
    y = randint(500, 800)
    while check_in_wall(x, y):
        x = randint(500, 800)
        y = randint(500, 800)
    return x, y
def startgame():
    global starttime
    starttime = time.time()
    tk.after(100, checktime)
    button.pack_forget()



amazon = False
leftover_time = 30
walltouchcat = False
walltouchmouse = False



width = 1000
height = 850
tk = tkinter.Tk()
tk.configure(bg = "Yellow")
tk.title(leftover_time)
paper = Canvas(tk, width = width, height = height)

wall1 = paper.create_rectangle(20, 20, 100, 100, fill = "Brown")
wall2 = paper.create_rectangle(80, 80, 150, 150, fill = "Brown")
wall3 = paper.create_rectangle(130, 130, 200, 200, fill = "Brown")
wall4 = paper.create_rectangle(170, 170, 250, 250, fill = "Brown")
wall5 = paper.create_rectangle(230, 230, 300, 300, fill = "Brown")
wall6 = paper.create_rectangle(400, 400, 450, 450, fill = "Brown")
wall7 = paper.create_rectangle(1000, 1000, 800, 800, fill = "Brown")
wall8 = paper.create_rectangle(500, 500, 613, 613, fill = "Brown")


mouse_image = ImageTk.PhotoImage(Image.open('../../pictures_and_sounds/mouse_small2.png'))
x, y = set_animal_not_in_wall()
mouse = paper.create_image(x, y, anchor=NW, image=mouse_image)


cat_img = ImageTk.PhotoImage(Image.open('../../pictures_and_sounds/cat_small2.png'))
x, y = set_animal_not_in_wall()
cat = paper.create_image(x, y, anchor=NW, image=cat_img)



tk.bind("<Right>", right)
tk.bind("<Left>", left)
tk.bind("<Up>", up)
tk.bind("<Down>", down)
tk.bind("<d>", d)
tk.bind("<a>", a)
tk.bind("<w>", w)
tk.bind("<s>", s)



paper.pack()

button = tkinter.Button(tk, text = "Start", command=startgame)
button.pack(side = "top")
tk.mainloop()