import numpy as np

def sito(N):
    x = np.arange(2, N+1)
    mini = x[0] # pierwsza niezakreślona liczba
    maks = x[-1] # ostatnia, maksmalna liczba


    while(mini<np.sqrt(maks)): # szukamy do pierwiastka z maksymalnej liczby
        for k in range(2, int(np.floor(maks/mini))): # iteujemy przez kolejne mozliwe wielokrotnosci
            num1 = k*mini # wyznaczamy indeks tej wielokrotnosci (mini to nasza aktualna liczba pierwsza)
            x[num1-2]=0 # zerujemy wartosc w tablicy dla wielokrotnosci
        mini=mini+1 # po przejsciu przez wszystkie wielokrotnosci przesuwamy sie na kolejna wielokrotnosc

    # wszystkie wielokonosci zostaly zastapione zerami, wiec mozna znalezc te liczby, ktore sa wieksze niz 0:
    liczby_pierwsze = [xx for xx in x if xx>0]
    return liczby_pierwsze


print(sito(100))
