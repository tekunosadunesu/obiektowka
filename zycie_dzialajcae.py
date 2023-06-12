import numpy as np
import matplotlib.pyplot as plt

def zycie(wiersze, kolumny, cykle):
    # tworzenie planszy z randomowymi wartosciami
    pierwotna_tab = np.random.randint(low=0, high=2, size=(wiersze, kolumny))

    # zmiana wartosci 1 na 255, zeby bylo ladnie widac pozniej
    pierwotna_tab[pierwotna_tab == 1] = 255
    print(pierwotna_tab)

    for cykl in range(cykle):
        tab = pierwotna_tab

        for i in range(wiersze):
            for j in range(kolumny):
                sasiad = 0
                # sprawdzanie czy sa zyjacy sasiedzi

                # lewy gorny rog
                if i == 0 and j == 0:
                    if tab[i][j + 1] == 255:
                        sasiad += 1
                    if tab[i + 1][j] == 255:
                        sasiad += 1
                    if tab[i + 1][j + 1] == 255:
                        sasiad += 1

                # prawy gorny rog
                elif i == 0 and j == kolumny - 1:
                    if tab[i][j - 1] == 255:
                        sasiad += 1
                    if tab[i + 1][j - 1] == 255:
                        sasiad += 1
                    if tab[i + 1][j] == 255:
                        sasiad += 1

                # lewy dolny rog
                elif i == wiersze - 1 and j == 0:
                    if tab[i - 1][j] == 255:
                        sasiad += 1
                    if tab[i - 1][j + 1] == 255:
                        sasiad += 1
                    if tab[i][j + 1] == 255:
                        sasiad += 1

                # prawy dolny rog
                elif i == wiersze - 1 and j == kolumny - 1:
                    if tab[i - 1][j - 1] == 255:
                        sasiad += 1
                    if tab[i - 1][j] == 255:
                        sasiad += 1
                    if tab[i][j - 1] == 255:
                        sasiad += 1

                # gorne krawedzie
                elif i == 0:
                    if tab[i][j - 1] == 255:
                        sasiad += 1
                    if tab[i][j + 1] == 255:
                        sasiad += 1
                    if tab[i + 1][j - 1] == 255:
                        sasiad += 1
                    if tab[i + 1][j] == 255:
                        sasiad += 1
                    if tab[i + 1][j + 1] == 255:
                        sasiad += 1

                # dolne krawedzie
                elif i == wiersze - 1:
                    if tab[i][j - 1] == 255:
                        sasiad += 1
                    if tab[i][j + 1] == 255:
                        sasiad += 1
                    if tab[i - 1][j - 1] == 255:
                        sasiad += 1
                    if tab[i - 1][j] == 255:
                        sasiad += 1
                    if tab[i - 1][j + 1] == 255:
                        sasiad += 1

                # lewe krawedzie
                elif j == 0:
                    if tab[i - 1][j] == 255:
                        sasiad += 1
                    if tab[i - 1][j + 1] == 255:
                        sasiad += 1
                    if tab[i][j + 1] == 255:
                        sasiad += 1
                    if tab[i + 1][j] == 255:
                        sasiad += 1
                    if tab[i + 1][j + 1] == 255:
                        sasiad += 1

                # prawe krawedzie
                elif j == kolumny - 1:
                    if tab[i - 1][j - 1] == 255:
                        sasiad += 1
                    if tab[i - 1][j] == 255:
                        sasiad += 1
                    if tab[i][j - 1] == 255:
                        sasiad += 1
                    if tab[i + 1][j - 1] == 255:
                        sasiad += 1
                    if tab[i + 1][j] == 255:
                        sasiad += 1

                # srodkowe
                else:
                    if tab[i - 1][j - 1] == 255:
                        sasiad += 1
                    if tab[i - 1][j] == 255:
                        sasiad += 1
                    if tab[i - 1][j + 1] == 255:
                        sasiad += 1
                    if tab[i][j - 1] == 255:
                        sasiad += 1
                    if tab[i][j + 1] == 255:
                        sasiad += 1
                    if tab[i + 1][j - 1] == 255:
                        sasiad += 1
                    if tab[i + 1][j] == 255:
                        sasiad += 1
                    if tab[i + 1][j + 1] == 255:
                        sasiad += 1

                # jesli komorka ma trzech sasiadow to ozyje, jesli nie to pozostanie martwa
                if tab[i][j] == 0:
                    if sasiad == 3:
                        tab[i][j] = 255
                    else:
                        tab[i][j] = 0

                # jesli zyjaca komorka ma 2 lub 3 sasiadow to pozostanie zywa
                if tab[i][j] == 255:
                    if sasiad < 2 or sasiad > 3:
                        tab[i][j] = 0

        # animacja
        plt.pause(0.5)
        plt.clf()
        plt.imshow(tab)
        plt.title("Pokolenie" + " " + str(cykl+1))
    plt.show()

zycie(50, 50, 100)
