from PyQt5.QtWidgets import *
from PyQt5 import uic
import time
import sys
import random
class main(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("bedi.ui",self)

        self.pencere()

    def pencere(self):
        self.label_6.setText("Mode : Easy")
        self.mode = "easy"
        self.pushButton.clicked.connect(lambda : self.zorluk(self.radioButton.isChecked(), self.radioButton_2.isChecked(), self.radioButton_3.isChecked(), self.label_6))
        self.pushButton_2.clicked.connect(self.yazdir)
        self.pushButton_3.clicked.connect(self.cevapla)
        self.actionHesapla.triggered.connect(self.cevapla)
        self.pushButton_4.clicked.connect(self.cevabigoster)
        self.radioButton_3.clicked.connect(self.radyo)
        self.label_5.setText("")


        self.show()
        self.e = 5
        self.puan = 0

        self.pushButton_5.clicked.connect(self.exit)
        self.sayac = 0
        self.yazdir()

    def radyo(self):
        print("Bak bu çok zordur ")
    def exit(self):
        print(self.sayac)
        qApp.quit()
    def cevabigoster(self):
        self.lineEdit.setText(self.easyab)
        self.puan -= self.e *2
    def cevapla(self):
        cevap = self.lineEdit.text()

        if self.puan > 500:
            self.setWindowTitle("Mükemmelsin")

        else:
            self.setWindowTitle("Toplama oyunupy")



        if cevap == self.easyab:
            self.label_5.setText("Dogruu :)")
            self.label_5.setStyleSheet("color : lightgreen")
            self.puan += self.e
            self.label_8.setText(str(self.puan))
            self.lineEdit.clear()
            self.yazdir()
            self.sayac +=1

        elif cevap == "puan" or cevap == "PUAN" or cevap == "Puan":
            self.puan +=100
            self.label_5.setStyleSheet("color : cyan")
            self.label_5.setText("+100 PUAN")
            self.label_8.setText(str(self.puan))
        elif cevap == "-puan" or cevap == "puan-":
            self.puan -=100
            self.label_5.setStyleSheet("color : orange")
            self.label_5.setText("-100 PUAN")
            self.label_8.setText(str(self.puan))
        elif cevap == "++puan" or cevap == "puan++":
            self.puan += 1000
            self.label_5.setStyleSheet("color : blue")
            self.label_5.setText("+1000 PUAN!")
            self.label_8.setText(str(self.puan))
        else:
            self.label_5.setText("Yanlis :/")
            self.label_5.setStyleSheet("color: red")
            self.puan -= self.e
            self.label_8.setText(str(self.puan))
            self.lineEdit.clear()
            self.yazdir()
            self.sayac += 1
    def yazdir(self):
        if self.mode == "easy":
            a = random.randint(1, 10)
            b = random.randint(1, 10)
            self.easyab = str(a + b)
            self.label.setText(str(a))
            self.label_2.setText(str(b))
            self.e = 5
        elif self.mode == "normal":
            a = random.randint(10,50)
            b = random.randint(1,10)
            self.easyab = str(a + b)
            self.label.setText(str(a))
            self.label_2.setText(str(b))
            self.e = 15
        elif self.mode == "hard":
            a = random.randint(10, 40)
            b = random.randint(10, 100)
            self.easyab = str(a + b)
            self.label.setText(str(a))
            self.label_2.setText(str(b))
            self.e = 25
    def zorluk(self,radio1,radio2,radio3,label):
        if radio1:
            self.mode = "easy"
            label.setText("Mode : Easy")

        if radio2:
            self.mode = "normal"
            label.setText("Mode : Normal")

        if radio3:
            self.mode = "hard"
            label.setText("Mode : Hard")




app = QApplication(sys.argv)
main = main()
sys.exit(app.exec_())