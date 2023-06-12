
import numpy as np


liczby = []
ilosc = int(input("Ile liczb chcesz wysolowac?:"))
#ilosc = 10
for j in range(ilosc):
    n = np.random.randint(0, 100)
    liczby.append(n)
print("Lista przed sortowaniem:", liczby)

def merge_sort(lista):

    # dzielenie listy na pol
    if len(lista) > 1: 
        polowa = int(len(lista) // 2) 
        print(lista)
        prawa_lista = lista[polowa :]
        lewa_lista = lista[: polowa]
        print(lewa_lista, prawa_lista)
        merge_sort(lewa_lista)  # rekurencja
        merge_sort(prawa_lista)
        
        # wstawianie wartosci do koncowej listy
        i = j = k = 0
        while i < len(lewa_lista) and j < len(prawa_lista): 
            if lewa_lista[i] < prawa_lista[j]:
                lista[k] = lewa_lista[i]
                i += 1
                print(lista)
            else:
                lista[k] = prawa_lista[j]
                j = j + 1
                print(lista)
            k += 1

        while i < len(lewa_lista):
            lista[k] = lewa_lista[i]
            i += 1

        while j < len(prawa_lista):
            lista[k] = prawa_lista[j]
            j += 1

        print(lista)


merge_sort(liczby)
