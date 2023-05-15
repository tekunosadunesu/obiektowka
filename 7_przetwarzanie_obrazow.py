import matplotlib.pyplot as plt
import numpy as np

obraz = plt.imread("Australia.jpg")  # wczytuje obraz
print(obraz.shape)  # wyswietla (wiersze, kolumny, liczbe warswt kolorow)

x = obraz.shape[0]  # wiersze
y = obraz.shape[1]  # kolumny

print("Rozmiary obrazu:", x, "x", y)
nowy_x = int(input("Podaj jaki procent wierszy chcesz wyswietlic: "))
if nowy_x > 100 or nowy_x < 0:
    print("Bledna wartosc, nie moze byc wieksze niz 100% oraz mniejsze niz 0%")
else:
    nowy_x = (nowy_x / 100) * x  # zmienia podana wartosc nowego x z procent na liczbe
    nowy_x = int(nowy_x)

nowy_y = int(input("Podaj jaki procent kolumn chcesz wyswietlic: "))  # tak samo jak z nowy_x
if nowy_y > 100 or nowy_y < 0:
    print("Bledna wartosc, nie moze byc wieksze niz 100% oraz mniejsze niz 0%")
else:
    nowy_y = (nowy_y / 100) * y
    nowy_y = int(nowy_y)

print("Nowe wymiary obrazu to: ", nowy_x, "x", nowy_y)
nowy_obraz = obraz[:nowy_x - 1, :nowy_y - 1, :]  # podstawia do nowego obrazu nowe wymiary, indeksy o -1, poniewaz sa numerowane od 0

# dzieli na trzy  warstwy kolorow
red = nowy_obraz[:, :, 0]  # 0 poniwaz jest to pierwszy kolor w RGB
green = nowy_obraz[:, :, 1]  # 1 poniewaz drugi kolor
blue = nowy_obraz[:, :, 2]  # analogicznie do tamtych
# fig, ax = plt.subplots(1, 4, figsize=[15, 7])  # tworzy 1 rzad, 4 wykresow, w dany rozmiarze (1 - "wiersze", 4 - "kolumny, figsize - "rozmiar"
# ax[0].imshow(red, cmap="gray")  # pierwszy wykres
# ax[0].set_title("Czerwony")  # dodaje tytul wykresu
# ax[1].imshow(green, cmap="gray")  # drugi wykres
# ax[1].set_title("Zielony")
# ax[2].imshow(blue, cmap="gray")  # trzeci wykres
# ax[2].set_title("Niebieski")
# ax[3].set_title("Oryginalny")  # czwarty wykres to zwykly obraz
# fig.suptitle("RGB w odcieniach szarosci")  # dodaje tytyl figurze

# lab 8
[hist1, edges1] = np.histogram(red, bins=40, range=(0, 255))  # bins-ile mamy przedzialow
hist2, edges2 = np.histogram(green, bins=40, range=(0, 255))
hist3, edges3 = np.histogram(blue, bins=40, range=(0, 255))

# histogramy osobno
# fig, ax = plt.subplots(1, 1)
# ax[0].bar(edges1[0:-1], hist1, color="red", width=6)
# ax[0].bar(edges2[0:-1], hist2, color="green", width=6)
# ax[0].bar(edges3[0:-1], hist3, color="blue", width=6)

# histogramy razem
plt.figure()
plt.bar(edges1[0:-1], hist1, color="red", width=6, alpha=0.5)
plt.bar(edges2[0:-1], hist2, color="green", width=6, alpha=0.5)
plt.bar(edges3[0:-1], hist3, color="blue", width=6, alpha=0.5)
# plt.imshow(nowy_obraz)
plt.show()
