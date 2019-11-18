import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon, QFont

class MWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('images/yezi.png'))

        self.show()

def main():
    app = QApplication(sys.argv)

    widget = QWidget()
    widget.resize(250, 150)
    widget.move(300, 300)
    widget.setWindowTitle('Simple')
    widget.show()

    sys.exit(app.exec_())

def qicon():
    app = QApplication(sys.argv)

    mwidget = MWidget()
    sys.exit(app.exec_())

if __name__ == "__main__":
    qicon()





