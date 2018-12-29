from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Dialogs.superadmin.Events.addEvent import *
from Dialogs.superadmin.Events.selectEvent import *
from Dialogs.superadmin.Events.viewEvents import *


class Events(object):
    def setup(self, Events, superadmin):
        Events.setObjectName("Events")
        Events.resize(1366, 768)
        self.centralwidget = QtWidgets.QWidget(Events)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(550, 20, 255, 70))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title.sizePolicy().hasHeightForWidth())
        self.title.setSizePolicy(sizePolicy)
        self.title.setMinimumSize(QtCore.QSize(0, 50))
        self.title.setMaximumSize(QtCore.QSize(400, 70))
        self.title.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.title.setObjectName("title")
        self.logout = QtWidgets.QPushButton(self.centralwidget)
        self.logout.setGeometry(QtCore.QRect(1240, 10, 101, 91))
        self.logout.setStyleSheet("border:none;")
        self.logout.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../MDTouch/Images/logout.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.logout.setIcon(icon)
        self.logout.setIconSize(QtCore.QSize(80, 80))
        self.logout.setObjectName("logout")
        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(30, 0, 101, 100))
        self.back.setStyleSheet("border:none;")
        self.back.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../MDTouch/Images/back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.back.setIcon(icon1)
        self.back.setIconSize(QtCore.QSize(80, 80))
        self.back.setObjectName("back")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 100, 1371, 80))
        self.frame.setStyleSheet("background-color: rgb(85, 255, 127);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(120, 0, 1131, 80))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.hospitals = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.hospitals.setMaximumSize(QtCore.QSize(80, 80))
        self.hospitals.setStyleSheet("border:none;")
        self.hospitals.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../MDTouch/Images/hospital.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.hospitals.setIcon(icon2)
        self.hospitals.setIconSize(QtCore.QSize(50, 50))
        self.hospitals.setObjectName("hospitals")
        self.horizontalLayout_4.addWidget(self.hospitals)
        self.events = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.events.setMaximumSize(QtCore.QSize(80, 80))
        self.events.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"border:none;")
        self.events.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../MDTouch/Images/event.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.events.setIcon(icon3)
        self.events.setIconSize(QtCore.QSize(50, 50))
        self.events.setObjectName("events")
        self.horizontalLayout_4.addWidget(self.events)
        self.bloodBank = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.bloodBank.setMaximumSize(QtCore.QSize(80, 80))
        self.bloodBank.setStyleSheet("border:none;")
        self.bloodBank.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../MDTouch/Images/bloodbank.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bloodBank.setIcon(icon4)
        self.bloodBank.setIconSize(QtCore.QSize(50, 50))
        self.bloodBank.setObjectName("bloodBank")
        self.horizontalLayout_4.addWidget(self.bloodBank)
        self.testCenters = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.testCenters.setMaximumSize(QtCore.QSize(80, 80))
        self.testCenters.setStyleSheet("border:none;")
        self.testCenters.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../MDTouch/Images/test_2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.testCenters.setIcon(icon5)
        self.testCenters.setIconSize(QtCore.QSize(50, 50))
        self.testCenters.setObjectName("testCenters")
        self.horizontalLayout_4.addWidget(self.testCenters)
        self.doctors = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.doctors.setMaximumSize(QtCore.QSize(80, 80))
        self.doctors.setStyleSheet("border:none;")
        self.doctors.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("../MDTouch/Images/doctor.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.doctors.setIcon(icon6)
        self.doctors.setIconSize(QtCore.QSize(50, 50))
        self.doctors.setObjectName("doctors")
        self.horizontalLayout_4.addWidget(self.doctors)
        self.dispensary = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.dispensary.setMaximumSize(QtCore.QSize(80, 80))
        self.dispensary.setStyleSheet("border:none;")
        self.dispensary.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("../MDTouch/Images/dispensary.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.dispensary.setIcon(icon7)
        self.dispensary.setIconSize(QtCore.QSize(50, 50))
        self.dispensary.setObjectName("dispensary")
        self.horizontalLayout_4.addWidget(self.dispensary)
        self.emergency = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.emergency.setMaximumSize(QtCore.QSize(80, 80))
        self.emergency.setStyleSheet("border:none;")
        self.emergency.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("../MDTouch/Images/ambulance.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.emergency.setIcon(icon8)
        self.emergency.setIconSize(QtCore.QSize(50, 50))
        self.emergency.setObjectName("emergency")
        self.horizontalLayout_4.addWidget(self.emergency)
        self.deleteEventLabel = QtWidgets.QLabel(self.centralwidget)
        self.deleteEventLabel.setGeometry(QtCore.QRect(980, 370, 112, 80))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deleteEventLabel.sizePolicy().hasHeightForWidth())
        self.deleteEventLabel.setSizePolicy(sizePolicy)
        self.deleteEventLabel.setObjectName("deleteEventLabel")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 230, 1291, 151))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.addEvent = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.addEvent.setMaximumSize(QtCore.QSize(120, 120))
        self.addEvent.setStyleSheet("border:none;")
        self.addEvent.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("../MDTouch/Images/add_event.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addEvent.setIcon(icon9)
        self.addEvent.setIconSize(QtCore.QSize(100, 100))
        self.addEvent.setObjectName("addEvent")
        self.horizontalLayout.addWidget(self.addEvent)
        self.viewEvents = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.viewEvents.sizePolicy().hasHeightForWidth())
        self.viewEvents.setSizePolicy(sizePolicy)
        self.viewEvents.setMaximumSize(QtCore.QSize(120, 120))
        self.viewEvents.setStyleSheet("border:none;")
        self.viewEvents.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("../MDTouch/Images/search_hospital.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.viewEvents.setIcon(icon10)
        self.viewEvents.setIconSize(QtCore.QSize(100, 100))
        self.viewEvents.setObjectName("viewEvents")
        self.horizontalLayout.addWidget(self.viewEvents)
        self.deleteEvent = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.deleteEvent.setMaximumSize(QtCore.QSize(120, 120))
        self.deleteEvent.setStyleSheet("border:none;")
        self.deleteEvent.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("../MDTouch/Images/delete_event.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.deleteEvent.setIcon(icon11)
        self.deleteEvent.setIconSize(QtCore.QSize(100, 100))
        self.deleteEvent.setObjectName("deleteEvent")
        self.horizontalLayout.addWidget(self.deleteEvent)
        self.addEventLabel = QtWidgets.QLabel(self.centralwidget)
        self.addEventLabel.setGeometry(QtCore.QRect(260, 370, 126, 80))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addEventLabel.sizePolicy().hasHeightForWidth())
        self.addEventLabel.setSizePolicy(sizePolicy)
        self.addEventLabel.setObjectName("addEventLabel")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(210, 520, 1011, 161))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.eventStatistics = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.eventStatistics.sizePolicy().hasHeightForWidth())
        self.eventStatistics.setSizePolicy(sizePolicy)
        self.eventStatistics.setMaximumSize(QtCore.QSize(120, 120))
        self.eventStatistics.setStyleSheet("border:none;")
        self.eventStatistics.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("../MDTouch/Images/statistics.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.eventStatistics.setIcon(icon12)
        self.eventStatistics.setIconSize(QtCore.QSize(100, 100))
        self.eventStatistics.setObjectName("eventStatistics")
        self.horizontalLayout_2.addWidget(self.eventStatistics)
        self.broadcast = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.broadcast.sizePolicy().hasHeightForWidth())
        self.broadcast.setSizePolicy(sizePolicy)
        self.broadcast.setMaximumSize(QtCore.QSize(120, 120))
        self.broadcast.setStyleSheet("border:none;")
        self.broadcast.setText("")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("../MDTouch/Images/broadcast.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.broadcast.setIcon(icon13)
        self.broadcast.setIconSize(QtCore.QSize(100, 100))
        self.broadcast.setObjectName("broadcast")
        self.horizontalLayout_2.addWidget(self.broadcast)
        self.eventStatisticsLabel = QtWidgets.QLabel(self.centralwidget)
        self.eventStatisticsLabel.setGeometry(QtCore.QRect(460, 660, 145, 81))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.eventStatisticsLabel.sizePolicy().hasHeightForWidth())
        self.eventStatisticsLabel.setSizePolicy(sizePolicy)
        self.eventStatisticsLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.eventStatisticsLabel.setObjectName("eventStatisticsLabel")
        self.viewEventsLabel = QtWidgets.QLabel(self.centralwidget)
        self.viewEventsLabel.setGeometry(QtCore.QRect(620, 370, 126, 80))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.viewEventsLabel.sizePolicy().hasHeightForWidth())
        self.viewEventsLabel.setSizePolicy(sizePolicy)
        self.viewEventsLabel.setObjectName("viewEventsLabel")
        self.broadcastLabel = QtWidgets.QLabel(self.centralwidget)
        self.broadcastLabel.setGeometry(QtCore.QRect(820, 660, 161, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.broadcastLabel.sizePolicy().hasHeightForWidth())
        self.broadcastLabel.setSizePolicy(sizePolicy)
        self.broadcastLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.broadcastLabel.setObjectName("broadcastLabel")
        self.inbox = QtWidgets.QPushButton(self.centralwidget)
        self.inbox.setGeometry(QtCore.QRect(1130, 0, 80, 80))
        self.inbox.setMaximumSize(QtCore.QSize(100, 100))
        self.inbox.setStyleSheet("border:none;")
        self.inbox.setText("")
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap("../MDTouch/Images/inbox.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.inbox.setIcon(icon15)
        self.inbox.setIconSize(QtCore.QSize(80, 80))
        self.inbox.setObjectName("inbox")
        Events.setCentralWidget(self.centralwidget)

        self.retranslateUi(Events, superadmin)
        QtCore.QMetaObject.connectSlotsByName(Events)

    def retranslateUi(self, Events, superadmin):
        _translate = QtCore.QCoreApplication.translate
        Events.setWindowTitle(_translate("Events", "MainWindow"))
        self.title.setText(_translate("Events", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:36pt; font-weight:600; text-decoration: underline;\">MDTouch</span></p></body></html>"))
        self.deleteEventLabel.setText(_translate("Events", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; text-decoration: underline;\">Delete</span></p><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; text-decoration: underline;\">Event</span></p></body></html>"))
        self.addEventLabel.setText(_translate("Events", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; text-decoration: underline;\">Add</span></p><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; text-decoration: underline;\">Event</span></p></body></html>"))
        self.eventStatisticsLabel.setText(_translate("Events", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; text-decoration: underline;\">Statistics</span></p></body></html>"))
        self.viewEventsLabel.setText(_translate("Events", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; text-decoration: underline;\">View</span></p><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; text-decoration: underline;\">Events</span></p></body></html>"))
        self.broadcastLabel.setText(_translate("Events", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; text-decoration: underline;\">Broadcast</span></p></body></html>"))

        self.clickEvents(Events, superadmin)

    def clickEvents(self, parent, superadmin):
        self.hospitals.clicked.connect(lambda: self.clickOnHospital(parent, superadmin))
        self.bloodBank.clicked.connect(lambda: self.clickOnBloodBank(parent, superadmin))
        self.testCenters.clicked.connect(lambda: self.clickOnTestCenters(parent, superadmin))
        self.emergency.clicked.connect(lambda: self.clickOnEmergency(parent, superadmin))
        self.dispensary.clicked.connect(lambda: self.clickOnDispensary(parent, superadmin))
        self.doctors.clicked.connect(lambda: self.clickOnDoctors(parent, superadmin))
        self.inbox.clicked.connect(lambda: self.clickOnInbox(parent, superadmin))
        self.logout.clicked.connect(lambda: self.clickOnLogOut(parent, superadmin))
        self.back.clicked.connect(lambda: self.clickOnBack(parent, superadmin))

        self.addEvent.clicked.connect(lambda: self.clickOnAddEvent())
        self.deleteEvent.clicked.connect(lambda: self.clickOnDeleteEvent())
        self.viewEvents.clicked.connect(lambda : self.clickOnViewEvent())

    def clickOnHospital(self, parent, superadmin):
        superadmin.hospital_home.setup(parent, superadmin)

    def clickOnBloodBank(self, parent, superadmin):
        superadmin.bloodbank_home.setup(parent, superadmin)

    def clickOnTestCenters(self, parent, superadmin):
        superadmin.testcenter_home.setup(parent, superadmin)

    def clickOnEmergency(self, parent, superadmin):
        superadmin.emergency_home.setup(parent, superadmin)

    def clickOnDispensary(self, parent, superadmin):
        superadmin.dispensary_home.setup(parent, superadmin)

    def clickOnDoctors(self, parent, superadmin):
        superadmin.doctor_home.setup(parent, superadmin)

    def clickOnInbox(self, parent, superadmin):
        pass

    def clickOnLogOut(self, parent, superadmin):
        parent.loginpage.setup(parent)

    def clickOnBack(self, parent, superadmin):
        superadmin.setup(parent)

    def clickOnAddEvent(self):
        self.window = QDialog()
        self.dialog = addEvent()
        self.dialog.setup(self.window)
        self.window.setModal(True)
        self.window.show()

    def clickOnDeleteEvent(self):
        self.window = QDialog()
        self.dialog = selectEvent()
        self.dialog.setup(self.window)
        self.window.setModal(True)
        self.window.show()

    def clickOnViewEvent(self):
        self.window = QDialog()
        self.dialog = viewEvent()
        self.dialog.setup(self.window)
        self.window.setModal(True)
        self.window.show()
