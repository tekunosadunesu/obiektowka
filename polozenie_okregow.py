import math
import matplotlib.pyplot as plt
import numpy as np

a = int(input("Podaj punkt X pierwszego okregu: "))
b = int(input("Podaj punkt Y pierwszego okregu: "))
c = int(input("Podaj promien pierwszego okregu: "))
x = int(input("Podaj punkt X drugiego okregu: "))
y = int(input("Podaj punkt Y drugiego okregu: "))
z = int(input("Podaj promien drugiego okregu: "))

dane1 = [a, b, c]
dane2 = [x, y, z]


def stycznosc(okrag1, okrag2):
    a1 = okrag1[0]
    b1 = okrag1[1]
    r1 = okrag1[2]
    a2 = okrag2[0]
    b2 = okrag2[1]
    r2 = okrag2[2]

    # warunki
    if math.sqrt((a1 - a2) ** 2 + (b1 - b2) ** 2) == math.fabs(round((r2 - r1), 1)):
        plt.title("Okregi styczne wewnetrznie")  # nadaje tytul w zaleznosci od spelnionego waruknu
        print("Okregi styczne wewnetrznie")

    elif math.sqrt((a1 - a2) ** 2 + (b1 - b2) ** 2) == round((r2 + r1), 1):
        plt.title("Okregi styczne zewnetrznie")
        print("Okregi styczne zewnetrznie")

    elif math.sqrt((a1 - a2) ** 2 + (b1 - b2) ** 2) < math.fabs(round((r2 - r1), 1)):
        plt.title("Okregi rozlaczne wewnetrznie")
        print("Okregi rozlaczne wewnetrznie")

    elif math.sqrt((a1 - a2) ** 2 + (b1 - b2) ** 2) > round((r2 + r1), 1):
        plt.title("Okregi rozlaczne zewnetrznie")
        print("Okregi rozlaczne zewnetrznie")

    elif round((r2 + r1), 1) > math.sqrt((a1 - a2) ** 2 + (b1 - b2) ** 2) > math.fabs(round((r2 - r1), 1)):
        plt.title("Okregi przecinajace sie w wdwoch punktach")
        print("Okregi przecinajace sie w wdwoch punktach")

    fi = np.linspace(0, 2 * np.pi, 150)  # zakres od 0 do 2pi, w ilosci 150 punktow

    x1 = a1 + r1 * np.cos(fi)  # rownanie parametryczne okregu
    y1 = b1 + r1 * np.sin(fi)
    x2 = a2 + r2 * np.cos(fi)
    y2 = b2 + r2 * np.sin(fi)

    plt.figure(1)  # utworzenie figury
    plt.axis("equal")  # rowne osie zeby byly rowne okregi
    plt.plot(x1, y1)  # wyswietlanie pierwszego okregu
    plt.plot(x2, y2)
    plt.grid()  # pokazuje siatke
    plt.show()


stycznosc(dane1, dane2)
