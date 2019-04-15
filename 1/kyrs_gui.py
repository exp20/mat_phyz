# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './kyrs_gui.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import math as m
import numpy as np
import matplotlib.pyplot as plt

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(640, 480)
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(10, 50, 621, 381))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.label_title = QtWidgets.QLabel(Dialog)
        self.label_title.setGeometry(QtCore.QRect(80, 10, 491, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_title.setFont(font)
        self.label_title.setObjectName("label_title")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(190, 90, 161, 17))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(380, 80, 131, 31))
        self.lineEdit.setText("20")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(380, 120, 131, 31))
        self.lineEdit_2.setText("0.59")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(70, 130, 281, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 180, 321, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(380, 170, 131, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setText("1.65")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(200, 220, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(380, 210, 131, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.setText("0")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(120, 260, 221, 17))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit_5 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_5.setGeometry(QtCore.QRect(380, 250, 131, 31))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_5.setText("0.002")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(120, 300, 221, 17))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lineEdit_6 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_6.setGeometry(QtCore.QRect(380, 290, 131, 31))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_6.setText("500")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(230, 340, 111, 17))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.lineEdit_7 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_7.setGeometry(QtCore.QRect(380, 340, 131, 31))
        self.lineEdit_7.setText("")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(520, 440, 99, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(380, 440, 99, 31))
        self.pushButton_2.setObjectName("pushButton_2")


        self.radioButton = QtWidgets.QRadioButton(Dialog)
        self.radioButton.setGeometry(QtCore.QRect(520, 290, 131, 31))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_2.setGeometry(QtCore.QRect(520, 341, 117, 31))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton.setChecked(True);
    

        self.pushButton_2.clicked.connect(self.buttonClicked_2)
        self.pushButton.clicked.connect(self.buttonClicked)


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Распределение температуры в цилиндре"))
        self.label_title.setText(_translate("Dialog", "Процесс теплопередачи в цилиндре "))
        self.label.setText(_translate("Dialog", "                        Радиус:"))
        self.label_2.setText(_translate("Dialog", "Коэффициент теплопроводности:"))
        self.label_3.setText(_translate("Dialog", "Коэффициент объёмной теплоёмкости:"))
        self.label_4.setText(_translate("Dialog", "Момент времени:"))
        self.label_5.setText(_translate("Dialog", "Коэффициент теплоотдачи:"))
        self.label_6.setText(_translate("Dialog", "Количество значений ряда:"))
        self.label_7.setText(_translate("Dialog", "Погрешность:"))
        self.pushButton.setText(_translate("Dialog", "Закрыть"))
        self.pushButton_2.setText(_translate("Dialog", "Рассчитать"))
        self.radioButton.setText(_translate("Dialog", "выбрать"))
        self.radioButton_2.setText(_translate("Dialog", "выбрать"))



    def buttonClicked_2(self):
        Error=False
        radio_b=0
        str0 = ""
        str1 = ""
        str2 = ""
        if(self.radioButton.isChecked()):
            radio_b=0
        if(self.radioButton_2.isChecked()):
            radio_b=1
        

        try:
            l = float(self.lineEdit.text())
            if l <= 0:
                str0 += "Радиус должен быть  > 0; \n"
        except:
            str0 += "Радиус введён неверно; \n"
        try:
            k = float(self.lineEdit_2.text())
            if k <= 0:
                str0 += "Коэффициент теплопроводности должен быть > 0; \n"
        except:
            str0 += "Коэффициент теплопроводности введён неверно; \n"
        try:
            c = float(self.lineEdit_3.text())
            if c <= 0:
                str0 += "Коэффициент объёмной теплоёмкости должен быть > 0; \n"
        except:
            str0+= "Коэффициент объёмной теплоёмкости введён неверно; \n"
        try:
            t = float(self.lineEdit_4.text())
            if t < 0:
                str0 += "Момент времени не может быть отрицательным; \n"
        except:
            str0 += "Момент времени введён неверно; \n"
        try:
            alp = float(self.lineEdit_5.text())
            if alp <= 0:
                str0 += "Коэффициент теплоотдачи должен быть > 0; \n"
        except:
            str0 += "Коэффициент теплоотдачи введён неверно; \n"


        
 

        if radio_b==0:
            try:
                n = int(self.lineEdit_6.text())
                if n < 0:
                    str1 += "Количество слагаемых ряда должно быть >= 0, целым числом; \n"
            except:
                str1 += "Количество слагаемых ряда неверно (не целое число); \n"
 
        
        if radio_b==1:
            try:
                eps = float(self.lineEdit_7.text())
                if eps < 0:
                    eps = abs(eps)
                elif eps == 0:
                    str2 += "Погрешность = 0 не следует задавать \n"
                
            except:
                str2 += "Погрешность введена неверно \n"

        if (len(str1) != 0 and len(str2) != 0):
            str0 += str1
            str0 += str2
            QMessageBox.about(temperature_distribution, "Ошибка", str0)
            Error = True
        elif not (((len(str1) != 0 and len(str2) == 0) or (len(str1) == 0 and len(str2) !=0)) or len(str0) == 0):
            str0 += str1
            str0 += str2
            QMessageBox.about(temperature_distribution, "Ошибка", str0)
            Error = True
        elif len(str0) != 0:
            QMessageBox.about(temperature_distribution, "Ошибка", str0)
            Error = True

         #meassuring
        if Error==True:
        	return
        else:
            R=float(self.lineEdit.text())
            c=float(self.lineEdit_3.text())
            k=float(self.lineEdit_2.text())
            t=float(self.lineEdit_4.text())
            print(m.pi)
            y=[]
            if t!=0:
            	self.redundancy_assessment(1,t,R,c,k)
        ## задано кол-во слагаемых 
            if radio_b==0:
            	N=int(self.lineEdit_6.text())
            	self.distribution_calculation(N,y,t,R,c,k)

        #epsilon
            else:
            	eps=float(self.lineEdit_7.text())
            	N=self.calculation_N_from_eps(R,c,k,t,eps)
            	self.distribution_calculation(N,y,t,R,c,k)
            	##оценка избыточности кол-ва слагаемых для удовлетвореня погрешности
            	#self.get_practic_N(N,y,t,R,c,k)
        
        #считаем ряд в точках
    def distribution_calculation(self,N,y,t,R,c,k):
        Riad_arr = []
        y=np.linspace(0, 2*m.pi*R, 2000)
        j=0
        while (j<len(y)):
        	Riad_arr.append(self.riad(N,y[j],t,R,c,k))
        	j+=1

        plt.plot(y,Riad_arr)
        plt.gcf().canvas.set_window_title('Распределение температуры в цилиндре') # меняем заголовок
        plt.ylabel('температура w(y,t)')
        plt.xlabel('y (y=ѲR)')
        plt.grid(True)
        plt.show()


	#получение оценки остатка ряда по кол-ву N
    def get_assessment_eps(self,R,c,k,t,N):
    	return(abs(  ((R**2)*c/(4*m.pi*((N+1)**2) * k * t) * m.exp(-1*((N**2)*k*t)/((R**2)*c)) ) ))
    

    def calculation_N_from_eps(self,R,c,k,t,eps):
    	i=1
    	while self.get_assessment_eps(R,c,k,t,i)>=eps:
    		i+=1
    	print("оценка остатка ряда погрешность достигается при N=",i)
    	return i


    def riad(self,N,y,t,R,c,k):
    	sum=0.5
    	i=1
    	while(i <= N):
    		sum+=(-1*(1/(m.pi*i))*(((-1)**i) - 1 ) * m.sin(i*y/R)*m.exp((-1*(i**2)*k*t)/((R**2)*c )) )
    		i+=1
    	return(sum)


    def redundancy_assessment(self,y,t,R,c,k):
        eps_arr=[0.1, 0.01,0.001,0.0001,0.00001,0.000001]
        t_arr=[0.001, 0.1, 20]
        N_t=[]
        N_norm=[]
        i=0
        j=0
        while (i < len(t_arr)):
            j=0
            while(j<len(eps_arr)):
                N_t.append(self.calculation_N_from_eps(R,c,k,t_arr[i],eps_arr[j]))
                N_norm.append(self.get_practic_N(N_t[j], eps_arr[j],y,t_arr[i],R,c,k))
                j+=1
            #print("При T=",t_arr[i], "\n", N_t,"\n", N_norm, "\n")
            i+=1
        print( N_t,"\n", N_norm, "\n")
			
        
    #высчитываем практическое значение слагаемых    
    def get_practic_N(self,N_t, eps,y,t,R,c,k):
                           N_n=N_t-1
                           while (abs(self.riad(N_t,y,t,R,c,k) - self.riad(N_n,y,t,R,c,k) )<eps):
                               N_t-=1
                           return (N_t+1)
		
           
    def buttonClicked(self):
        #print('Close button pressed')
        import sys
        sys.exit(0)



class info(object):
    def setupUi(self, info):
        _translate = QtCore.QCoreApplication.translate
        info.setWindowTitle(_translate("info", "Справка"))
        info.resize(600, 470)
        self.centralwidget = QtWidgets.QWidget(info)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(80, 30, 500, 520))
        self.listWidget.setObjectName("listWidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(200, 100, 320, 250))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setText(_translate("info", "Курсовая работа по дисциплине 'Уравнения математической физики'. Вариант № 15*. Данная программа строит график распределения температуры в  цилндре  в зависимости от координаты y=ѲR  в фиксированный момент времени. Ширина, момент времени и другие константы вводятся в поля программы. Программу разработал студент группы 6407 - Викторенков А.Е."))
        font=app.font()
        font.setPointSize(12)
        self.textBrowser.setFont(font)
        info.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(info)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        info.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(info)
        self.statusbar.setObjectName("statusbar")
        info.setStatusBar(self.statusbar)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    temperature_distribution= QtWidgets.QMainWindow()
    ui = Ui_Dialog()
    ui.setupUi(temperature_distribution)
    ui1 = info()
    info = QtWidgets.QMainWindow()
    ui1.setupUi(info)
    temperature_distribution.show()
    info.show()
    sys.exit(app.exec_())

