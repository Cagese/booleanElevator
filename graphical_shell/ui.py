# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Boolean_Elevator(object):
    def setupUi(self, Boolean_Elevator):
        Boolean_Elevator.setObjectName("Boolean_Elevator")
        Boolean_Elevator.resize(1148, 780)
        Boolean_Elevator.setMinimumSize(QtCore.QSize(1148, 780))
        Boolean_Elevator.setMaximumSize(QtCore.QSize(1148, 780))
        self.centralwidget = QtWidgets.QWidget(Boolean_Elevator)
        self.centralwidget.setObjectName("centralwidget")
        self.levels_widget = QtWidgets.QTextBrowser(self.centralwidget)
        self.levels_widget.setEnabled(False)
        self.levels_widget.setGeometry(QtCore.QRect(30, 30, 71, 661))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.levels_widget.setFont(font)
        self.levels_widget.setMouseTracking(True)
        self.levels_widget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.levels_widget.setAutoFillBackground(False)
        self.levels_widget.setObjectName("levels_widget")
        self.controlButton = QtWidgets.QPushButton(self.centralwidget)
        self.controlButton.setGeometry(QtCore.QRect(70, 710, 151, 23))
        self.controlButton.setObjectName("controlButton")
        self.elevators_widget = QtWidgets.QTextBrowser(self.centralwidget)
        self.elevators_widget.setEnabled(False)
        self.elevators_widget.setGeometry(QtCore.QRect(100, 30, 161, 661))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.elevators_widget.setFont(font)
        self.elevators_widget.setMouseTracking(True)
        self.elevators_widget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.elevators_widget.setAutoFillBackground(False)
        self.elevators_widget.setObjectName("elevators_widget")
        self.peoples_widgets = QtWidgets.QTextBrowser(self.centralwidget)
        self.peoples_widgets.setEnabled(False)
        self.peoples_widgets.setGeometry(QtCore.QRect(260, 30, 441, 661))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.peoples_widgets.setFont(font)
        self.peoples_widgets.setMouseTracking(True)
        self.peoples_widgets.setFocusPolicy(QtCore.Qt.NoFocus)
        self.peoples_widgets.setAutoFillBackground(False)
        self.peoples_widgets.setObjectName("peoples_widgets")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(710, 30, 401, 661))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_14 = QtWidgets.QLabel(self.layoutWidget)
        self.label_14.setMaximumSize(QtCore.QSize(16777215, 13))
        self.label_14.setObjectName("label_14")
        self.verticalLayout_3.addWidget(self.label_14)
        self.searching = QtWidgets.QLabel(self.layoutWidget)
        self.searching.setMaximumSize(QtCore.QSize(16777215, 13))
        self.searching.setObjectName("searching")
        self.verticalLayout_3.addWidget(self.searching)
        self.departure = QtWidgets.QLabel(self.layoutWidget)
        self.departure.setMaximumSize(QtCore.QSize(16777215, 13))
        self.departure.setObjectName("departure")
        self.verticalLayout_3.addWidget(self.departure)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_3.addWidget(self.label_9)
        self.horizontalLayout_5.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lift1name = QtWidgets.QLabel(self.layoutWidget)
        self.lift1name.setObjectName("lift1name")
        self.horizontalLayout_4.addWidget(self.lift1name)
        self.lift2name = QtWidgets.QLabel(self.layoutWidget)
        self.lift2name.setObjectName("lift2name")
        self.horizontalLayout_4.addWidget(self.lift2name)
        self.lift3name = QtWidgets.QLabel(self.layoutWidget)
        self.lift3name.setObjectName("lift3name")
        self.horizontalLayout_4.addWidget(self.lift3name)
        self.lift4name = QtWidgets.QLabel(self.layoutWidget)
        self.lift4name.setObjectName("lift4name")
        self.horizontalLayout_4.addWidget(self.lift4name)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.searching1 = QtWidgets.QLabel(self.layoutWidget)
        self.searching1.setObjectName("searching1")
        self.horizontalLayout.addWidget(self.searching1)
        self.searching2 = QtWidgets.QLabel(self.layoutWidget)
        self.searching2.setObjectName("searching2")
        self.horizontalLayout.addWidget(self.searching2)
        self.searching3 = QtWidgets.QLabel(self.layoutWidget)
        self.searching3.setObjectName("searching3")
        self.horizontalLayout.addWidget(self.searching3)
        self.searching4 = QtWidgets.QLabel(self.layoutWidget)
        self.searching4.setObjectName("searching4")
        self.horizontalLayout.addWidget(self.searching4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.departure1 = QtWidgets.QLabel(self.layoutWidget)
        self.departure1.setObjectName("departure1")
        self.horizontalLayout_2.addWidget(self.departure1)
        self.departure2 = QtWidgets.QLabel(self.layoutWidget)
        self.departure2.setObjectName("departure2")
        self.horizontalLayout_2.addWidget(self.departure2)
        self.departure3 = QtWidgets.QLabel(self.layoutWidget)
        self.departure3.setObjectName("departure3")
        self.horizontalLayout_2.addWidget(self.departure3)
        self.departure4 = QtWidgets.QLabel(self.layoutWidget)
        self.departure4.setObjectName("departure4")
        self.horizontalLayout_2.addWidget(self.departure4)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.people1 = QtWidgets.QTextBrowser(self.layoutWidget)
        self.people1.setEnabled(False)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.people1.setFont(font)
        self.people1.setObjectName("people1")
        self.horizontalLayout_3.addWidget(self.people1)
        self.people2 = QtWidgets.QTextBrowser(self.layoutWidget)
        self.people2.setEnabled(False)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.people2.setFont(font)
        self.people2.setObjectName("people2")
        self.horizontalLayout_3.addWidget(self.people2)
        self.people3 = QtWidgets.QTextBrowser(self.layoutWidget)
        self.people3.setEnabled(False)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.people3.setFont(font)
        self.people3.setObjectName("people3")
        self.horizontalLayout_3.addWidget(self.people3)
        self.people4 = QtWidgets.QTextBrowser(self.layoutWidget)
        self.people4.setEnabled(False)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.people4.setFont(font)
        self.people4.setObjectName("people4")
        self.horizontalLayout_3.addWidget(self.people4)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)
        Boolean_Elevator.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Boolean_Elevator)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1148, 21))
        self.menubar.setObjectName("menubar")
        Boolean_Elevator.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Boolean_Elevator)
        self.statusbar.setObjectName("statusbar")
        Boolean_Elevator.setStatusBar(self.statusbar)

        self.retranslateUi(Boolean_Elevator)
        QtCore.QMetaObject.connectSlotsByName(Boolean_Elevator)

    def retranslateUi(self, Boolean_Elevator):
        _translate = QtCore.QCoreApplication.translate
        Boolean_Elevator.setWindowTitle(_translate("Boolean_Elevator", "Boolean_Elevator"))
        self.controlButton.setText(_translate("Boolean_Elevator", "Начать Симуляцию"))
        self.label_14.setText(_translate("Boolean_Elevator", "Лифты"))
        self.searching.setText(_translate("Boolean_Elevator", "Поиск этажа"))
        self.departure.setText(_translate("Boolean_Elevator", "Разгрузка"))
        self.label_9.setText(_translate("Boolean_Elevator", "Люди в кабинах"))
        self.lift1name.setText(_translate("Boolean_Elevator", "Лифт 1"))
        self.lift2name.setText(_translate("Boolean_Elevator", "Лифт 2"))
        self.lift3name.setText(_translate("Boolean_Elevator", "Лифт 3"))
        self.lift4name.setText(_translate("Boolean_Elevator", "Лифт 4"))
        self.searching1.setText(_translate("Boolean_Elevator", "False"))
        self.searching2.setText(_translate("Boolean_Elevator", "False"))
        self.searching3.setText(_translate("Boolean_Elevator", "False"))
        self.searching4.setText(_translate("Boolean_Elevator", "False"))
        self.departure1.setText(_translate("Boolean_Elevator", "False"))
        self.departure2.setText(_translate("Boolean_Elevator", "False"))
        self.departure3.setText(_translate("Boolean_Elevator", "False"))
        self.departure4.setText(_translate("Boolean_Elevator", "False"))
