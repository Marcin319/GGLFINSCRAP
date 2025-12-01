from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QPushButton, 
    QGridLayout, QLineEdit, QPlainTextEdit, QListWidget,
    QStackedWidget, QVBoxLayout, QDateTimeEdit
    )
from PyQt5.QtCore import Qt
import logic as lg

class OknoGlowne(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 200, 700, 700)
        self.setWindowTitle("GOOGLE FINANCE SCRAPPER")


        #self.setup_ui()

    #def setup_ui(self):

        #---CENTRAL WIDGET---
        central = QWidget()
        self.setCentralWidget(central)

        main_layout = QVBoxLayout()
        central.setLayout(main_layout)

        self.stacked = QStackedWidget()
        main_layout.addWidget(self.stacked)

        self.strona_glowna = StronaGlowna(self.stacked)
        self.strona_ustawien_danych = StronaDane(self.stacked)

        #---STACK---
        self.stacked.addWidget(self.strona_glowna)
        self.stacked.addWidget(self.strona_ustawien_danych)


class StronaGlowna(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()

        self.stacked_widget = stacked_widget

        #---LAYOUT---
        layout = QGridLayout()
        self.setLayout(layout)

        #Napis mówiący, czy użytkownik jest online
        self.napis = QLabel(lg.czy_online())
        layout.addWidget(self.napis, 0, 0)

        #Przycisk do odświeżania statusu online
        button = QPushButton("Refresh connection status")
        layout.addWidget(button, 0, 1)

        #Napis mówiący, czy użytkownik jest online
        self.napis = QLabel("Name (Ticket)")
        layout.addWidget(self.napis, 0, 4, 1, 1)
            
        #Konsola
        self.console = QPlainTextEdit()
        self.console.setReadOnly(True)
        layout.addWidget(self.console, 1, 0, 3, 3)

        #Lista ticketów
        self.list = QListWidget()
        layout.addWidget(self.list, 1, 4, 3, 1)

        #Pole tekstowe (do inputu użytkownika)
        self.inputText = QLineEdit(self)
        layout.addWidget(self.inputText, 4, 0, 1, 3)

        #Przycisk do pobierania tekstu z inputu
        self.button2 = QPushButton("FIND BY TICKER")
        layout.addWidget(self.button2, 5, 0)

        self.przycisk_ustawienia = QPushButton("Przejdź do ustawień")
        layout.addWidget(self.przycisk_ustawienia, 5, 1)
        self.przycisk_ustawienia.clicked.connect(
             lambda: self.stacked_widget.setCurrentIndex(1)
        )

        self.adjustSize()

        self.setLayout(layout)

class StronaDane(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()

        self.stacked_widget = stacked_widget

        layout = QGridLayout()
        self.setLayout(layout)

        self.datetime_beggining_cap = QLabel("Beggining of time series")
        layout.addWidget(self.datetime_beggining_cap, 0, 0)

        self.datetime_end_cap = QLabel("End of time series")
        layout.addWidget(self.datetime_end_cap, 0, 1)

        self.datetime_beggining = QDateTimeEdit(self, calendarPopup = True)
        layout.addWidget(self.datetime_beggining, 1, 0)

        self.przycisk_powrot = QPushButton("Cancel")
        layout.addWidget(self.przycisk_powrot, 2, 0)

        self.przycisk_powrot.clicked.connect(
             lambda: self.stacked_widget.setCurrentIndex(0)
        )

        self.adjustSize()
    
    def update(self):
        value = self.datetime_beggining.dateTime()
        self.result_label.setText(value.toString("yyyy-MM-dd"))
        