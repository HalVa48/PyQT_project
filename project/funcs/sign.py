import sympy as sp

def sign(f):
    # Задаем символьную переменную
    x = sp.symbols('x')
    func = sp.simplify(f)
    # Находим корни уравнения f(x) = 0
    roots = sp.solve(func, x)

    # Сортируем корни, если они существуют
    sorted_roots = sorted(roots, key=lambda i: sp.re(i))

    # Определяем интервалы знакопостоянства
    intervals = []
    last = -sp.oo  # начинаем с минус бесконечности

    for r in sorted_roots:
        midpoint = (last + r) / 2  # берем точку между корнями
        if func.subs(x, midpoint) > 0:  # если значение функции положительное
            sign = "+"
        else:
            sign = "-"
        intervals.append((last, r, sign))
        last = r

    # Проверяем интервал от последнего корня до плюс бесконечности
    midpoint = last + 1
    if func.subs(x, midpoint) > 0:
        sign = "+"
    else:
        sign = "-"
    intervals.append((last, sp.oo, sign))

    res = ''
    # Выводим интервалы знакопостоянства
    for interval in intervals:
        res += f"На интервале ({interval[0]}, {interval[1]}) функция знак {interval[2]}\n"
    return res