from sympy import symbols, S
from sympy.calculus.util import continuous_domain
import sympy as sp

def linear_domain(f):
    # Задаем переменную
    x = symbols('x')
    func = sp.simplify(f)

    # Используем SymPy для нахождения области определения функции
    domain = continuous_domain(func, x, S.Reals)

    # Печатаем результат
    res = [str(i).replace("Interval.open", "") for i in domain.args]
    if res:
        return [str(i).replace("Interval.open", "") for i in domain.args]
    else:
        return "-oo; oo"

def range_of_values(f):
    # Задаем символьную переменную
    x = sp.symbols('x')
    func = sp.simplify(f)
    # Найдем производную функции
    f_prime = sp.diff(func, x)

    # Найдем критические точки, решив f'(x) = 0
    critical_points = sp.solve(f_prime, x)

    # Вычисляем значения функции в критических точках и выбираем экстремальные значения
    extreme_values = [func.subs(x, cp) for cp in critical_points]

    # Если функция непрерывна на всей числовой прямой, проверяем пределы на бесконечности
    limits_at_infinity = [sp.limit(func, x, -sp.oo), sp.limit(func, x, sp.oo)]

    # Объединяем все возможные экстремальные значения
    extreme_values.extend(limits_at_infinity)

    # Область значений функции будет от минимального до максимального из этих значений
    range_of_f = (min(extreme_values), max(extreme_values))

    return range_of_f
