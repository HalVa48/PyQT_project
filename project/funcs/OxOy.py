from sympy import solveset, symbols
import sympy as sp

def ox(f):
    x = symbols('x')
    func = sp.simplify(f)
    roots = solveset(func, x)
    print(type(roots))
    res = ''
    for i in roots.args:
        res += f'({i}, 0) '
        return res


def oy(f):
    x = symbols('x')
    func = sp.simplify(f)
    return (0, func.subs(x, 0))

ox("x ** 2")