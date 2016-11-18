# coding=utf-8
from Tkinter import *
import numpy as np
import random
import math
import parser
import solve
from pyparsing import Literal, CaselessLiteral, Word, Combine, Group, Optional,\
    ZeroOrMore, Forward, nums, alphas
import operator

# expression stack
exprStack = []

# answer stack
answerStack = []
index = 0

# Parent Window.
root = Tk()
root.geometry('1000x750')
top = Frame(root)
bottom = Frame(root)
top.pack(side=TOP)
bottom.pack(side=BOTTOM, fill=BOTH, expand=True)


def display_Credits():
    creditsArea = Canvas(top, relief=GROOVE, bd=3, width=175,
                         height=130, bg="white", highlightcolor="black")
    creditsArea.grid(row=3, column=6, sticky=N, columnspan=3, rowspan=10)
    trevor = creditsArea.create_text(10, 10, anchor="nw")
    creditsArea.itemconfig(trevor, text="Trevor D'Souza")
    sean = creditsArea.create_text(10, 25, anchor="nw")
    creditsArea.itemconfig(sean, text="Sean Chow")
    daniel = creditsArea.create_text(10, 40, anchor="nw")
    creditsArea.itemconfig(daniel, text="Daniel Domalik")
    alej = creditsArea.create_text(10, 55, anchor="nw")
    creditsArea.itemconfig(alej, text="Alejandro Lobo Mujica")
    caleb = creditsArea.create_text(10, 70, anchor="nw")
    creditsArea.itemconfig(caleb, text="Caleb Allen")
    connor = creditsArea.create_text(10, 85, anchor="nw")
    creditsArea.itemconfig(connor, text="Connor Campbell")
    scott = creditsArea.create_text(10, 100, anchor="nw")
    creditsArea.itemconfig(scott, text="Scott Bootsma")
    shell = creditsArea.create_text(10, 115, anchor="nw")
    creditsArea.itemconfig(shell, text="Sheldon Taylor-Rawson")


def startGUI():
    root.mainloop()
num1 = StringVar()
txtDisplay = Entry(top, textvariable=num1, relief=RIDGE,
                   bd=10, width=63, insertwidth=1, font=40)
txtDisplay.grid(row=0, column=2)

g1Label = Button(top,command=lambda:drawIndividualGraph(1), text="G1", font=70)
g2Label = Button(top,command=lambda:drawIndividualGraph(2), text="G2", font=70)
g3Label = Button(top,command=lambda:drawIndividualGraph(3), text="G3", font=70)
g4Label = Button(top,command=lambda:drawIndividualGraph(4), text="G4", font=70)
g5Label = Button(top,command=lambda:drawIndividualGraph(5), text="G5", font=70)
g6Label = Button(top,command=lambda:drawIndividualGraph(6), text="G6", font=70)

g1 = Entry(top, relief=RIDGE, bd=10, width=20, font=40)
g1Label.grid(row=2, column=0)
g1.grid(row=2, column=1)
g2 = Entry(top, relief=RIDGE, bd=10, width=20, font=40)
g2Label.grid(row=3, column=0)
g2.grid(row=3, column=1)
g3 = Entry(top, relief=RIDGE, bd=10, width=20, font=40)
g3Label.grid(row=4, column=0)
g3.grid(row=4, column=1)
g4 = Entry(top, relief=RIDGE, bd=10, width=20, font=40)
g4Label.grid(row=5, column=0)
g4.grid(row=5, column=1)
g5 = Entry(top, relief=RIDGE, bd=10, width=20, font=40)
g5Label.grid(row=6, column=0)
g5.grid(row=6, column=1)


def limitInput(*args):
    value = x1.get()
    if len(value) > 4:
        x1.set(value[:4])


def limitInput2(*args):
    value = x2.get()
    if len(value) > 4:
        x2.set(value[:4])


x1 = StringVar()
x1.trace('w', limitInput)

x2 = StringVar()
x2.trace('w', limitInput2)

xValuesLabel = Label(top, text="x values:", font=70)
commaLabel = Label(top, text=",", font=40)
xValuesLabel.grid(row=1, column=6, sticky=N)
xEntry1 = Entry(top, bd=1, width=5, insertwidth=1, font=40, textvariable=x1)
xEntry1.grid(row=1, column=7, sticky=N)
commaLabel.grid(row=1, column=8, sticky=N)
xEntry2 = Entry(top, bd=1, width=5, insertwidth=1, font=40, textvariable=x2)
xEntry2.grid(row=1, column=9, sticky=N)

graphArea = Canvas(top, relief=GROOVE, bd=3, width=501,
                   height=501, bg="white", highlightcolor="black")
graphArea.grid(row=1, column=2, sticky=W, columnspan=5, rowspan=20)


def goUp():
    global answerStack
    global index
    maxIndex = len(answerStack)
    print maxIndex

    if (index < maxIndex - 1):
        index += 1
        txtDisplay.delete(0, END)
        update_entry(str(answerStack[index]))


def goDown():
    global answerStack
    global index
    txtDisplay.delete(0, END)
    if (index > 0):
        index -= 1
        txtDisplay.delete(0, END)
        update_entry(str(answerStack[index]))

# function to calculate


def calculate():
    global emptyStack
    global answerStack
    global index
    index += 1
    equation = txtDisplay.get()
    emptyStack = []
    ans = BNF().parseString(equation)
    ans = evaluateStack(emptyStack[:])
    txtDisplay.delete(0, END)
    # insert answer
    answerStack.append(ans)
    update_entry(str(ans))
# clear the text box


def clear():
    txtDisplay.delete(0, END)
    return

# function to draw the graph

def drawIndividualGraph(graphNo):
    xvalues = []
    yvalues = []
    graphArea.create_line(250, 0, 250, 500)
    graphArea.create_line(0, 250, 500, 250)
    xRangeMin = float(xEntry1.get())
    xRangeMax = float(xEntry2.get())

    for x in np.arange(xRangeMin, xRangeMax, 0.05):  # x1,x2,step
        if graphNo == 1:
            equation = g1.get()
        elif graphNo == 2:
            equation = g2.get()
        elif graphNo == 3:
            equation = g3.get()
        elif graphNo == 4:
            equation = g4.get()
        elif graphNo == 5:
            equation = g5.get()
        elif graphNo == 6:
            equation = g6.get()

        equation = equation.replace("x", str(x))
        global emptyStack
        emptyStack = []
        ans = BNF().parseString(equation)
        ans = evaluateStack(emptyStack[:])
        xvalues.append(x)
        yvalues.append(ans)
    for i, y in zip(xvalues, yvalues):
        graphArea.create_oval(250 + i - 1, 250 - y - 1,
                              250 + i + 1, 250 - y + 1, fill="black")
def drawNumbers():
    graphArea.delete("all")
    # lists hold x,y values
    xvalues = []
    yvalues = []
    graphArea.create_line(250, 0, 250, 500)
    graphArea.create_line(0, 250, 500, 250)
    xRangeMin = float(xEntry1.get())
    xRangeMax = float(xEntry2.get())
    for x in np.arange(xRangeMin, xRangeMax, 0.05):  # x1,x2,step
        equation = txtDisplay.get()
        equation = equation.replace("x", str(x))
        global emptyStack
        emptyStack = []
        ans = BNF().parseString(equation)
        ans = evaluateStack(emptyStack[:])
        xvalues.append(x)
        yvalues.append(ans)
    # iterate through both lists, zip preventes from one array going past other
    for i, y in zip(xvalues, yvalues):
        graphArea.create_oval(250 + i - 1, 250 - y - 1,
                              250 + i + 1, 250 - y + 1, fill="black")

# functinos for solving infix


def pushFirst(strg, loc, toks):
    emptyStack.append(toks[0])


def pushUMinus(strg, loc, toks):
    if toks and toks[0] == '-':
        emptyStack.append('unary -')
        #~ exprStack.append( '-1' )
        #~ exprStack.append( '*' )

bnf = None


def BNF():
    """
    expop   :: '^'
    multop  :: '*' | '/'
    addop   :: '+' | '-'
    integer :: ['+' | '-'] '0'..'9'+
    atom    :: PI | E | real | fn '(' expr ')' | '(' expr ')'
    factor  :: atom [ expop factor ]*
    term    :: factor [ multop factor ]*
    expr    :: term [ addop term ]*
    """
    global bnf
    if not bnf:
        point = Literal(".")
        e = CaselessLiteral("E")
        fnumber = Combine(Word("+-" + nums, nums) +
                          Optional(point + Optional(Word(nums))) +
                          Optional(e + Word("+-" + nums, nums)))
        ident = Word(alphas, alphas + nums + "_$")

        plus = Literal("+")
        minus = Literal("-")
        mult = Literal("*")
        div = Literal("/")
        lpar = Literal("(").suppress()
        rpar = Literal(")").suppress()
        addop = plus | minus
        multop = mult | div
        expop = Literal("^")
        pi = CaselessLiteral("PI")

        expr = Forward()
        atom = (Optional("-") + (pi | e | fnumber | ident + lpar + expr + rpar).setParseAction(
            pushFirst) | (lpar + expr.suppress() + rpar)).setParseAction(pushUMinus)

        # by defining exponentiation as "atom [ ^ factor ]..." instead of "atom [ ^ atom ]...", we get right-to-left exponents, instead of left-to-righ
        # that is, 2^3^2 = 2^(3^2), not (2^3)^2.
        factor = Forward()
        factor << atom + ZeroOrMore((expop + factor).setParseAction(pushFirst))

        term = factor + ZeroOrMore((multop + factor).setParseAction(pushFirst))
        expr << term + ZeroOrMore((addop + term).setParseAction(pushFirst))
        bnf = expr
    return bnf

# map operator symbols to corresponding arithmetic operations
epsilon = 1e-12
opn = {"+": operator.add,
       "-": operator.sub,
       "*": operator.mul,
       "/": operator.truediv,
       "^": operator.pow}
fn = {"sin": math.sin,
      "cos": math.cos,
      "tan": math.tan,
      "abs": abs,
      "trunc": lambda a: int(a),
      "round": round,
      "sgn": lambda a: abs(a) > epsilon and cmp(a, 0) or 0}


def evaluateStack(s):
    op = s.pop()
    if op == 'unary -':
        return -evaluateStack(s)
    if op in "+-*/^":
        op2 = evaluateStack(s)
        op1 = evaluateStack(s)
        return opn[op](op1, op2)
    elif op == "PI":
        return math.pi  # 3.1415926535
    elif op == "E":
        return math.e  # 2.718281828
    elif op in fn:
        return fn[op](evaluateStack(s))
    elif op[0].isalpha():
        return 0
    else:
        return float(op)

# update text box


def update_entry(v):
    current_value = num1.get()
    num1.set(current_value + v)


# Buttons:
zeroButton = Button(bottom, text='0', width=27, height=2, bg='white', fg='black',
                    command=lambda: update_entry('0')).grid(row=3, column=0, columnspan=3)
oneButton = Button(bottom, text='1', width=8, height=2, bg='white',
                   fg='black', command=lambda: update_entry('1')).grid(row=2, column=0)
twoButton = Button(bottom, text='2', width=8, height=2, bg='white',
                   fg='black', command=lambda: update_entry('2')).grid(row=2, column=1)
threeButton = Button(bottom, text='3', width=8, height=2, bg='white',
                     fg='black', command=lambda: update_entry('3')).grid(row=2, column=2)
fourButton = Button(bottom, text='4', width=8, height=2, bg='white',
                    fg='black', command=lambda: update_entry('4')).grid(row=1, column=0)
fiveButton = Button(bottom, text='5', width=8, height=2, bg='white',
                    fg='black', command=lambda: update_entry('5')).grid(row=1, column=1)
sixButton = Button(bottom, text='6', width=8, height=2, bg='white',
                   fg='black', command=lambda: update_entry('6')).grid(row=1, column=2)
sevenButton = Button(bottom, text='7', width=8, height=2, bg='white', fg='black',
                     command=lambda: update_entry('7')).grid(row=0, column=0)
eightButton = Button(bottom, text='8', width=8, height=2, bg='white', fg='black',
                     command=lambda: update_entry('8')).grid(row=0, column=1)
ninthButton = Button(bottom, text='9', width=8, height=2, bg='white', fg='black',
                     command=lambda: update_entry('9')).grid(row=0, column=2)

decimalButton = Button(bottom, text='.', width=38, height=2, bg='gray',
                       command=lambda: update_entry('.')).grid(row=3, column=3, columnspan=3)
equalButton = Button(bottom, text='=', width=38, height=2, bg='Lightgreen',
                     command=calculate).grid(row=1, column=3, columnspan=3)
plusButton = Button(bottom, text='+', width=8, height=2, bg='gray',
                    command=lambda: update_entry('+')).grid(row=3, column=6, columnspan=3)
minusButton = Button(bottom, text='-', width=8, height=2, bg='gray',
                     command=lambda: update_entry('-')).grid(row=2, column=6, columnspan=3)
multiplyButton = Button(bottom, text='x', width=8, height=2, bg='gray',
                        command=lambda: update_entry('*')).grid(row=1, column=6, columnspan=3)
divideButton = Button(bottom, text='÷', width=8, height=2, bg='gray',
                      command=lambda: update_entry('/')).grid(row=0, column=6, columnspan=3)
clearButton = Button(bottom, text='Clear (CE)', width=38,
                     height=2, command=clear, bg='pink').grid(row=0, column=3, columnspan=3)

shiftButton = Button(bottom, text='Shift', width=15, height=2,
                     command=clear, bg='orange').grid(row=3, column=9, columnspan=3)
graphButton = Button(bottom, text='GRAPH', width=38,
                     height=2, bg='pink', command=drawNumbers).grid(row=2, column=3, columnspan=3)
cosButton = Button(bottom, text='cos', width=15, height=2,
                   bg='skyblue', command=lambda: update_entry("cos")).grid(row=0, column=9, columnspan=3)
sineButton = Button(bottom, text='sin', command=lambda: update_entry("sin"), width=15, height=2,
                    bg='skyblue').grid(row=1, column=9, columnspan=3)
tanButton = Button(bottom, text='tan', width=15, height=2,
                   bg='skyblue', command=lambda: update_entry("tan")).grid(row=2, column=9, columnspan=3)
invCosButton = Button(bottom, text='cos^-1', width=15, height=2,
                      bg='skyblue', command=lambda: update_entry("cos^-1")).grid(row=0, column=12, columnspan=3)
invSineButton = Button(bottom, text='sin^-1', command=lambda: update_entry("sin^-1"), width=15, height=2,
                       bg='skyblue').grid(row=1, column=12, columnspan=3)
invTanButton = Button(bottom, text='tan^-1', width=15, height=2,
                      bg='skyblue', command=lambda: update_entry("tan^-1")).grid(row=2, column=12, columnspan=3)
eButton = Button(bottom, text='e', width=15, height=2,
                 bg='skyblue', command=lambda: update_entry("e")).grid(row=3, column=12, columnspan=3)
sqrtButton = Button(bottom, text='√', width=15, height=2,
                    bg='skyblue', command=lambda: update_entry("√")).grid(row=0, column=16, columnspan=3)
exponButton = Button(bottom, text='^', width=15, height=2,
                     bg='skyblue', command=lambda: update_entry("^")).grid(row=1, column=16, columnspan=3)
upButton = Button(bottom, text='UP', width=15, height=2,
                  bg='skyblue', command=goUp).grid(row=2, column=16, columnspan=3)
downButton = Button(bottom, text='DOWN', width=15, height=2,
                    bg='skyblue', command=goDown).grid(row=3, column=16, columnspan=3)
aButton = Button(bottom, text='A', width=15, height=2,
                 bg='skyblue', command=lambda: update_entry("A")).grid(row=0, column=20, columnspan=3)
bButton = Button(bottom, text='B', width=15, height=2,
                 bg='skyblue', command=lambda: update_entry("B")).grid(row=1, column=20, columnspan=3)
cButton = Button(bottom, text='C', width=15, height=2,
                 bg='skyblue', command=lambda: update_entry("C")).grid(row=2, column=20, columnspan=3)
piButton = Button(bottom, text='π', width=15, height=2,
                  bg='skyblue', command=lambda: update_entry("pi")).grid(row=3, column=20, columnspan=3)
credsButton = Button(top, text='credits', width=10, height=1, bg='gray',
                     command=lambda: display_Credits()).grid(row=2, column=6, sticky=N)

# Locks the parent windows size.
root.maxsize(1500, 1000)
root.minsize(1500, 1000)
root.wm_title("Graphing Calculator | Group 3")
# Parent window's background color:
root.configure(background='white')
