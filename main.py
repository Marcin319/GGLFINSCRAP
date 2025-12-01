import logic as lg
import sys
from PyQt5.QtWidgets import QApplication
import gui

tlm = lg.TicketListManager("ticketList.csv")

app = QApplication(sys.argv)
okno = gui.OknoGlowne()
okno.show()

okno.strona_glowna.console.appendPlainText(tlm.ticketListCSV())

for i in zip(tlm.ticketList["Name"], tlm.ticketList["Ticket"]):
    okno.strona_glowna.list.addItem(f"{i[0]} ({i[1]})")

def item_click(item):
    input_from_list = item.text()
    ticket = input_from_list[input_from_list.find("(")+1:input_from_list.find(")")]
    okno.strona_glowna.inputText.clear()
    okno.strona_glowna.inputText.insert(ticket)

okno.strona_glowna.list.itemClicked.connect(item_click)

okno.strona_glowna.button2.clicked.connect(lambda: print(okno.strona_glowna.inputText.text()))

sys.exit(app.exec_())

