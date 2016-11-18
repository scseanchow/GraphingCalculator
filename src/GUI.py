# coding=utf-8
from Tkinter import *
# allows for regular "for loops"
import numpy as np
import random
import arithmetic

root = Tk()
def startGUI():
    root.geometry('1000x750')
    #start loop
    root.mainloop()

# function to calculate
def calculate():
    equation = txtDisplay.get()
    #call infix/calculate function
    txtDisplay.delete(0, END)
    # insert answer
    txtDisplay.insert(0, "GOTTI")

# clear the text box
def clear():
    txtDisplay.delete(0, END)
    return

# function to draw the graph
def drawNumbers():
    #lists hold x,y values
    xvalues = []
    yvalues = []
    graphArea.create_line(250, 0, 250, 500)
    graphArea.create_line(0, 250, 500, 250)

    for i in np.arange(-50,50,0.01): # x1,x2,step
        xvalues.append(i)
        yvalues.append(2 * i + 3 * i) # calculate Y here

    minimumX = min(xvalues)
    #print minimumX
    maximumX = max(xvalues)
    #print maximumX
    minimumY = min(yvalues)
    #print minimumX
    maximumY = max(yvalues)
    #print maximumX

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
        graphArea.create_oval(250+i-1, 250-y-1, 250+i+1,250-y+1, fill = "black")

# update text box
def update_entry(v):
    current_value = num1.get()
    num1.set(current_value + v)


# Main entry.
num1 = StringVar()
txtDisplay = Entry(root, textvariable=num1, relief=RIDGE,
                   bd=10, width=63, insertwidth=1, font=40).grid(row = 0, column = 0)
graphArea = Canvas(root, relief=GROOVE, bd=3, width=501,
                   height=501, bg="white", highlightcolor="black")
graphArea.grid(row=1, column=0)

# Locks the parent windows size.
root.maxsize(1000, 750)
root.minsize(1000, 750)
root.wm_title("Graphing Calculator | Group 3")
# Parent window's background color:
root.configure(background='white')
# Buttons:
zeroButton = Button(root, text='0', width=20, height=2, bg='white', fg='black',
                    command=lambda: update_entry('0')).place(x=264 ,y= 700)
oneButton = Button(root, text='1', width=8, height=2, bg='white', fg='black', command=lambda: update_entry('1')).place(
    x=17, y=700)
twoButton = Button(root, text='2', width=8, height=2, bg='white', fg='black', command=lambda: update_entry('2')).place(
    x=100, y=700)
threeButton = Button(root, text='3', width=8, height=2, bg='white', fg='black',
                     command=lambda: update_entry('3')).place(x=182, y=700)
fourButton = Button(root, text='4', width=8, height=2, bg='white', fg='black', command=lambda: update_entry('4')).place(
    x=17, y=630)
fiveButton = Button(root, text='5', width=8, height=2, bg='white', fg='black', command=lambda: update_entry('5')).place(
    x=100, y=630)
sixButton = Button(root, text='6', width=8, height=2, bg='white', fg='black', command=lambda: update_entry('6')).place(
    x=182, y=630)
sevenButton = Button(root, text='7', width=8, height=2, bg='white', fg='black',
                     command=lambda: update_entry('7')).place(x=17, y=562)
eightButton = Button(root, text='8', width=8, height=2, bg='white', fg='black',
                     command=lambda: update_entry('8')).place(x=100, y=562)
ninthButton = Button(root, text='9', width=8, height=2, bg='white', fg='black',
                     command=lambda: update_entry('9')).place(x=182, y=562)

decimalButton = Button(root, text='.', width=10, height=2, bg='gray', command=lambda: update_entry('.')).place(x=264,
                                                                                                              y=630)
equalButton = Button(root, text='=', width=20, height=2, bg='Lightgreen', command=calculate).place(x=264,
                                                                                                  y=562)
plusButton = Button(root, text='+', width=8, height=2, bg='gray',
                    command=lambda: update_entry('+')).place(x=425, y=562)
minusButton = Button(root, text='-', width=8, height=2, bg='gray', command=lambda: update_entry('-')).place(x=425,
                                                                                                            y=630)
multiplyButton = Button(root, text='x', width=8, height=2, bg='gray', command=lambda: update_entry('*')).place(x=425,
                                                                                                               y=700)
divideButton = Button(root, text='÷', width=8, height=2, bg='gray', command=lambda: update_entry('/')).place(x=350,
                                                                                                             y=630)
clearButton = Button(root, text='Clear (CE)', width=38,
                     height=3, command=clear, bg='pink').place(x=515, y=495)

shiftButton = Button(root, text='Shift', width=20, height=5,
                     command=clear, bg='orange').place(x=515, y=562)
graphButton = Button(root, text='GRAPH', width=20,
                     height=5, bg='pink',command = drawNumbers).place(x=515, y=655)
cosButton = Button(root, text='cos', width=15, height=3,
                   bg='skyblue',command=lambda: update_entry("cos")).place(x=675, y=562)
sineButton = Button(root, text='sine',command=lambda: update_entry("sin"), width=15, height=3,
                    bg='skyblue').place(x=675, y=624)
tanButton = Button(root, text='tan', width=15, height=3,
                   bg='skyblue',command=lambda: update_entry("tan")).place(x=675, y=685)
