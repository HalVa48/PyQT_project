from sympy import symbols, diff, solveset, S, oo
import sympy


def monotonicity_intervals(func):
    x = symbols('x')
    f = sympy.sympify(func)

    # calculate the first derivative
    df = diff(f, x)

    # find the extrema by solving df(x) = 0
    extrema = list(solveset(df, x, domain=S.Reals))

    # add infinities to the list
    extrema.append(-oo)
    extrema.append(oo)
    extrema.sort()

    intervals = []

    for i in range(len(extrema) - 1):
        # get the middle of each interval
        mid = (extrema[i] + extrema[i + 1]) / 2

        # check the sign of the derivative in the middle of the interval
        result = df.subs(x, mid)
        if not result == sympy.nan:
            if result > 0:
                intervals.append((extrema[i], extrema[i + 1], 'increasing'))
            else:
                intervals.append((extrema[i], extrema[i + 1], 'decreasing'))

    return intervals



