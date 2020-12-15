import tkinter as tk
import random as r
from tkinter import messagebox as mb
window= tk.Tk()
window.geometry("500x500")
pixelVirtual = tk.PhotoImage(width=1, height=1)
count = 17
colors = ["black","purple","yellow","white","green","brown","red","blue"]
colors2 = {"black":2,"purple":2,"yellow":2,"white":2,"green":2,"brown":2,"red":2,"blue":2}
click = 0
clicked = None
clicked2 = None
nechto = None
timer = 0
revive = 16
def open_card(e):
    global click,nechto,clicked,clicked2, revive
    revive = 16
    try:
        if click == 1:
            e.widget["bg"] = e.widget.color
            clicked2 = e.widget
            time(clicked,clicked2)
        if e.widget.state2 == "normal" and click == 0: 
            e.widget["bg"] = e.widget.color
            click = 1
            clicked = e.widget
    except:
        pass

def time(obj1, obj2):
    global timer,click,nechto,clicked,clicked2, revive,y1,x1,btns,colors2
    if timer == 0:
        for btn in btns:
            btn["state"] = "disabled"
            btn.state2 = "disabled"
    if timer == 3000:
        if obj1.color == obj2.color:
            obj1.para = True
            obj2.para = True
        for btn in btns:
            if btn.para == False:
                btn["state"] = tk.NORMAL
                btn.state2 = "normal"
                btn["bg"] = "gray"
                revive = revive - 1
        click = 0
        clicked = None
        clicked2 = None
        timer = 0
        if revive == 16:
            answer = mb.askyesno(title="Вопрос",message="Начать заново?")
            if answer:
                x1,y1 = 31.25,31.25
                btns = []
                colors2 = {"black":2,"purple":2,"yellow":2,"white":2,"green":2,"brown":2,"red":2,"blue":2}
                generator()
        stop()
    timer = timer + 1
    nechto = window.after(1,time(obj1, obj2))
def stop():
    window.after_cancel(nechto)


x1,y1 = 31.25,31.25
btns = []
def generator():
    global x1,y1,btns
    for i in range(1,count):
        btn = tk.Button(window, text=" ", height = 50, width = 50,  compound="c", image=pixelVirtual, bg = "gray")
        btn.num = i
        btn.state2 = "normal"
        btn.para = False
        a = True
        while a:
            rand = r.randint(0,7)
            if colors2[colors[rand]] > 0:
                btn.color = colors[rand]
                a = False
                colors2[colors[rand]] = colors2[colors[rand]] - 1
        btns.append(btn)

    for btn in btns:
            btn.place(x = x1, y = y1)
            if btn.num % 4 == 0:
                y1 = y1 + 125
                x1 = 31.25
            else:
                x1 = x1 + 125

generator()


window.bind("<Button-1>", open_card)
window.mainloop()