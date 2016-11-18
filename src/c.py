import parser
from math import *

def equate(eqn):
    eqn = eqn.replace(" ", "")
    eqn = eqn.lower()
    a = parser.expr(eqn).compile()
    step = 0.1
    x = step
    for i in range(0, 10):
        print 'answer: ', eval(a), ' step: ', x
        x += step

equate("x")
