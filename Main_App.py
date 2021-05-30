from seat_built import seat_built_detector
from drowsiness_detector import drowsiness_detector
import sys
from PyQt5.QtWidgets import  QTextEdit,QProgressBar ,QMessageBox,QMainWindow,QFormLayout, QApplication,QPushButton,QDialog,QGroupBox,QHBoxLayout,QVBoxLayout,QWidget,QLabel,QLineEdit,QGridLayout,QScrollArea
from PyQt5.QtWidgets import QTextBrowser
from PyQt5 import QtGui,QtCore
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import *
stylesheet = """
    MainWindow {
        background-image: url("D:/back.jpg"); 
        background-repeat: no-repeat; 
        background-position: center;
    }
"""
class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setStyleSheet("")
        self.InitWindow()
        self.show()
    def InitWindow(self):
        myFont = QtGui.QFont('Times', 18)
        myFont.setBold(True)
        self.window().setWindowTitle("Wake Up!")
        self.groupBox = QGroupBox("Welcome to Your Favourite Detector")
        #self.groupBox.setStyleSheet("color=red")
        self.groupBox.setStyleSheet(stylesheet)
        self.groupBox.setFont(QtGui.QFont("Lucida Console", 25))
        self.Main = QFormLayout()
        #  self.centralwidget = QWidget()
        #  self.setCentralWidget(self.centralwidget)
        self.pushButton1 = QPushButton("Drowsiness Detection")
        self.pushButton1.setStyleSheet("color:Blue")
        self.pushButton2 = QPushButton("SeatBuilt Detector")
        self.pushButton2.setStyleSheet("color:Blue")
        self.pushButton1.setFont(myFont)
        self.pushButton1.setIconSize(QtCore.QSize(10, 10))
        self.pushButton1.setGeometry(10, 10, 10, 10)
        self.pushButton1.adjustSize()
        self.pushButton2.setFont(myFont)
        self.pushButton2.setIconSize(QtCore.QSize(40, 40))
        self.pushButton2.setGeometry(20, 20, 20, 20)
        self.pushButton1.clicked.connect(drowsiness_detector)
        self.pushButton2.clicked.connect(seat_built_detector)
        self.pushButton2.adjustSize()
        self.centered_text = QLabel('''
            Choose your Wanted Functionality and Enjoy..
            If you wanted anytime to finish detecting, 
                        just PRESS ESC
            Then you'll be able to choose another Functionality.
                ''')
        self.centered_text.setFont(myFont)
        self.centered_text.setAlignment(QtCore.Qt.AlignHCenter)
        self.centered_text.setStyleSheet("color:red")
        self.container = QVBoxLayout()
        self.container.addWidget(self.centered_text)
        self.Main.addRow(self.container)
        self.Main.addRow(self.pushButton1)
        self.Main.addRow(self.pushButton2)
        self.groupBox.setLayout(self.Main)
        self.vBox = QVBoxLayout()
        self.vBox.addWidget(self.groupBox)
        self.vBox.setAlignment(QtCore.Qt.AlignHCenter)
        self.setStyleSheet(stylesheet)
        self.setLayout(self.vBox)
        self.vBox.addStretch(1)

        #  self.centralwidget = QWidget()
        #  self.setCentralWidget(self.centralwidget)
        self.setStyleSheet("color:black")
        self.show()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    app.setStyleSheet('''background-image: url("D:/back.jpg"); 
        background-repeat: no-repeat; 
        background-position: center;''')     # <---
    window = Window()
    window.resize(400, 400)
    window.show()
    window.setStyleSheet(stylesheet)
    sys.exit(app.exec_())

Window()