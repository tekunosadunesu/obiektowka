import numpy as np


class FiguraGeometryczna:
    def __init__(self, promien, bok1, bok2, bok3):
        self.promien = promien
        self.bok1 = bok1
        self.bok2 = bok2
        self.bok3 = bok3
        pass

    def obwod(self):
        pass

    def pole(self):
        pass


class Kolo(FiguraGeometryczna):
    def obwod(self):
        obwod = 2 * 3.14 * self.promien
        return obwod

    def pole(self):
        pole = 3.14 * self.promien * self.promien
        return pole


class Trojkat(FiguraGeometryczna):
    def obwod(self):
        obwod = self.bok1 + self.bok2 + self.bok3
        return obwod

    def pole(self):
        p = 0.5 * (self.bok1 + self.bok2 + self.bok3)
        pole = np.sqrt(p * (p - self.bok1) * (p - self.bok2) * (p - self.bok3))
        return pole


class Prostokat(FiguraGeometryczna):
    def obwod(self):
        obwod = 2 * self.bok1 + 2 * self.bok2
        return obwod

    def pole(self):
        pole = self.bok1 * self.bok2
        return pole


class Kwadrat(FiguraGeometryczna):
    def obwod(self):
        obwod = 4 * self.bok1
        return obwod

    def pole(self):
        pole = self.bok1 * self.bok1
        return pole


print("kolo")
a = int(input("Podaj promien okregu: "))
koleczko = Kolo(a, 0, 0, 0)
print("obwod kola wynosi: ", koleczko.obwod())
print("pole kola wynosi: ", koleczko.pole())

print("trojkat")
a = int(input("Podaj pierwszy bok:  "))
b = int(input("Podaj drugi bok:  "))
c = int(input("Podaj trzeci bok:  "))
trojkacik = Trojkat(0, a, b, c)
print("obwod trojkata wynosi: ", trojkacik.obwod())
print("pole trojkata wynosi: ", trojkacik.pole())

print("prostokat")
a = int(input("Podaj pierwszy bok:  "))
b = int(input("Podaj drugi bok:  "))
prostokacik = Prostokat(0, a, b, 0)
print("obwod prostokata wynosi: ", prostokacik.obwod())
print("pole prostokata wynosi: ", prostokacik.pole())

print("kwadrat")
a = int(input("Podaj bok:  "))
kwadracik = Kwadrat(0, a, 0, 0)
print("obwod kwadratu wynosi: ", kwadracik.obwod())
print("pole kwadratu wynosi: ", kwadracik.pole())
