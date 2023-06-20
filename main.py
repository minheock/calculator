# ch 4.2.1. main.py

import sys 

from PyQt5.QtWidgets import QApplication, QWidget

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('계산기')
        self.resize(256,256)
        self.show()

# 이 파일을 직접 실행할 시에만 명령을 수행하겠다.
if __name__=='__main__':
    app = QApplication(sys.argv) # 시스템에서 주어지는 인수를 받아 앱을 켜겠다.
    view = Calculator() # 위에서 만든 Calculator 객체를 생성 하겠다
    sys.exit(app.exec_()) # 창이 꺼질 시 시스템도 끄겠다.

