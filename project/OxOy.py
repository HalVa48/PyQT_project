from sympy import solveset, symbols
import sympy

def ox(f):
    x = symbols('x')
    return solveset(f, x)

def oy (f):
    x = symbols('x')
    return f.subs(x, 0)