from PyQt5.QtWidgets import *#QApplications,QMainwindow,QPushButton
from PyQt5.QtGui import *
from PyQt5.QtCore import *#QTime
import sys
class Stopwatch(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Stop Watch")
        self.setGeometry(0,0,500,500)
        self.UiComponents()
        self.show()
    def UiComponents(self):
        
        self.count=0
        self.flag=False
        self.label=QLabel(self)
        self.label.setGeometry(75,100,250,70)
        self.label.setStyleSheet("border:4px solid black")


        self.label.setText(str(self.count))
        self.label.setFont(QFont("arial",25))
        self.label.setAlignment(Qt.AlignCenter)

        start=QPushButton("Start",self)
        start.setGeometry(125,250,150,40)
        start.pressed.connect(self.start)

        pause=QPushButton("Pause",self)
        pause.setGeometry(125,300,150,40)
        pause.pressed.connect(self.pause)

        reset=QPushButton("Reset",self)
        reset.setGeometry(125,350,150,40)
        reset.pressed.connect(self.reset)

        timer=QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(100)


    def start(self):
        print("pressing start button")
        self.flag=True
    
    def pause(self):
        print("pressing pause button")
        self.flag=False

    def reset(self):
        print("pressing reset button")
        self.flag=False
        self.count=0

    def showTime(self):
        if(self.flag):
            self.count=self.count+1
        text=self.count/10
        self.label.setText(str(text))

app=QApplication(sys.argv)
win=Stopwatch()
win.show()
exit(app.exec_())