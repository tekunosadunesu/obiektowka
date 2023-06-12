from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit
import sys
import numpy as np
import pyqtgraph as pg

def clicked1():
    print("brawo :)")
    button2.setVisible(True)
    button1.setVisible(False)

def funkcja():
    x = np.linspace(-10, 10, 100)
    y = float(a.text()) * x + float(b.text())     # a.text() dziala jak input, pobiera stringa
    print(y)
    wykres.plot(x, y)  # rysuje wykres


app = QApplication([])
widget = QWidget()
widget.setGeometry(0, 0, 500, 500)  # (x, y, rozmiar_okna_X,  rpozmar_okna_y), x, y - polozenie "startowe"

# przycisk 1
button1 = QPushButton(widget)  # tworzenie przycisku
button1.setText("Kliknij :/")  # tekst na przycisku
button1.move(200, 250)  # polozenie przycisku
button1.clicked.connect(clicked1)  # jezeli przycisniety to wywoluje funkcje !!! BEZ NAWIASU !!!

# przycisk 2
button2 = QPushButton(widget)
button2.setText("Oblicz")
button2.move(100, 250)
button2.setVisible(False)  # ustawia przycisk na niewidzialny
button2.clicked.connect(funkcja)

# okienka
a = QLineEdit(widget)
a.setText("5")
a.move(50, 50)

b = QLineEdit(widget)
b.setText("10")
b.move(50, 100)

wykres = pg.PlotWidget(widget)
wykres.setGeometry(250, 300, 600, 600)

widget.setWindowTitle("Aplikacja :)")  # nadaje tytul aplikacji
widget.show()  # pokazuje okno
sys.exit(app.exec_())  # zatrzymuje okineko zeby sie nie zamykalo


# pytania na zasadzie co to jest zmienna, pyatnia o krotki kod, 