# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUIFINAL.ui'
#
# Created by: PyQt5 UI code generator 5.15.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

import Capstone2_part3 as CP3
import os


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(741, 556)
        MainWindow.setMinimumSize(QtCore.QSize(741, 556))
        MainWindow.setMaximumSize(QtCore.QSize(741, 556))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.CoinCalculatorbutton = QtWidgets.QPushButton(self.centralwidget)
        self.CoinCalculatorbutton.setGeometry(QtCore.QRect(20, 20, 121, 32))
        self.CoinCalculatorbutton.setObjectName("CoinCalculatorbutton")
        self.MultipleCoin_button = QtWidgets.QPushButton(self.centralwidget)
        self.MultipleCoin_button.setGeometry(QtCore.QRect(140, 20, 113, 32))
        self.MultipleCoin_button.setObjectName("MultipleCoin_button")
        self.Configurationsbutton = QtWidgets.QPushButton(self.centralwidget)
        self.Configurationsbutton.setGeometry(QtCore.QRect(250, 20, 113, 32))
        self.Configurationsbutton.setObjectName("Configurationsbutton")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(20, 50, 701, 481))
        self.stackedWidget.setStyleSheet("")
        self.stackedWidget.setObjectName("stackedWidget")
        self.CoinCalculatorPage = QtWidgets.QWidget()
        self.CoinCalculatorPage.setStyleSheet("background-color: lightblue")
        self.CoinCalculatorPage.setObjectName("CoinCalculatorPage")
        self.coinsorttitlelabel = QtWidgets.QLabel(self.CoinCalculatorPage)
        self.coinsorttitlelabel.setGeometry(QtCore.QRect(200, 40, 300, 100))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.coinsorttitlelabel.setFont(font)
        self.coinsorttitlelabel.setObjectName("coinsorttitlelabel")
        self.coinsortamountlabel = QtWidgets.QLabel(self.CoinCalculatorPage)
        self.coinsortamountlabel.setGeometry(QtCore.QRect(120, 160, 120, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.coinsortamountlabel.setFont(font)
        self.coinsortamountlabel.setObjectName("coinsortamountlabel")
        self.csradiobuttontwopound = QtWidgets.QRadioButton(self.CoinCalculatorPage)
        self.csradiobuttontwopound.setGeometry(QtCore.QRect(310, 220, 100, 20))
        self.csradiobuttontwopound.setObjectName("csradiobuttontwopound")
        self.csradiobuttononepound = QtWidgets.QRadioButton(self.CoinCalculatorPage)
        self.csradiobuttononepound.setGeometry(QtCore.QRect(310, 250, 100, 20))
        self.csradiobuttononepound.setObjectName("csradiobuttononepound")
        self.Coinsorttextbox = QtWidgets.QLineEdit(self.CoinCalculatorPage)
        self.Coinsorttextbox.setGeometry(QtCore.QRect(320, 160, 113, 21))
        self.Coinsorttextbox.setObjectName("Coinsorttextbox")
        self.csradiobutton50p = QtWidgets.QRadioButton(self.CoinCalculatorPage)
        self.csradiobutton50p.setGeometry(QtCore.QRect(370, 220, 100, 20))
        self.csradiobutton50p.setObjectName("csradiobutton50p")
        self.csradiobutton20p = QtWidgets.QRadioButton(self.CoinCalculatorPage)
        self.csradiobutton20p.setGeometry(QtCore.QRect(370, 250, 100, 20))
        self.csradiobutton20p.setObjectName("csradiobutton20p")
        self.csradiobutton10p = QtWidgets.QRadioButton(self.CoinCalculatorPage)
        self.csradiobutton10p.setGeometry(QtCore.QRect(440, 220, 100, 20))
        self.csradiobutton10p.setObjectName("csradiobutton10p")
        self.coinsortdenomlabel = QtWidgets.QLabel(self.CoinCalculatorPage)
        self.coinsortdenomlabel.setGeometry(QtCore.QRect(40, 200, 220, 101))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.coinsortdenomlabel.setFont(font)
        self.coinsortdenomlabel.setObjectName("coinsortdenomlabel")
        self.coinsortresultsbutton = QtWidgets.QPushButton(self.CoinCalculatorPage)
        self.coinsortresultsbutton.setGeometry(QtCore.QRect(100, 350, 113, 32))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.coinsortresultsbutton.setFont(font)
        self.coinsortresultsbutton.setObjectName("coinsortresultsbutton")
        self.coinsortresultslabel = QtWidgets.QLabel(self.CoinCalculatorPage)
        self.coinsortresultslabel.setGeometry(QtCore.QRect(320, 320, 361, 81))
        self.coinsortresultslabel.setObjectName("coinsortresultslabel")
        self.stackedWidget.addWidget(self.CoinCalculatorPage)
        self.MultipleCoinPage = QtWidgets.QWidget()
        self.MultipleCoinPage.setStyleSheet("background-color: lightyellow")
        self.MultipleCoinPage.setObjectName("MultipleCoinPage")
        self.Multiplecointitlelabel = QtWidgets.QLabel(self.MultipleCoinPage)
        self.Multiplecointitlelabel.setGeometry(QtCore.QRect(100, 40, 550, 100))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.Multiplecointitlelabel.setFont(font)
        self.Multiplecointitlelabel.setObjectName("Multiplecointitlelabel")
        self.multiplesortresultsbutton = QtWidgets.QPushButton(self.MultipleCoinPage)
        self.multiplesortresultsbutton.setGeometry(QtCore.QRect(90, 370, 211, 32))
        self.multiplesortresultsbutton.setObjectName("multiplesortresultsbutton")
        self.Multiplecoinamountlabel = QtWidgets.QLabel(self.MultipleCoinPage)
        self.Multiplecoinamountlabel.setGeometry(QtCore.QRect(150, 160, 120, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Multiplecoinamountlabel.setFont(font)
        self.Multiplecoinamountlabel.setObjectName("Multiplecoinamountlabel")
        self.MultipleAmountsTextbox = QtWidgets.QLineEdit(self.MultipleCoinPage)
        self.MultipleAmountsTextbox.setGeometry(QtCore.QRect(360, 150, 113, 21))
        self.MultipleAmountsTextbox.setObjectName("MultipleAmountsTextbox")
        self.Multiplecoinsortresultslabel = QtWidgets.QLabel(self.MultipleCoinPage)
        self.Multiplecoinsortresultslabel.setGeometry(QtCore.QRect(370, 360, 341, 61))
        self.Multiplecoinsortresultslabel.setObjectName("Multiplecoinsortresultslabel")
        self.MultipleCoinDenomexcludelabel = QtWidgets.QLabel(self.MultipleCoinPage)
        self.MultipleCoinDenomexcludelabel.setGeometry(QtCore.QRect(90, 200, 221, 111))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.MultipleCoinDenomexcludelabel.setFont(font)
        self.MultipleCoinDenomexcludelabel.setObjectName("MultipleCoinDenomexcludelabel")
        self.multiplecoinradio2pound = QtWidgets.QRadioButton(self.MultipleCoinPage)
        self.multiplecoinradio2pound.setGeometry(QtCore.QRect(370, 190, 100, 20))
        self.multiplecoinradio2pound.setObjectName("multiplecoinradio2pound")
        self.multiplecoinradio1pound = QtWidgets.QRadioButton(self.MultipleCoinPage)
        self.multiplecoinradio1pound.setGeometry(QtCore.QRect(370, 220, 100, 20))
        self.multiplecoinradio1pound.setObjectName("multiplecoinradio1pound")
        self.multiplecoinradio50p = QtWidgets.QRadioButton(self.MultipleCoinPage)
        self.multiplecoinradio50p.setGeometry(QtCore.QRect(370, 250, 100, 20))
        self.multiplecoinradio50p.setObjectName("multiplecoinradio50p")
        self.multiplecoinradio20p = QtWidgets.QRadioButton(self.MultipleCoinPage)
        self.multiplecoinradio20p.setGeometry(QtCore.QRect(370, 280, 100, 20))
        self.multiplecoinradio20p.setObjectName("multiplecoinradio20p")
        self.multiplecoinradio10p = QtWidgets.QRadioButton(self.MultipleCoinPage)
        self.multiplecoinradio10p.setGeometry(QtCore.QRect(370, 310, 100, 20))
        self.multiplecoinradio10p.setObjectName("multiplecoinradio10p")
        self.stackedWidget.addWidget(self.MultipleCoinPage)
        self.Configurations = QtWidgets.QWidget()
        self.Configurations.setStyleSheet("background-color: lightcoral")
        self.Configurations.setObjectName("Configurations")
        self.Configtitlelabel = QtWidgets.QLabel(self.Configurations)
        self.Configtitlelabel.setGeometry(QtCore.QRect(150, 30, 500, 71))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.Configtitlelabel.setFont(font)
        self.Configtitlelabel.setObjectName("Configtitlelabel")
        self.configconfirmbutton = QtWidgets.QPushButton(self.Configurations)
        self.configconfirmbutton.setGeometry(QtCore.QRect(40, 300, 181, 31))
        self.configconfirmbutton.setObjectName("configconfirmbutton")
        self.configcurrentcurrencylabel = QtWidgets.QLabel(self.Configurations)
        self.configcurrentcurrencylabel.setGeometry(QtCore.QRect(60, 230, 151, 41))
        self.configcurrentcurrencylabel.setObjectName("configcurrentcurrencylabel")
        self.configminamountlabel = QtWidgets.QLabel(self.Configurations)
        self.configminamountlabel.setGeometry(QtCore.QRect(59, 120, 131, 20))
        self.configminamountlabel.setObjectName("configminamountlabel")
        self.configmaxamountlabel = QtWidgets.QLabel(self.Configurations)
        self.configmaxamountlabel.setGeometry(QtCore.QRect(60, 180, 141, 16))
        self.configmaxamountlabel.setObjectName("configmaxamountlabel")
        self.configmintextbox = QtWidgets.QLineEdit(self.Configurations)
        self.configmintextbox.setGeometry(QtCore.QRect(300, 120, 113, 21))
        self.configmintextbox.setAutoFillBackground(False)
        self.configmintextbox.setStyleSheet("")
        self.configmintextbox.setObjectName("configmintextbox")
        self.configmaxtextbox = QtWidgets.QLineEdit(self.Configurations)
        self.configmaxtextbox.setGeometry(QtCore.QRect(300, 180, 113, 21))
        self.configmaxtextbox.setObjectName("configmaxtextbox")
        self.configcurrencybuttGBP = QtWidgets.QRadioButton(self.Configurations)
        self.configcurrencybuttGBP.setGeometry(QtCore.QRect(280, 230, 100, 20))
        self.configcurrencybuttGBP.setObjectName("configcurrencybuttGBP")
        self.configcurrencybuttMGA = QtWidgets.QRadioButton(self.Configurations)
        self.configcurrencybuttMGA.setGeometry(QtCore.QRect(380, 230, 100, 20))
        self.configcurrencybuttMGA.setObjectName("configcurrencybuttMGA")
        self.configcurrencybuttUSD = QtWidgets.QRadioButton(self.Configurations)
        self.configcurrencybuttUSD.setGeometry(QtCore.QRect(460, 230, 100, 20))
        self.configcurrencybuttUSD.setObjectName("configcurrencybuttUSD")
        self.printcoinlistbutton = QtWidgets.QPushButton(self.Configurations)
        self.printcoinlistbutton.setGeometry(QtCore.QRect(40, 340, 181, 31))
        self.printcoinlistbutton.setObjectName("printcoinlistbutton")
        self.printcoinlistbutton_2 = QtWidgets.QPushButton(self.Configurations)
        self.printcoinlistbutton_2.setGeometry(QtCore.QRect(40, 380, 181, 32))
        self.printcoinlistbutton_2.setObjectName("printcoinlistbutton_2")
        self.configresultslabel = QtWidgets.QLabel(self.Configurations)
        self.configresultslabel.setGeometry(QtCore.QRect(290, 290, 391, 131))
        self.configresultslabel.setObjectName("configresultslabel")
        self.stackedWidget.addWidget(self.Configurations)
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionMenu2 = QtWidgets.QAction(MainWindow)
        self.actionMenu2.setObjectName("actionMenu2")

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    #Functions for changing the stacked widget pages.
    def GoToCoinCalcPage(self):
        self.stackedWidget.setCurrentIndex(0)

    def GoToCoinMultCalcPage(self):
        self.stackedWidget.setCurrentIndex(1)
    
    def GoToCoinConfigPage(self):
        self.stackedWidget.setCurrentIndex(2)

    #Functions for doing the calculations and printing the results

    def CSClicked(self):
        RadioFailBoo = False
        try:
            amount = int(self.Coinsorttextbox.text())
            if amount > CP3.Configurations["Minimum Value"] and amount < CP3.Configurations["Maximum Value"]:

                if self.csradiobuttontwopound.isChecked():
                    denom = 0
                elif self.csradiobuttononepound.isChecked():
                    denom = 1
                elif self.csradiobutton50p.isChecked():
                    denom = 2
                elif self.csradiobutton20p.isChecked():
                    denom = 3
                elif self.csradiobutton10p.isChecked():
                    denom = 4
                else:
                    RadioFailBoo = True
                
                if not RadioFailBoo:
                    result = CP3.UserFriendlyPrintCoinSort(CP3.CoinSort((amount, denom)))
                else:
                    result = "Please select a denomination"

            else:
                result = "Please enter a value between " + str(CP3.Configurations["Minimum Value"]) + " and " + str(CP3.Configurations["Maximum Value"])

            self.coinsortresultslabel.setText(result)
        
        except ValueError:
            self.coinsortresultslabel.setText("Integers only!")

    def MCSClicked(self):
        RadioFailBoo = False
        try:
            
            amount = int(self.MultipleAmountsTextbox.text())

            if amount > CP3.Configurations["Minimum Value"] and amount < CP3.Configurations["Maximum Value"]:

                if self.multiplecoinradio2pound.isChecked():
                    denom = 0
                elif self.multiplecoinradio1pound.isChecked():
                    denom = 1
                elif self.multiplecoinradio50p.isChecked():
                    denom = 2
                elif self.multiplecoinradio20p.isChecked():
                    denom = 3
                elif self.multiplecoinradio10p.isChecked():
                    denom = 4
                else:
                    RadioFailBoo = True
                
                if not RadioFailBoo:
                    result = CP3.UserFriendlyPrintMultipleCoin(CP3.MultipleCoinSort((amount, denom)))
                else:
                    result = "Please select a denomination"

                
            else:
                result = "Please enter a value between " + str(CP3.Configurations["Minimum Value"]) + " and " + str(CP3.Configurations["Maximum Value"])   
            
            self.Multiplecoinsortresultslabel.setText(result)

        except ValueError:
            self.Multiplecoinsortresultslabel.setText("Integers only!")

    def UpdateConfigurationClicked(self):
        try:
            errormessage = "Configurations Updated!"
            RadioFailBoo = False
            newmin = int(self.configmintextbox.text())
            newmax = int(self.configmaxtextbox.text())

            if not (newmin > newmax or newmin < 0):
                if self.configcurrencybuttGBP.isChecked():
                    currency = "GBP (£)"
                elif self.configcurrencybuttMGA.isChecked():
                    currency = "MGA (Ar)"
                elif self.configcurrencybuttUSD.isChecked():
                    currency = "USD ($)"
                else:
                    RadioFailBoo = True
                    errormessage = "Please select a currency"
            else: 
                errormessage = "Please give us a reasonable minimum and maximum"
                RadioFailBoo = True

            if not RadioFailBoo:
                CP3.UpdateConfiguration(newmin, newmax, currency)

            
        except ValueError:
            errormessage = "Integers only!"
        
        self.configresultslabel.setText(errormessage)

    def PrintConfigurations(self):
        self.configresultslabel.setText(CP3.PrintConfigurations())

    def PrintCoinListClicked(self):
        self.configresultslabel.setText(CP3.PrintCoinList())



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Capstone Coin Sorter"))
        #This gets the absolute path of the icon file

        scriptDir = os.path.dirname(os.path.realpath("WinIcon.jpg"))
        MainWindow.setWindowIcon(QtGui.QIcon(scriptDir + os.path.sep + "WinIcon.jpg"))
        self.CoinCalculatorbutton.setText(_translate("MainWindow", "Coin Calculator"))
        self.MultipleCoin_button.setText(_translate("MainWindow", "Multiple Coin"))
        self.Configurationsbutton.setText(_translate("MainWindow", "Configurations"))
        self.coinsorttitlelabel.setText(_translate("MainWindow", "COIN SORTER"))
        self.coinsortamountlabel.setText(_translate("MainWindow", "AMOUNT"))
        self.csradiobuttontwopound.setText(_translate("MainWindow", "£2"))
        self.csradiobuttononepound.setText(_translate("MainWindow", "£1"))
        self.csradiobutton50p.setText(_translate("MainWindow", "50p"))
        self.csradiobutton20p.setText(_translate("MainWindow", "20p"))
        self.csradiobutton10p.setText(_translate("MainWindow", "10p"))
        self.coinsortdenomlabel.setText(_translate("MainWindow", "DENOMINATIONS"))
        self.coinsortresultsbutton.setText(_translate("MainWindow", "SORT"))
        self.coinsortresultslabel.setText(_translate("MainWindow", ""))
        self.Multiplecointitlelabel.setText(_translate("MainWindow", "MULTIPLE COIN SORTER"))
        self.multiplesortresultsbutton.setText(_translate("MainWindow", "MULTIPLE SORT"))
        self.Multiplecoinamountlabel.setText(_translate("MainWindow", "AMOUNT"))
        self.Multiplecoinsortresultslabel.setText(_translate("MainWindow", ""))
        self.MultipleCoinDenomexcludelabel.setText(_translate("MainWindow", "DENOMINATION\n   TO EXCLUDE"))
        self.multiplecoinradio2pound.setText(_translate("MainWindow", "£2"))
        self.multiplecoinradio1pound.setText(_translate("MainWindow", "£1"))
        self.multiplecoinradio50p.setText(_translate("MainWindow", "50p"))
        self.multiplecoinradio20p.setText(_translate("MainWindow", "20p"))
        self.multiplecoinradio10p.setText(_translate("MainWindow", "10p"))
        self.Configtitlelabel.setText(_translate("MainWindow", "CONFIGUARATIONS"))
        self.configconfirmbutton.setText(_translate("MainWindow", "CONFIRM"))
        self.configcurrentcurrencylabel.setText(_translate("MainWindow", "CURRENT CURRENCY"))
        self.configminamountlabel.setText(_translate("MainWindow", "MINIMUM AMOUNT"))
        self.configmaxamountlabel.setText(_translate("MainWindow", "MAXIMUM AMOUNT"))
        self.configcurrencybuttGBP.setText(_translate("MainWindow", "GBP"))
        self.configcurrencybuttMGA.setText(_translate("MainWindow", "MGA"))
        self.configcurrencybuttUSD.setText(_translate("MainWindow", "USD"))
        self.printcoinlistbutton.setText(_translate("MainWindow", "PRINT COIN LIST "))
        self.printcoinlistbutton_2.setText(_translate("MainWindow", "PRINT CONFIGURATIONS"))
        self.configresultslabel.setText(_translate("MainWindow", "CONFIGURATION RESULTS"))
        self.actionMenu2.setText(_translate("MainWindow", "Menu2"))

        #event listeners for menu buttons
        self.CoinCalculatorbutton.clicked.connect(self.GoToCoinCalcPage)
        self.MultipleCoin_button.clicked.connect(self.GoToCoinMultCalcPage)
        self.Configurationsbutton.clicked.connect(self.GoToCoinConfigPage)

        #listeners for calculation buttons
        self.coinsortresultsbutton.clicked.connect(self.CSClicked)
        self.multiplesortresultsbutton.clicked.connect(self.MCSClicked)

        self.configconfirmbutton.clicked.connect(self.UpdateConfigurationClicked)
        self.printcoinlistbutton.clicked.connect(self.PrintCoinListClicked)
        self.printcoinlistbutton_2.clicked.connect(self.PrintConfigurations)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
