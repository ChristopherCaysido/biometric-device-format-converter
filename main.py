import sys
from pathlib import Path
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication,  QMainWindow, QWidget, QPushButton, QVBoxLayout, QFileDialog

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Python Biometric Converter")

        button = QPushButton("Convert")
        button.clicked.connect(self.convertBiometricData)

        openFileButton = QPushButton("Open File")
        self.fileToConvert = QFileDialog(self)
        self.setFixedSize(QSize(400,300))

        self.setCentralWidget(button)
    def convertBiometricData(self):
        print('Converted Data')

    

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()



