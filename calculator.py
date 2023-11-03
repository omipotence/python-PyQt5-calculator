import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QHBoxLayout, QVBoxLayout, QGridLayout

calc = QApplication([])
window = QWidget()
layout = QGridLayout()
num1 = 0
num2 = 0
numfin = 0
class Window(QWidget):
    def __init__(self):
        global num1, num2, numfin
        super().__init__()
        self.setWindowTitle("Calculator")
        self.l1 = QLabel()
        self.l2 = QLabel()
        self.l1.setText("")
        self.l2.setText("")
        self.num1 = 0
        self.num2 = 0
        self.numfin = 0
        outerlayout = QVBoxLayout()
        outerlayout.addWidget(self.l1)
        outerlayout.addWidget(self.l2)

        self.C = QPushButton("C")
        self.C.clicked.connect(self.C_clicked)
        layout.addWidget(self.C , 0, 0)

        self.back = QPushButton("del")
        self.back.clicked.connect(self.back_clicked)
        layout.addWidget(self.back, 0, 1)

        self.div = QPushButton("/")
        self.div.clicked.connect(self.div_clicked)
        layout.addWidget(self.div , 0, 2)

        self.b1 = QPushButton("1")
        self.b1.clicked.connect(self.b1_clicked)
        layout.addWidget(self.b1 , 1, 0)

        self.b2 = QPushButton("2")
        self.b2.clicked.connect(self.b2_clicked)
        layout.addWidget(self.b2 , 1, 1)

        self.b3 = QPushButton("3")
        self.b3.clicked.connect(self.b3_clicked)
        layout.addWidget(self.b3 , 1, 2)

        self.mult = QPushButton("*")
        self.mult.clicked.connect(self.mult_clicked)
        layout.addWidget(self.mult , 1, 3)

        self.b4 = QPushButton("4")
        self.b4.clicked.connect(self.b4_clicked)
        layout.addWidget(self.b4 , 2, 0)

        self.b5 = QPushButton("5")
        self.b5.clicked.connect(self.b5_clicked)
        layout.addWidget(self.b5, 2, 1)

        self.b6 = QPushButton("6")
        self.b6.clicked.connect(self.b6_clicked)
        layout.addWidget(self.b6 , 2, 2)

        self.minus = QPushButton("-")
        self.minus.clicked.connect(self.minus_clicked)
        layout.addWidget(self.minus , 2, 3)

        self.b7 = QPushButton("7")
        self.b7.clicked.connect(self.b7_clicked)
        layout.addWidget(self.b7 , 3, 0)

        self.b8 = QPushButton("8")
        self.b8.clicked.connect(self.b8_clicked)
        layout.addWidget(self.b8 , 3, 1)

        self.b9 = QPushButton("9")
        self.b9.clicked.connect(self.b9_clicked)
        layout.addWidget(self.b9 , 3, 2)

        self.plus = QPushButton("+")
        self.plus.clicked.connect(self.plus_clicked)
        layout.addWidget(self.plus, 3, 3)
        
        self.b0 = QPushButton("0")
        self.b0.clicked.connect(self.b0_clicked)
        layout.addWidget(self.b0 , 4, 1)

        self.dot = QPushButton(".")
        self.dot.clicked.connect(self.dot_clicked)
        layout.addWidget(self.dot, 4, 2)

        self.res = QPushButton("=")
        self.res.clicked.connect(self.res_clicked)
        layout.addWidget(self.res, 4, 3)
        
        outerlayout.addLayout(layout)

        self.setLayout(outerlayout)
        print(self.children)
        num1 = self.l1.text()
    
    def b1_clicked(self):
        self.l1.setText(self.l1.text() + "1")
    
    def b2_clicked(self):
        self.l1.setText(self.l1.text() + "2")

    def b3_clicked(self):
        self.l1.setText(self.l1.text() + "3")

    def b4_clicked(self):
        self.l1.setText(self.l1.text() + "4")

    def b5_clicked(self):
        self.l1.setText(self.l1.text() + "5")

    def b6_clicked(self):
        self.l1.setText(self.l1.text() + "6")

    def b7_clicked(self):
        self.l1.setText(self.l1.text() + "7")

    def b8_clicked(self):
        self.l1.setText(self.l1.text() + "8")

    def b9_clicked(self):
        self.l1.setText(self.l1.text() + "9")

    def b0_clicked(self):  
        self.l1.setText(self.l1.text() + "0")
    
    def C_clicked(self):
        self.l1.setText("")
        self.l2.setText("")
    
    def back_clicked(self):
        if self.l1.text():
            self.l1.setText(self.l1.text()[:-1])

    def div_clicked(self):
        global num1
        if "/" not in self.l1.text() and "/" not in self.l2.text():
            num1 = self.l1.text()
            self.l2.setText(self.l1.text() + " /")
            self.l1.setText("")


    def mult_clicked(self):
        global num1
        if "*" not in self.l1.text() and "*" not in self.l2.text():
            num1 = self.l1.text()
            self.l2.setText(self.l1.text() + " *")
            self.l1.setText("")

    def minus_clicked(self):
        global num1
        if "-" not in self.l1.text() and "-" not in self.l2.text():
            num1 = self.l1.text()
            self.l2.setText(self.l1.text() + " -")
            self.l1.setText("")

    def plus_clicked(self):
        global num1
        if "+" not in self.l1.text() and "+" not in self.l2.text():
            num1 = self.l1.text()
            self.l2.setText(self.l1.text() + " +")
            self.l1.setText("")
    
    def dot_clicked(self):
        if "." not in self.l1.text():
            self.l1.setText(self.l1.text() + ".")
    
    def res_clicked(self):
        global num1, num2
        if self.l1.text():
            if "+" not in self.l2.text() and "-" not in self.l2.text() and "/" not in self.l2.text() and "*" not in self.l2.text():
                print("")
            elif "+" in self.l2.text():
                num2 = self.l1.text()
                self.l1.setText("")
                numfin = float(num1) + float(num2)
                self.l2.setText(str(numfin))
            elif "-" in self.l2.text():
                num2 = self.l1.text()
                self.l1.setText("")
                numfin = float(num1) - float(num2)
                self.l2.setText(str(numfin))
            elif "*" in self.l2.text():
                num2 = self.l1.text()
                self.l1.setText("")
                numfin = float(num1) * float(num2)
                self.l2.setText(str(numfin))
            elif "/" in self.l2.text():
                num2 = self.l1.text()
                self.l1.setText("")
                numfin = float(num1) / float(num2)
                self.l2.setText(str(int(numfin)))




 

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())