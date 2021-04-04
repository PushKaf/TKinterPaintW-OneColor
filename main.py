from tkinter import *


curX, curY = 0, 0
def locXY(event):
    global curX, curY
    curX, curY = event.x, event.y
    # print(curX, curY)

def addLine(event):
    global curX, curY
    canvas.create_line((curX, curY, event.x, event.y))
    curX, curY = event.x, event.y


root = Tk()
root.title("Pain(t) Pog!")
root.state("zoomed")
# root.geometry("1280x720")
# root.resizable(False, False)
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

canvas = Canvas(root)
canvas.grid(row=0, column=0, sticky="nsew")

canvas.bind("<Button-1>", locXY)
canvas.bind("<B1-Motion>", addLine)

root.mainloop()