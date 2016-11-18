import Tkinter
import sys
import math
# allows for regular "for loops"
import numpy as np
import random

top = Tkinter.Tk()
# title of graph
top.wm_title("Graph Drawer")
# canvas size for graphing portion
C = Tkinter.Canvas(top, bg="white", height=501, width=501)

# main function call to draw graph
# IN: int array holding x,y coordinates, float step (delta X)
# OUT: n/a (visual)
# POST:
# Error: n/a

def drawNumbers():
    #lists hold x,y values
    xvalues = []
    yvalues = []
    C.create_line(250, 0, 250, 500)
    C.create_line(0, 250, 500, 250)

    for i in np.arange(-50,50,0.01): # x1,x2,step
        xvalues.append(i)
        yvalues.append(2 * i + 3 * i) # calculate Y here

    minimumX = min(xvalues)
    print minimumX
    maximumX = max(xvalues)
    print maximumX
    minimumY = min(yvalues)
    print minimumX
    maximumY = max(yvalues)
    print maximumX

    if (abs(minimumX-maximumX) > abs(minimumY-maximumY) and abs(minimumX-maximumX) > 500 or abs(maximumY-maximumY) > 500):
        scaleFactor = abs(minimumX-maximumX) / 500
    elif (abs(maximumY-minimumY) > abs(minimumX-maximumX)):
        scaleFactor = abs(minimumY-maximumY) / 500
    else:
        scaleFactor = 5;
    # iterate through both lists, zip preventes from one array going past other
    for i,y in zip(xvalues,yvalues):
        if scaleFactor > 1:
            i = i * scaleFactor
            y = y * scaleFactor
        else:
            i = i / scaleFactor
            y = y / scaleFactor
        C.create_oval(250+i-1, 250-y-1, 250+i+1,250-y+1, fill = "black")

drawNumbers()
C.pack()
top.mainloop()
