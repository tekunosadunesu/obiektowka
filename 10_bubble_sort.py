import matplotlib.pyplot as plt
import time
from IPython import display


liczby = [5, 1, 100, 3, 6, 2, 4, 15, 67, 24, 5, 0, 12, 54, 66, 0, 7]


def bubble_sort(lista):
    licznik = 5
    while licznik != 0:
        licznik = 0
        for j in range(len(lista) - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                licznik += 1

                plt.clf()
                plt.bar(range(len(lista)), lista)
                display.display(plt.gcf())
                display.clear_output(wait=True)
                time.sleep(0.5)

    print(lista)


bubble_sort(liczby)
