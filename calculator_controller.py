from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import MainWindow
from calculator_model import Calculator

class Controller(QtWidgets.QWidget,MainWindow.Ui_MainWindow):
    def __init__(win,self,*args, **kwargs):
        self.pushButton_eq.clicked.connect(lambda i: Calculator.doMath(i,self))
        self.pushButton_1.clicked.connect(lambda i :Calculator.buttons(i,self,self.pushButton_1))
        self.pushButton_2.clicked.connect(lambda i :Calculator.buttons(i,self,self.pushButton_2))
        self.pushButton_3.clicked.connect(lambda i :Calculator.buttons(i,self,self.pushButton_3))
        self.pushButton_4.clicked.connect(lambda i :Calculator.buttons(i,self,self.pushButton_4))
        self.pushButton_5.clicked.connect(lambda i :Calculator.buttons(i,self,self.pushButton_5))
        self.pushButton_6.clicked.connect(lambda i :Calculator.buttons(i,self,self.pushButton_6))
        self.pushButton_7.clicked.connect(lambda i :Calculator.buttons(i,self,self.pushButton_7))
        self.pushButton_8.clicked.connect(lambda i :Calculator.buttons(i,self,self.pushButton_8))
        self.pushButton_9.clicked.connect(lambda i :Calculator.buttons(i,self,self.pushButton_9))
        self.pushButton_0.clicked.connect(lambda i :Calculator.buttons(i,self,self.pushButton_0))
        self.pushButton_point.clicked.connect(lambda i :Calculator.buttons(i,self,self.pushButton_point))
        self.pushButton_add.clicked.connect(lambda i :Calculator.buttons(i,self,self.pushButton_add))
        self.pushButton_sub.clicked.connect(lambda i :Calculator.buttons(i,self,self.pushButton_sub))
        self.pushButton_mul.clicked.connect(lambda i :Calculator.buttons(i,self,self.pushButton_mul))
        self.pushButton_div.clicked.connect(lambda i :Calculator.buttons(i,self,self.pushButton_div))
        #self.pushButton_eq.clicked.connect(lambda i :Calculator.buttons(i,self,self.pushButton_eq))
        self.pushButton_17.clicked.connect(lambda i :Calculator.buttons(i,self,self.pushButton_17))

    
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    
    ex = MainWindow.Ui_MainWindow()
    
    w = QtWidgets.QMainWindow()
    
    ex.setupUi(w)

   

    #Calculator(ex)
    Controller(ex)
    
    w.show()
    
    sys.exit(app.exec_())

