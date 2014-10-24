from Tkinter import *
import tkMessageBox
import sys
import os
import subprocess
import urllib2

#A reeeeaaally simple "paint" program

b1 = "up"
xold, yold = None, None
color= "black"
linesize = 2

def main():
    global root
    root = Tk()
    global drawing_area
    drawing_area = Canvas(root, width=1280, height=720, background="white")
    drawing_area.pack()
    drawing_area.bind("<Motion>", motion)
    drawing_area.bind("<ButtonPress-1>", b1down)
    drawing_area.bind("<ButtonRelease-1>", b1up)
    
    global drawing_area_id
    drawing_area_id = drawing_area.create_text(290, 10, anchor=NW)
    drawing_area.itemconfig(drawing_area_id, text = linesize)

    global drawing_area_id2
    drawing_area_id2 = drawing_area.create_text(12, 0, anchor=NW)
    drawing_area.itemconfig(drawing_area_id2, text = "Current Color")

    global square
    square = drawing_area.create_rectangle(18,15,80,25, fill="black")

    buttonred = Button(root, command = buttred, anchor = N)
    buttonred.configure(width = 3, background = "#FF0000", relief = FLAT)
    buttonred_window = drawing_area.create_window(740, 0, anchor=N, window=buttonred)

    buttonblack = Button(root, command = buttblack, anchor = N)
    buttonblack.configure(width = 3, background = "#000000", relief = FLAT)
    buttonblack_window = drawing_area.create_window(790, 0, anchor=N, window=buttonblack)

    buttongreen = Button(root, command = buttgreen, anchor = N)
    buttongreen.configure(width = 3, background = "#00FF00", relief = FLAT)
    buttongreen_window = drawing_area.create_window(840, 0, anchor=N, window=buttongreen)

    buttonblue = Button(root, command = buttblue, anchor = N)
    buttonblue.configure(width = 3, background = "#0000FF", relief = FLAT)
    buttonblue_window = drawing_area.create_window(890, 0, anchor=N, window=buttonblue)

    buttonyellow = Button(root, command = buttyellow, anchor = N)
    buttonyellow.configure(width = 3, background = "#FFFF00", relief = FLAT)
    buttonyellow_window = drawing_area.create_window(940, 0, anchor=N, window=buttonyellow)

    button1 = Button(root, text = "Reset", command = remove_lines, anchor = N)
    button1.configure(width = 3, background = "#FFFFFF", relief = FLAT)
    button1_window = drawing_area.create_window(640, 0, anchor=N, window=button1)

    buttoneraser = Button(root, text="Eraser", command = butter, anchor = N)
    buttoneraser.configure(width = 3, background = "#FFFFFF", relief = FLAT)
    buttoneraser_window = drawing_area.create_window(690, 0, anchor=N, window=buttoneraser)

    buttonquote = Button(root, text="Quotes", command = text, anchor = N)
    buttonquote.configure(width = 3, background = "#FFFFFF", relief = FLAT)
    buttonquote_window = drawing_area.create_window(590, 0, anchor=N, window=buttonquote)

    buttongrey = Button(root, command = buttgrey, anchor = N)
    buttongrey.configure(width = 3, background = "#808080", relief = FLAT)
    buttongrey_window = drawing_area.create_window(540, 0, anchor=N, window=buttongrey)    

    buttonpurple = Button(root, command = buttpurple, anchor = N)
    buttonpurple.configure(width = 3, background = "#800080", relief = FLAT)
    buttonpurple_window = drawing_area.create_window(490, 0, anchor=N, window=buttonpurple)

    buttonorange = Button(root, command = buttorange, anchor = N)
    buttonorange.configure(width = 3, background = "#FFA500", relief = FLAT)
    buttonorange_window = drawing_area.create_window(440, 0, anchor=N, window=buttonorange)

    buttonbrown = Button(root, command = buttbrown, anchor = N)
    buttonbrown.configure(width = 3, background = "#A52A2A", relief = FLAT)
    buttonbrown_window = drawing_area.create_window(390, 0, anchor=N, window=buttonbrown)

    buttoncyan = Button(root, command = buttcyan, anchor = N)
    buttoncyan.configure(width = 3, background = "#00FFFF", relief = FLAT)
    buttoncyan_window = drawing_area.create_window(340, 0, anchor=N, window=buttoncyan)

    buttonsub = Button(root, text="-", command = buttsub, anchor = N)
    buttonsub.configure(width = 3, background = "#FFFFFF", relief = FLAT)
    buttonsub_window = drawing_area.create_window(240, 0, anchor=N, window=buttonsub)

    buttonadd = Button(root, text="+", command = buttadd, anchor = N)
    buttonadd.configure(width = 3, background = "#FFFFFF", relief = FLAT)
    buttonadd_window = drawing_area.create_window(190, 0, anchor=N, window=buttonadd)

    root.geometry('1280x720')
    root.geometry('+200+200')
    #root.overrideredirect(True)         #No border
    root.mainloop()

def remove_lines():
    drawing_area.delete("lines")

def text():
    quotes = subprocess.Popen(['/usr/games/fortune'], stdout=subprocess.PIPE).communicate()[0]
    tkMessageBox.showinfo("Timeless Quotes", quotes)

def buttred():
    global color
    color= "red"
    global square
    drawing_area.delete(square)
    square = drawing_area.create_rectangle(11,15,80,25, fill="red")

def buttblack():
    global color
    color= "black"
    global square
    drawing_area.delete(square)
    square = drawing_area.create_rectangle(11,15,80,25, fill="black")

def buttgreen():
    global color
    color= "green"
    global square
    drawing_area.delete(square)
    square = drawing_area.create_rectangle(11,15,80,25, fill="green")

def buttblue():
    global color
    color= "blue"
    global square
    drawing_area.delete(square)
    square = drawing_area.create_rectangle(11,15,80,25, fill="blue")

def buttyellow():
    global color
    color= "yellow"
    global square
    drawing_area.delete(square)
    square = drawing_area.create_rectangle(11,15,80,25, fill="yellow")

def buttgrey():
    global color
    color= "grey"
    global square
    drawing_area.delete(square)
    square = drawing_area.create_rectangle(11,15,80,25, fill="grey")

def buttpurple():
    global color
    color= "purple"
    global square
    drawing_area.delete(square)
    square = drawing_area.create_rectangle(11,15,80,25, fill="purple")

def buttorange():
    global color
    color= "orange"
    global square
    drawing_area.delete(square)
    square = drawing_area.create_rectangle(11,15,80,25, fill="orange")

def buttbrown():
    global color
    color= "brown"
    global square
    drawing_area.delete(square)
    square = drawing_area.create_rectangle(11,15,80,25, fill="brown")

def buttcyan():
    global color
    color= "cyan"
    global square
    drawing_area.delete(square)
    square = drawing_area.create_rectangle(11,15,80,25, fill="cyan")

def butter():
    global color
    color= "white"
    global square
    drawing_area.delete(square)
    square = drawing_area.create_rectangle(11,15,80,25, fill="white")

def buttadd():
    global linesize
    if linesize < 10:
        linesize += 1
    global drawing_area_id
    drawing_area.delete(drawing_area_id)
    drawing_area_id = drawing_area.create_text(290, 10, anchor=NW)
    drawing_area.itemconfig(drawing_area_id, text = linesize)

def buttsub():
    global linesize
    if linesize > 1:
        linesize -= 1
    global drawing_area_id
    drawing_area.delete(drawing_area_id)
    drawing_area_id = drawing_area.create_text(290, 10, anchor=NW)
    drawing_area.itemconfig(drawing_area_id, text = linesize)

def b1down(event):
    global b1
    b1 = "down"

def b1up(event):
    global b1, xold, yold
    b1 = "up"
    xold = None
    yold = None

def motion(event):
    if b1 == "down":
        global xold, yold
        if xold is not None and yold is not None:
            event.widget.create_line(xold,yold,event.x,event.y,smooth=TRUE,fill = color, width=linesize, tag="lines")
        xold = event.x
        yold = event.y

if __name__ == "__main__":
    main()