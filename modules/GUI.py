# coding=utf-8

from Tkinter import *


def clear():
    txtDisplay.delete(0, END)
    return


# Parent Window.
root = Tk()
root.title('3250 Calculator')
root.geometry('350x750')

# Main entry.
num1 = StringVar()
txtDisplay = Entry(root, textvariable=num1, relief=RIDGE, bd=10, width=27, insertwidth=1, font=40)
txtDisplay.place(x=15, y=10)
txtDisplay.focus()


def update_entry(v):
    current_value = num1.get()
    num1.set(current_value + v)


# Buttons:
zeroButton = Button(root, text='0', width=20, height=3, bg='white', fg='black',
                    command=lambda: update_entry('0')).place(x=17, y=682)
oneButton = Button(root, text='1', width=8, height=3, bg='white', fg='black', command=lambda: update_entry('1')).place(
    x=17, y=602)
twoButton = Button(root, text='2', width=8, height=3, bg='white', fg='black').place(x=100, y=602)
threeButton = Button(root, text='3', width=8, height=3, bg='white', fg='black').place(x=182, y=602)
fourButton = Button(root, text='4', width=8, height=3, bg='white', fg='black').place(x=17, y=522)
fiveButton = Button(root, text='5', width=8, height=3, bg='white', fg='black').place(x=100, y=522)
sixButton = Button(root, text='6', width=8, height=3, bg='white', fg='black').place(x=182, y=522)
sevenButton = Button(root, text='7', width=8, height=3, bg='white', fg='black').place(x=17, y=442)
eightButton = Button(root, text='8', width=8, height=3, bg='white', fg='black').place(x=100, y=442)
ninthButton = Button(root, text='9', width=8, height=3, bg='white', fg='black').place(x=182, y=442)

decimalButton = Button(root, text='.', width=8, height=3, bg='gray').place(x=182, y=682)
equalButton = Button(root, text='=', width=8, height=8, bg='Lightgreen').place(x=264, y=602)
plusButton = Button(root, text='+', width=8, height=3, bg='gray', command=lambda: update_entry('+')).place(x=264, y=442)
minusButton = Button(root, text='-', width=8, height=3, bg='gray').place(x=264, y=522)
multiplyButton = Button(root, text='x', width=8, height=3, bg='gray').place(x=264, y=366)
divideButton = Button(root, text='÷', width=8, height=3, bg='gray').place(x=182, y=366)
clearButton = Button(root, text='Clear (CE)', width=20, height=3, command=clear, bg='pink').place(x=17, y=366)

# Locks the parent windows size.
root.maxsize(350, 750)
root.minsize(350, 750)

# Parent window's background color:
root.configure(background='black')
root.mainloop()
