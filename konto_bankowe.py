import numpy as np


class KontoBankowe:
    def __init__(self, imie, nazwisko, pesel):
        self.imie = imie
        self.nazwisko = nazwisko
        self.__nr_konta = np.random.randint(10000, 99999)
        self.__saldo = 0
        self.__transakcja = []

    def wyswietlanie_salda(self):
        print("Twoje saldo:", self.__saldo, "zl")

    def wyswietlanie_historii(self):
        print(self.__transakcja)

    def wplata(self, kwota_wplaty):
        self.__saldo = self.__saldo + kwota_wplaty
        self.__transakcja.append(["wplata pieniedzy: ", kwota_wplaty])

    def wyplata(self, kwota_wyplaty):
        if self.__saldo >= kwota_wyplaty:
            self.__saldo = self.__saldo - kwota_wyplaty
            self.__transakcja.append(["wyplata pieniedzy: ", kwota_wyplaty])

        elif self.__saldo < kwota_wyplaty:
            self.__transakcja.append(["NIEUDANA wyplata pieniedzy"])
            print("Nie masz pieniedzy")

    def nr_konta(self):
        print("Numer konta to:", self.__nr_konta)

    def przelew(self, docelowe, kwota):
        if kwota <= self.__saldo:
            self.__saldo = self.__saldo - kwota
            self.__transakcja.append(["przelew pieniedzy: ", kwota])
            docelowe.wplata(kwota)

        else:
            self.__transakcja.append(["NIEUDANy przelew"])
            print("Nie masz pieniedzy")


konto1 = KontoBankowe("Jan", "Kowalski", 165276)
konto2 = KontoBankowe("Maria", "Nowak", 668372)

konto1.wplata(1600)
konto1.wyplata(600)
# konto1.wplata(1)
# konto1.wyplata(50)
# konto1.wplata(500)
# konto1.wyplata(600)
# konto1.wyswietlanie_salda()
# konto1.wyswietlanie_historii()
konto1.wyswietlanie_salda()
konto1.przelew(konto2, 100)
konto1.wyswietlanie_historii()
konto2.wyswietlanie_salda()
konto2.wyswietlanie_historii()

# przelew





















# def menu():
#     print("1) Wyswietl saldo")
#     print("2) Wplata pieniedzy")
#     print("3) Wyplata pieniedzy")
#     print("4) Historia")
#     print("99) Wyjscie")
#
# print("1)", konto1.imie, konto1.nazwisko)
# print("2)", konto2.imie, konto2.nazwisko)
# x = int(input("Wybierz konto: "))
#
# if x == 1:
#     n = 0
#     while n != 99:
#         print(" ")
#         menu()
#         n = int(input("Wybierz opcje: "))
#         if n == 1:
#             konto1.wyswietlanie_salda()
#
#         if n == 2:
#             a = int(input("Ile chcesz wplacic?: "))
#             konto1.wplata(a)
#
#         if n == 3:
#             b = int(input("Ile chcesz wyplacic?: "))
#             konto1.wyplata(b)
