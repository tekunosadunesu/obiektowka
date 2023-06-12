import math


def f(x):
    return (x-5)**3 - 3


przedzial = [-100, 100]
dokladnosc = 0.0001  # dokładność z jaką porównujemy f(x) do 0


def bisekcja(a, b, c):  # a - lewa granica, b - prawa granica, c - dokładność
    if f(a) * f(b) >= 0:
        return "Brak znalezionego pierwiastka w przedziale."

    while math.fabs(b - a) > c:  # działa dopóki różnica jest większa od dokładności
        srodek = (a + b) / 2

        if f(srodek) == 0:  # znalezienie pierwiastka
            return "Pierwiastkiem jest", round(srodek, 2)

        elif f(a) * f(srodek) < 0:
            b = srodek
        else:
            a = srodek

    srodek = (a + b) / 2
    return "Pierwiastkiem jest", round(srodek, 2)


print(bisekcja(przedzial[0], przedzial[1], dokladnosc))
