import numpy as np


liczby = []
ilosc = int(input("Ile liczb chcesz wysolowac?:"))
# ilosc = 10
for j in range(ilosc):
    n = np.random.randint(0, 100)
    liczby.append(n)
print("Lista przed sortowaniem:", liczby)


def sortowanie(lista):
    dlugosc = len(lista)

    for i in range(dlugosc):
        if i < (dlugosc - 1):
            min_wartosc = min(lista[i + 1:])
            if lista[i] > min_wartosc:
                indeks = lista.index(min_wartosc)
                lista[i], lista[indeks] = lista[indeks], lista[i]
    print("Lista po sortowaniu:", lista)


sortowanie(liczby)
