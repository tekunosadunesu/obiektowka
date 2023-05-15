import numpy as np
import matplotlib.pyplot as plt


class Wielomian:
    def __init__(self):
        self.wspolczynniki = []
        self.dane = []
        self.dane = np.loadtxt("przykladowe_dane.txt")
        self.x = self.dane[:, 0]
        self.y = self.dane[:, 1]

    def wczytaj(self):
        self.wspolczynniki = np.polyfit(self.x, self.y, 2)

        plt.figure()
        # plt.plot(x, y, "o", color="red")
        plt.plot(self.x, self.y, color="yellow")  # plot robi ciagla funkcje
        plt.grid()
        plt.xlabel("Os X")
        plt.ylabel("Os Y")
        plt.title("Wykres jakiejs funkcji")
        plt.legend("cos tam")
        plt.scatter(self.x, self.y, color="blue")  # scatter domyslnie pokazuje kropeczki
        plt.savefig("nowy_plik.png")
        plt.show()

    # def oblicz_wspolczynniki(self):
    #     x = self.dane[:, 0]
    #     y = self.dane[:, 1]
    #
    #     self.wspolczynniki = np.polyfit(x, y, 2)
    #
    #     plt.figure()
    #     plt.plot(x, y, color = "red")
    #     plt.show()


w1 = Wielomian()
w1.wczytaj()
