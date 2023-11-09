from sympy import symbols, S
from sympy.calculus.util import continuous_domain

def linear_domain(f):
    # Задаем переменную
    x = symbols('x')

    # Используем SymPy для нахождения области определения функции
    domain = continuous_domain(f, x, S.Reals)

    # Печатаем результат
    return [str(i).replace("Interval.open", "") for i in domain.args]

