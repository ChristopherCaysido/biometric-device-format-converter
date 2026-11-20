import sys
from pathlib import Path
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication,  QMainWindow, QWidget, QPushButton, QHBoxLayout, QFileDialog

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Python Biometric Converter")

        # Created the central QWidget
        centralWidget = QWidget()

        # Created the Open File Button
        openFileButton = QPushButton("Open File")
        openFileButton.clicked.connect(self.openFileToConvert)

        # Created the Convert Button
        button = QPushButton("Convert")
        button.clicked.connect(self.convertBiometricData)

        # Initial Layout
        self.layout = QHBoxLayout()
        self.layout.addWidget(openFileButton)
        centralWidget.setLayout(self.layout)

        # File Dialog
        self.fileToConvert = QFileDialog(self)
        
        # Window Settings
        self.setFixedSize(QSize(400,300))
        self.setCentralWidget(centralWidget)

    def convertBiometricData(self):
        print('Converted Data')
    
    def openFileToConvert(self):
        self.fileToConvert.exec()

    

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()



