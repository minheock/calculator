# ch 4.2.1. main.py

import sys 

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout,QMessageBox, QPlainTextEdit, QHBoxLayout
from PyQt5.QtGui import QIcon

import random # 내 맘대로 로또 추첨 기능 추가할래


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.te1 = QPlainTextEdit()
        self.te1.setReadOnly(True)

        self.btn1 = QPushButton('Message', self)
        self.btn1.clicked.connect(self.activateMessage)
        self.btn2 = QPushButton('Clear', self)
        self.btn2.clicked.connect(self.clearMessage)
        #수평
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.btn1)
        hbox.addWidget(self.btn2)
        #수직
        vbox = QVBoxLayout()
        vbox.addWidget(self.te1) 
        vbox.addLayout(hbox) #버튼을 가운데로 
        vbox.addStretch(1) #아랫 여백

        self.setLayout(vbox) # 반영

        self.setWindowTitle('로또번호 추첨기')
        # self.setWindowIcon(QIcon(''))
        self.resize(256,256)
        self.show()

    def activateMessage(self) :
        lottoNum = random.sample(range(1,46), 6)
        lottoNum.sort() # 오름차순 정렬
        self.te1.appendPlainText(str(lottoNum))
    def clearMessage(self):
        self.te1.clear()    

# 이 파일을 직접 실행할 시에만 명령을 수행하겠다.
if __name__=='__main__':
    app = QApplication(sys.argv) # 시스템에서 주어지는 인수를 받아 앱을 켜겠다.
    view = Calculator() # 위에서 만든 Calculator 객체를 생성 하겠다
    sys.exit(app.exec_()) # 창이 꺼질 시 시스템도 끄겠다.

