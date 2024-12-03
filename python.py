import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.uic import loadUi

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("design.ui", self)
        self.setWindowTitle("MojeDźwięki, Wykonał: 00000000000")

        with open("./data.txt", "r") as file:
            self.data = file.read()

        print(self.data)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec())
