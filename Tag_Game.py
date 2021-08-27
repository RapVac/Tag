from tkinter import *
import time
import random
tk=Tk()
tk.title("Tag!!!")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas=Canvas(tk, width=500, height=500, bd=0, highlightthickness=0)
canvas.create_rectangle(0, 0, 500, 500, fill='green')
canvas.pack()
tk.update()
t1=time.time()

class Human:
    def __init__(self, canvas, color, speed):
        self.canvas=canvas
        self.speed=speed
        self.id=canvas.create_rectangle(10, 10, 30, 30, fill=color)
        self.canvas.move(self.id, 250, 250)
        self.x = 0
        self.y = 0
        self.canvas_height = canvas.winfo_height()
        self.canvas_width = canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Up>', self.Move)
        self.canvas.bind_all('<KeyPress-Down>', self.Move)
        self.canvas.bind_all('<KeyPress-Left>', self.Move)
        self.canvas.bind_all('<KeyPress-Right>', self.Move)

    def Move(self, event):
        if event.keysym == 'Up':
            self.y = -self.speed
            self.x=0
        if event.keysym == 'Down':
            self.y = self.speed
            self.x=0
        if event.keysym == 'Left':
            self.x = -self.speed
            self.y=0
        if event.keysym == 'Right':
            self.x = self.speed
            self.y=0
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 0
        if pos[3] >= self.canvas_height:
            self.y = 0
        if pos[0] <= 0:
            self.x=0
        if pos[2] >= self.canvas_width:
            self.x=0


class Hunter:
    def __init__(self, human, canvas, color, speed):
        self.canvas=canvas
        self.human=human
        self.speed=speed
        self.id = canvas.create_rectangle(10, 10, 30, 30, fill=color)
        self.canvas.move(self.id, 250, 20)
        self.x=0
        self.y=0
        self.canvas_height = canvas.winfo_height()
        self.canvas_width = canvas.winfo_width()
        self.your_it = False
        self.p=1
        self.pts=0

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        human_pos = self.canvas.coords(self.human.id)
        h_x1 = human_pos[0]
        s_x1 = pos[0]
        if h_x1 >= s_x1:
            self.x = self.speed
        if h_x1 <= s_x1:
            self.x = -self.speed
        h_y1 = human_pos[1]
        s_y1 = pos[1]
        if h_y1 >= s_y1:
            self.y = self.speed
        if h_y1 <= s_y1:
            self.y = -self.speed

            
        if abs(h_x1-s_x1) < 10 and abs(h_y1-s_y1) < 10:
            self.your_it = True
            time.sleep(1)
            t2 = time.time()
            ft="You lasted %s seconds" % round(t2-t1)
            canvas.create_text(250, 250, text="Tag! Your it!", fill='dark blue', font=('Times', 30))
            canvas.create_text(250, 285, text=ft, fill='dark blue', font=('Times', 22))
            
            
human = Human(canvas, 'blue', 3)
hunter = Hunter(human, canvas, 'black', 2.2)

while 1:
    if hunter.your_it == False:
        human.draw()
        hunter.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
