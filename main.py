# ch 4.2.1. main.py

import sys 

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout,QMessageBox
from PyQt5.QtGui import QIcon
class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.btn1 = QPushButton('Message', self)
        self.btn1.clicked.connect(self.activateMessage)

        vbox = QVBoxLayout()
        vbox.addStretch(1) #addStretch = 여백 ,, 윗여백
        vbox.addWidget(self.btn1) #버튼을 가운데로 
        vbox.addStretch(1) #아랫 여백

        self.setLayout(vbox) # 반영

        self.setWindowTitle('계산기')
        # self.setWindowIcon(QIcon(''))
        self.resize(256,256)
        self.show()

    def activateMessage(self) :
        QMessageBox.information(self, 'infomation', "Button Clicked!")

# 이 파일을 직접 실행할 시에만 명령을 수행하겠다.
if __name__=='__main__':
    app = QApplication(sys.argv) # 시스템에서 주어지는 인수를 받아 앱을 켜겠다.
    view = Calculator() # 위에서 만든 Calculator 객체를 생성 하겠다
    sys.exit(app.exec_()) # 창이 꺼질 시 시스템도 끄겠다.

