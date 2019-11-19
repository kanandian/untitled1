import sys
from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QPushButton, QMessageBox, QDesktopWidget, QMainWindow, QAction, qApp, QLCDNumber, QSlider, QVBoxLayout
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication, Qt


#事件(signals and slots)
class EventWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        lcd = QLCDNumber(self)
        sld = QSlider(Qt.Horizontal, self)

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)

        self.setLayout(vbox)
        sld.valueChanged.connect(lcd.display)


        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Signals and Slots')
        self.show()

    #重写keyPressEvent函数以
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()



# 菜单栏和工具栏
class MMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        #状态栏
        # self.statusBar().showMessage('ready')

        #按钮（普通控件）
        btn = QPushButton('我很帅', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)

        #菜单栏
        exitAct = QAction(QIcon('images/yezi.png'), '&Exit', self)
        exitAct.setShortcut('shift+Q')
        exitAct.setStatusTip('exit application')
        exitAct.triggered.connect(qApp.quit)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAct)
        menubar.setNativeMenuBar(False)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('StatusBar')
        self.show()


class MWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('images/yezi.png'))

        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget</b> widget')

        btn = QPushButton('我很帅', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')

        btn.resize(btn.sizeHint())
        btn.move(50, 50)

        #退出按钮
        quit_btn = QPushButton('quit', self)
        quit_btn.clicked.connect(QCoreApplication.instance().quit)
        quit_btn.resize(quit_btn.sizeHint())
        quit_btn.move(100, 100)

        #移到屏幕中间
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

        self.show()

    #重写关闭应用事件
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', 'Are you sure to quit?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


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

def qmainwindow():
    app = QApplication(sys.argv)
    mainwindow = MMainWindow()
    sys.exit(app.exec_())

def qeventhandle():
    app = QApplication(sys.argv)
    event_widget = EventWidget()
    sys.exit(app.exec_())

if __name__ == "__main__":
    qeventhandle()





