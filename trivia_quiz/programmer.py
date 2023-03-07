import sys
from PyQt5.QtWidgets import QApplication, QLabel, QGridLayout, QPushButton, QVBoxLayout, QWidget, QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor
    
from functions import frame1, frame2, frame3, frame4, grid



app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Quiz game")
window.setFixedWidth(1200)
window.move(630, 200)
window.setStyleSheet("background: #161219;")

frame1()


window.setLayout(grid)

window.show()
sys.exit(app.exec())
