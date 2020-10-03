# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow2.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(781, 533)
        mainWindow.setMinimumSize(QtCore.QSize(160, 50))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        mainWindow.setFont(font)
        self.gridLayout_2 = QtWidgets.QGridLayout(mainWindow)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.verticalWidget = QtWidgets.QWidget(mainWindow)
        self.verticalWidget.setStyleSheet("background-color: rgb(180, 180, 180);")
        self.verticalWidget.setObjectName("verticalWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lb_side_up = QtWidgets.QLabel(self.verticalWidget)
        self.lb_side_up.setText("")
        self.lb_side_up.setObjectName("lb_side_up")
        self.verticalLayout_2.addWidget(self.lb_side_up)
        self.btn_park = QtWidgets.QPushButton(self.verticalWidget)
        self.btn_park.setMinimumSize(QtCore.QSize(160, 50))
        self.btn_park.setStyleSheet("background-color: rgb(254, 254, 254);\n"
"border-color: rgb(254, 254, 254);\n"
"gridline-color: rgb(254, 254, 254);\n"
"selection-background-color: rgb(254, 254, 254);\n"
"alternate-background-color: rgb(255, 255, 255);")
        self.btn_park.setAutoDefault(False)
        self.btn_park.setDefault(False)
        self.btn_park.setFlat(False)
        self.btn_park.setObjectName("btn_park")
        self.verticalLayout_2.addWidget(self.btn_park)
        self.btn_mycar = QtWidgets.QPushButton(self.verticalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_mycar.sizePolicy().hasHeightForWidth())
        self.btn_mycar.setSizePolicy(sizePolicy)
        self.btn_mycar.setMinimumSize(QtCore.QSize(160, 50))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        self.btn_mycar.setFont(font)
        self.btn_mycar.setAutoFillBackground(False)
        self.btn_mycar.setStyleSheet("background-color: rgb(254, 254, 254);\n"
"border-color: rgb(254, 254, 254);\n"
"gridline-color: rgb(254, 254, 254);\n"
"selection-background-color: rgb(254, 254, 254);\n"
"alternate-background-color: rgb(255, 255, 255);")
        self.btn_mycar.setAutoRepeatInterval(100)
        self.btn_mycar.setObjectName("btn_mycar")
        self.verticalLayout_2.addWidget(self.btn_mycar)
        self.btn_carout = QtWidgets.QPushButton(self.verticalWidget)
        self.btn_carout.setMinimumSize(QtCore.QSize(160, 50))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        self.btn_carout.setFont(font)
        self.btn_carout.setStyleSheet("background-color: rgb(254, 254, 254);\n"
"border-color: rgb(254, 254, 254);\n"
"gridline-color: rgb(254, 254, 254);\n"
"selection-background-color: rgb(254, 254, 254);\n"
"alternate-background-color: rgb(255, 255, 255);")
        self.btn_carout.setObjectName("btn_carout")
        self.verticalLayout_2.addWidget(self.btn_carout)
        self.lb_side_down = QtWidgets.QLabel(self.verticalWidget)
        self.lb_side_down.setText("")
        self.lb_side_down.setObjectName("lb_side_down")
        self.verticalLayout_2.addWidget(self.lb_side_down)
        self.gridLayout.addWidget(self.verticalWidget, 1, 0, 1, 1)
        self.stkwdg = QtWidgets.QStackedWidget(mainWindow)
        self.stkwdg.setObjectName("stkwdg")
        self.pg_main = QtWidgets.QWidget()
        self.pg_main.setObjectName("pg_main")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.pg_main)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.lb_2_1 = QtWidgets.QLabel(self.pg_main)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lb_2_1.setFont(font)
        self.lb_2_1.setStyleSheet("background-color: rgb(222, 222, 222);")
        self.lb_2_1.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_2_1.setObjectName("lb_2_1")
        self.gridLayout_4.addWidget(self.lb_2_1, 5, 1, 1, 1)
        self.lb_1_park = QtWidgets.QLabel(self.pg_main)
        self.lb_1_park.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lb_1_park.setFont(font)
        self.lb_1_park.setStyleSheet("background-color: rgb(222, 222, 222);")
        self.lb_1_park.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_1_park.setObjectName("lb_1_park")
        self.gridLayout_4.addWidget(self.lb_1_park, 0, 1, 1, 3)
        self.lb_2_park = QtWidgets.QLabel(self.pg_main)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lb_2_park.setFont(font)
        self.lb_2_park.setStyleSheet("background-color: rgb(222, 222, 222);")
        self.lb_2_park.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_2_park.setObjectName("lb_2_park")
        self.gridLayout_4.addWidget(self.lb_2_park, 4, 1, 1, 3)
        self.lb_1_3 = QtWidgets.QLabel(self.pg_main)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lb_1_3.setFont(font)
        self.lb_1_3.setStyleSheet("background-color: rgb(222, 222, 222);")
        self.lb_1_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_1_3.setObjectName("lb_1_3")
        self.gridLayout_4.addWidget(self.lb_1_3, 1, 3, 1, 1)
        self.lb_1_1 = QtWidgets.QLabel(self.pg_main)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lb_1_1.setFont(font)
        self.lb_1_1.setStyleSheet("background-color: rgb(222, 222, 222);")
        self.lb_1_1.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_1_1.setObjectName("lb_1_1")
        self.gridLayout_4.addWidget(self.lb_1_1, 1, 1, 1, 1)
        self.lb_1_2 = QtWidgets.QLabel(self.pg_main)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lb_1_2.setFont(font)
        self.lb_1_2.setStyleSheet("background-color: rgb(222, 222, 222);")
        self.lb_1_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_1_2.setObjectName("lb_1_2")
        self.gridLayout_4.addWidget(self.lb_1_2, 1, 2, 1, 1)
        self.lb_2_2 = QtWidgets.QLabel(self.pg_main)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lb_2_2.setFont(font)
        self.lb_2_2.setStyleSheet("background-color: rgb(222, 222, 222);")
        self.lb_2_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_2_2.setObjectName("lb_2_2")
        self.gridLayout_4.addWidget(self.lb_2_2, 5, 2, 1, 1)
        self.lb_2_3 = QtWidgets.QLabel(self.pg_main)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lb_2_3.setFont(font)
        self.lb_2_3.setStyleSheet("background-color: rgb(222, 222, 222);")
        self.lb_2_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_2_3.setObjectName("lb_2_3")
        self.gridLayout_4.addWidget(self.lb_2_3, 5, 3, 1, 1)
        self.stkwdg.addWidget(self.pg_main)
        self.pg_search = QtWidgets.QWidget()
        self.pg_search.setObjectName("pg_search")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.pg_search)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.ledt_search = QtWidgets.QLineEdit(self.pg_search)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.ledt_search.setFont(font)
        self.ledt_search.setText("")
        self.ledt_search.setObjectName("ledt_search")
        self.gridLayout_3.addWidget(self.ledt_search, 3, 1, 1, 1)
        self.lb_pg_search = QtWidgets.QLabel(self.pg_search)
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(20)
        self.lb_pg_search.setFont(font)
        self.lb_pg_search.setStyleSheet("border: 2px solid rgb(150, 150, 150);")
        self.lb_pg_search.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_pg_search.setObjectName("lb_pg_search")
        self.gridLayout_3.addWidget(self.lb_pg_search, 1, 0, 1, 2)
        self.lb_num_search = QtWidgets.QLabel(self.pg_search)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lb_num_search.setFont(font)
        self.lb_num_search.setObjectName("lb_num_search")
        self.gridLayout_3.addWidget(self.lb_num_search, 3, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.pg_search)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 2, 0, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.pg_search)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 2)
        self.btn_search = QtWidgets.QPushButton(self.pg_search)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_search.setFont(font)
        self.btn_search.setObjectName("btn_search")
        self.gridLayout_3.addWidget(self.btn_search, 4, 1, 1, 1)
        self.stkwdg.addWidget(self.pg_search)
        self.pg_out = QtWidgets.QWidget()
        self.pg_out.setObjectName("pg_out")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.pg_out)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.lb_camera = QtWidgets.QLabel(self.pg_out)
        self.lb_camera.setMinimumSize(QtCore.QSize(448, 211))
        self.lb_camera.setStyleSheet("border: 2px solid rgb(150, 150, 150);")
        self.lb_camera.setText("")
        self.lb_camera.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lb_camera.setObjectName("lb_camera")
        self.gridLayout_5.addWidget(self.lb_camera, 2, 0, 1, 4)
        self.lb_pg_out = QtWidgets.QLabel(self.pg_out)
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(20)
        self.lb_pg_out.setFont(font)
        self.lb_pg_out.setStyleSheet("border: 2px solid rgb(150, 150, 150);")
        self.lb_pg_out.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_pg_out.setObjectName("lb_pg_out")
        self.gridLayout_5.addWidget(self.lb_pg_out, 1, 0, 1, 4)
        self.lb_num_code = QtWidgets.QLabel(self.pg_out)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lb_num_code.setFont(font)
        self.lb_num_code.setObjectName("lb_num_code")
        self.gridLayout_5.addWidget(self.lb_num_code, 8, 2, 1, 1)
        self.lb_num_phone = QtWidgets.QLabel(self.pg_out)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lb_num_phone.setFont(font)
        self.lb_num_phone.setObjectName("lb_num_phone")
        self.gridLayout_5.addWidget(self.lb_num_phone, 7, 2, 1, 1)
        self.lb_num_out = QtWidgets.QLabel(self.pg_out)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lb_num_out.setFont(font)
        self.lb_num_out.setObjectName("lb_num_out")
        self.gridLayout_5.addWidget(self.lb_num_out, 6, 2, 1, 1)
        self.ledt_phone = QtWidgets.QLineEdit(self.pg_out)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.ledt_phone.setFont(font)
        self.ledt_phone.setObjectName("ledt_phone")
        self.gridLayout_5.addWidget(self.ledt_phone, 7, 3, 1, 1)
        self.ledt_car = QtWidgets.QLineEdit(self.pg_out)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.ledt_car.setFont(font)
        self.ledt_car.setText("")
        self.ledt_car.setObjectName("ledt_car")
        self.gridLayout_5.addWidget(self.ledt_car, 6, 3, 1, 1)
        self.ledt_name = QtWidgets.QLineEdit(self.pg_out)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.ledt_name.setFont(font)
        self.ledt_name.setObjectName("ledt_name")
        self.gridLayout_5.addWidget(self.ledt_name, 8, 3, 1, 1)
        self.btn_out = QtWidgets.QPushButton(self.pg_out)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_out.setFont(font)
        self.btn_out.setObjectName("btn_out")
        self.gridLayout_5.addWidget(self.btn_out, 6, 1, 3, 1)
        self.stkwdg.addWidget(self.pg_out)
        self.gridLayout.addWidget(self.stkwdg, 1, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(mainWindow)
        self.stkwdg.setCurrentIndex(0)
        self.btn_park.clicked.connect(mainWindow.changeLayout1)
        self.btn_mycar.clicked.connect(mainWindow.changeLayout2)
        self.btn_carout.clicked.connect(mainWindow.changeLayout3)
        self.btn_out.clicked.connect(mainWindow.findcle)
        self.btn_search.clicked.connect(mainWindow.searchcle)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "주차장 터치 패널"))
        self.btn_park.setText(_translate("mainWindow", "주차장"))
        self.btn_mycar.setText(_translate("mainWindow", "내차 검색"))
        self.btn_carout.setText(_translate("mainWindow", "자동차 빼기"))
        self.lb_2_1.setText(_translate("mainWindow", "2-1"))
        self.lb_1_park.setText(_translate("mainWindow", "1번 라인"))
        self.lb_2_park.setText(_translate("mainWindow", "2번 라인"))
        self.lb_1_3.setText(_translate("mainWindow", "1-3"))
        self.lb_1_1.setText(_translate("mainWindow", "1-1"))
        self.lb_1_2.setText(_translate("mainWindow", "1-2"))
        self.lb_2_2.setText(_translate("mainWindow", "2-2"))
        self.lb_2_3.setText(_translate("mainWindow", "2-3"))
        self.lb_pg_search.setText(_translate("mainWindow", "내차 검색"))
        self.lb_num_search.setText(_translate("mainWindow", "자동차 번호 : "))
        self.btn_search.setText(_translate("mainWindow", "검색"))
        self.lb_pg_out.setText(_translate("mainWindow", "내차 빼기"))
        self.lb_num_code.setText(_translate("mainWindow", "이름"))
        self.lb_num_phone.setText(_translate("mainWindow", "휴대폰 번호"))
        self.lb_num_out.setText(_translate("mainWindow", "자동차 번호 : "))
        self.btn_out.setText(_translate("mainWindow", "검색"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QWidget()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())