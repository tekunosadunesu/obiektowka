import numpy as np


class Punkt:
    def __init__(self):
        self.x_min =  np.random.uniform(-1, 1)
        self.x_max =  np.random.uniform(-1, 1)

    def czy_w_kole(self):
        a = (self.x_min * self.x_min) + (self.x_max * self.x_max)
        if a <= 1:
            return True
        elif a > 1:
            return False

def gen_pi(n):
    global wynik
    licznik = 0
    for i in range(n):
        los_punkt = Punkt()
        if los_punkt.czy_w_kole():
            licznik += 1

        wynik = 4 * (licznik / n)
    print(wynik)


print(gen_pi(1000))
