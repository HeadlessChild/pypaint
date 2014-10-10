from Tkinter import *
import sys
import os

#A reeeeaaally simple "paint" program

b1 = "up"
xold, yold = None, None
color= "black"
linesize = 2

def main():
    root = Tk()
    drawing_area = Canvas(root, width=800, height=600)
    drawing_area.pack()
    drawing_area.bind("<Motion>", motion)
    drawing_area.bind("<ButtonPress-1>", b1down)
    drawing_area.bind("<ButtonRelease-1>", b1up)

    button1 = Button(root, text = "Clear", command = restart_program, anchor = N)
    button1.configure(width = 3, background = "#FFFFFF", relief = FLAT)
    button1_window = drawing_area.create_window(400, 0, anchor=N, window=button1)

    buttonred = Button(root, command = buttred, anchor = N)
    buttonred.configure(width = 3, background = "#FF0000", relief = FLAT)
    buttonred_window = drawing_area.create_window(500, 0, anchor=N, window=buttonred)

    buttonblack = Button(root, command = buttblack, anchor = N)
    buttonblack.configure(width = 3, background = "#000000", relief = FLAT)
    buttonblack_window = drawing_area.create_window(550, 0, anchor=N, window=buttonblack)

    buttongreen = Button(root, command = buttgreen, anchor = N)
    buttongreen.configure(width = 3, background = "#00FF00", relief = FLAT)
    buttongreen_window = drawing_area.create_window(600, 0, anchor=N, window=buttongreen)

    buttonblue = Button(root, command = buttblue, anchor = N)
    buttonblue.configure(width = 3, background = "#0000FF", relief = FLAT)
    buttonblue_window = drawing_area.create_window(650, 0, anchor=N, window=buttonblue)

    buttonyellow = Button(root, command = buttyellow, anchor = N)
    buttonyellow.configure(width = 3, background = "#FFFF00", relief = FLAT)
    buttonyellow_window = drawing_area.create_window(700, 0, anchor=N, window=buttonyellow)

    buttongrey = Button(root, command = buttgrey, anchor = N)
    buttongrey.configure(width = 3, background = "#808080", relief = FLAT)
    buttongrey_window = drawing_area.create_window(300, 0, anchor=N, window=buttongrey)    

    buttonpurple = Button(root, command = buttpurple, anchor = N)
    buttonpurple.configure(width = 3, background = "#800080", relief = FLAT)
    buttonpurple_window = drawing_area.create_window(250, 0, anchor=N, window=buttonpurple)

    buttonorange = Button(root, command = buttorange, anchor = N)
    buttonorange.configure(width = 3, background = "#FFA500", relief = FLAT)
    buttonorange_window = drawing_area.create_window(200, 0, anchor=N, window=buttonorange)

    buttonbrown = Button(root, command = buttbrown, anchor = N)
    buttonbrown.configure(width = 3, background = "#A52A2A", relief = FLAT)
    buttonbrown_window = drawing_area.create_window(150, 0, anchor=N, window=buttonbrown)

    buttoncyan = Button(root, command = buttcyan, anchor = N)
    buttoncyan.configure(width = 3, background = "#00FFFF", relief = FLAT)
    buttoncyan_window = drawing_area.create_window(150, 0, anchor=N, window=buttoncyan)

    buttonadd = Button(root, text="+", command = buttadd, anchor = N)
    buttonadd.configure(width = 3, background = "#FFFFFF", relief = FLAT)
    buttonadd_window = drawing_area.create_window(50, 0, anchor=N, window=buttonadd)

    buttonsub = Button(root, text="-", command = buttsub, anchor = N)
    buttonsub.configure(width = 3, background = "#FFFFFF", relief = FLAT)
    buttonsub_window = drawing_area.create_window(100, 0, anchor=N, window=buttonsub)

    root.geometry('800x600')
    root.geometry('+400+200')
    #root.overrideredirect(True)         #No border
    root.mainloop()

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def buttred():
    global color
    color= "red"

def buttblack():
    global color
    color= "black"

def buttgreen():
    global color
    color= "green"

def buttblue():
    global color
    color= "blue"

def buttyellow():
    global color
    color= "yellow"

def buttgrey():
    global color
    color= "grey"

def buttpurple():
    global color
    color= "purple"

def buttorange():
    global color
    color= "orange"

def buttbrown():
    global color
    color= "brown"

def buttcyan():
    global color
    color= "cyan"

def buttadd():
    global linesize
    linesize += 0.5

def buttsub():
    global linesize
    linesize -= 0.5

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
            event.widget.create_line(xold,yold,event.x,event.y,smooth=TRUE,fill = color, width=linesize)
        xold = event.x
        yold = event.y

if __name__ == "__main__":
    main()