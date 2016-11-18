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

# global stack
emptyStack = []


def startText():
    path = "0"
    while(not path == "q"):

        path = raw_input("Enter the type of operation you want to perform.\n"
                         "1 - Calculate solution\n"
                         "2 - Graph Equation\n")
        if (path == "1"):
            equation = raw_input("Enter the equation:\n")
            global emptyStack
            emptyStack = []
            ans = BNF().parseString(equation)
            ans = evaluateStack(emptyStack[:])
            print str(ans)
        else:
            equation = raw_input("Enter the equation X:\n")
            minX = raw_input("Enter X1 (min range):\n")
            maxX = raw_input("Enter X2 (max range):\n")
            deltaX = raw_input("Enter the delta X (step):\n")
            global emptyStack
            for x in np.arange(float(minX), float(maxX), float(deltaX)):  # x1,x2,step
                equation = equation.replace("x", str(x))
                global emptyStack
                emptyStack = []
                ans = BNF().parseString(equation)
                ans = evaluateStack(emptyStack[:])
                print '(',x,',',ans,')'


def pushFirst( strg, loc, toks ):
    emptyStack.append( toks[0] )
def pushUMinus( strg, loc, toks ):
    if toks and toks[0]=='-':
        emptyStack.append( 'unary -' )
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
        point = Literal( "." )
        e     = CaselessLiteral( "E" )
        fnumber = Combine( Word( "+-"+nums, nums ) +
                           Optional( point + Optional( Word( nums ) ) ) +
                           Optional( e + Word( "+-"+nums, nums ) ) )
        ident = Word(alphas, alphas+nums+"_$")

        plus  = Literal( "+" )
        minus = Literal( "-" )
        mult  = Literal( "*" )
        div   = Literal( "/" )
        lpar  = Literal( "(" ).suppress()
        rpar  = Literal( ")" ).suppress()
        addop  = plus | minus
        multop = mult | div
        expop = Literal( "^" )
        pi    = CaselessLiteral( "PI" )

        expr = Forward()
        atom = (Optional("-") + ( pi | e | fnumber | ident + lpar + expr + rpar ).setParseAction( pushFirst ) | ( lpar + expr.suppress() + rpar )).setParseAction(pushUMinus)

        # by defining exponentiation as "atom [ ^ factor ]..." instead of "atom [ ^ atom ]...", we get right-to-left exponents, instead of left-to-righ
        # that is, 2^3^2 = 2^(3^2), not (2^3)^2.
        factor = Forward()
        factor << atom + ZeroOrMore( ( expop + factor ).setParseAction( pushFirst ) )

        term = factor + ZeroOrMore( ( multop + factor ).setParseAction( pushFirst ) )
        expr << term + ZeroOrMore( ( addop + term ).setParseAction( pushFirst ) )
        bnf = expr
    return bnf

# map operator symbols to corresponding arithmetic operations
epsilon = 1e-12
opn = { "+" : operator.add,
        "-" : operator.sub,
        "*" : operator.mul,
        "/" : operator.truediv,
        "^" : operator.pow }
fn  = { "sin" : math.sin,
        "cos" : math.cos,
        "tan" : math.tan,
        "abs" : abs,
        "trunc" : lambda a: int(a),
        "round" : round,
        "sgn" : lambda a: abs(a)>epsilon and cmp(a,0) or 0}
def evaluateStack( s ):
    op = s.pop()
    if op == 'unary -':
        return -evaluateStack( s )
    if op in "+-*/^":
        op2 = evaluateStack( s )
        op1 = evaluateStack( s )
        return opn[op]( op1, op2 )
    elif op == "PI":
        return math.pi # 3.1415926535
    elif op == "E":
        return math.e  # 2.718281828
    elif op in fn:
        return fn[op]( evaluateStack( s ) )
    elif op[0].isalpha():
        return 0
    else:
        return float( op )
