#!usr/bin/python

import sys
import math
import random


#Returns true if the argument is a number, otherwise returns false
def isNumber(a):
    try:
        float(a)
        return True #if a cast works
    except:
        return False

#returns a + b, if they are numbers (otherwise returns None)
def addition(a, b):
    if (isNumber(a) and isNumber(b)):
        return a + b
    else:
        sys.stderr.write("Incorrect usage of addition(a,b) function. arithmetic.py")
        return None

#subtracts b from a and returns the resulting value
def subtraction(a, b):
    return addition(a,-b)

#multiplies a and b if they are numeric (otherwise returns None)
def multiplication(a, b):
    if (isNumber(a) and isNumber(b)):
        return a * b
    else:
        sys.stderr.write("Incorrect usage of addition(a,b) function. arithmetic.py")
        return None

#returns a/b if they are numeric (otherwise returns None)
def division(a, b):
    return multiplication(a, 1/b)

#returns the square root of the argument if numeric
#(otherwise returns None)
def squareRoot(a):
    if (isNumber(a)):
        return math.sqrt(a)
    else:
        return None

#returns a^b, if a and b are numeric (otherwise returns None)
def power(a, b):
    if (isNumber(a) and isNumber(b)):
        return pow(a, b)
    else:
        return None

#finds the greatest common denominator of 2 numbers, using Euclid's algorithm
#if either is non-numeric, returns None
def greatestCommonDenominator(a, b):
    if (isNumber(a) and isNumber(b)):
        while b:      
            a, b = b, a % b
        return a
    else:
        return None

#returns the lowest common multiple of 2 numbers
#if either is non-numeric, returns None
def lowestCommonMultiple(a, b):
    if (isNumber(a) and isNumber(b)):
        return a * b // gcd(a, b)
    else:
        return None

#returns lowest common multiple given any amount of arguments
#returns None if any argument is non-numeric
def lowestCommonMultipleMult(*arg):
    for i in arg:
        if (not isNumber(i)):
            return None
    return reduce(lowestCommonMultiple, arg)

#returns sin(x) given X radians
#returns None if X is non-numeric
def trigSine(x):
    if (isNumber(x)):
        return math.sin(x)
    else:
        return None

def trigCosine(x):
    if (isNumber(x)):
        return math.cos(x)
    else:
        return None

#returns tan(x) given X radians
#returns None if X is non-numeric
def trigTan(x):
    if (isNumber(x)):
        return math.tan(x)
    else:
        return None

#returns a random integer, between a low a and a high b
#if a is higher than b, or if either a or b are non-numeric, returns None
def randomInt(a, b):
    if (isNumber(a) and isNumber(b) and (a <= b)):
        return random.randint(a,b)
    else:
        return None

#returns a random integer, between a low x and a high y
#if x is higher than y, or if either x or y are non-numeric, returns None
def randomFloat(x, y):
    if (isNumber(x) and isNumber(y) and (x <= y)):
        return random.uniform(x, y)
    else:
        return None

