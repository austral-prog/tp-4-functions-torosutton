import math
def roots(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant > 0:
        raiz_1 = (-b + (discriminant ** 0.5)) / (2 * a)
        raiz_2 = (-b - (discriminant ** 0.5)) / (2 * a)

        return (f"({raiz_1}, {raiz_2})")

    elif discriminant == 0:
        raiz = (-b - discriminant ** 0.5) / (2 * a)

        return (f"({raiz})")

    else:

        return ("( )")





def value_y(a, b, c, x):
    return ( (a * (x**2) + (b * x) + c ) )




def to_string(a, b, c):

    if a !=0 and b != 0 and c != 0:
        return (f"f(x) = {a} * X^2 + {b} * X + {c}")

    elif a != 0 and b != 0 and c == 0:
        return (f"f'(x) = {a} * X^2 + {b} * X")

    elif a != 0 and b == 0 and c != 0:
        return (f"f(x) = {a} * X^2 + {c}")

    elif a != 0 and b == 0 and c == 0:
        return (f"f(x) = {a} * X^2")

    elif a == 0 and b != 0 and c != 0:
        return (f"f(x) = {b} * X + {c}")

    elif a == 0 and b != 0 and c == 0:
        return (f"f(x) = {b} * X")

    else:
        return (f"f(x) = {c}")




def derivation(a, b, c):
    a = a * 2

    if a != 0 and b != 0:
        return (f"f'(x) = {a} * X + {b}")

    elif a!= 0 and b == 0:
        return (f"f'(x) = {a} * X")

    elif a == 0:
        return (f"f'(x) = {b}")