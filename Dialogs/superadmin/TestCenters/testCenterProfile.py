from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class testCenterProfile(object):
    def setup(self, testCenterProfile,data):
        testCenterProfile.setObjectName("testCenterProfile")
        testCenterProfile.resize(472, 433)
        self.OKButton = QtWidgets.QPushButton(testCenterProfile)
        self.OKButton.setGeometry(QtCore.QRect(330, 380, 131, 41))
        self.OKButton.setObjectName("OKButton")
        self.frame = QtWidgets.QFrame(testCenterProfile)
        self.frame.setGeometry(QtCore.QRect(10, 20, 451, 351))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.nameLabel = QtWidgets.QLabel(self.frame)
        self.nameLabel.setGeometry(QtCore.QRect(25, 40, 81, 41))
        self.nameLabel.setObjectName("nameLabel")
        self.addressLabel = QtWidgets.QLabel(self.frame)
        self.addressLabel.setGeometry(QtCore.QRect(25, 90, 91, 41))
        self.addressLabel.setObjectName("addressLabel")
        self.contactLabel = QtWidgets.QLabel(self.frame)
        self.contactLabel.setGeometry(QtCore.QRect(25, 300, 131, 41))
        self.contactLabel.setObjectName("contactLabel")
        self.stateLabel = QtWidgets.QLabel(self.frame)
        self.stateLabel.setGeometry(QtCore.QRect(25, 210, 61, 41))
        self.stateLabel.setObjectName("stateLabel")
        self.pinCodeLabel = QtWidgets.QLabel(self.frame)
        self.pinCodeLabel.setGeometry(QtCore.QRect(25, 170, 91, 41))
        self.pinCodeLabel.setObjectName("pinCodeLabel")
        self.cityLabel = QtWidgets.QLabel(self.frame)
        self.cityLabel.setGeometry(QtCore.QRect(25, 260, 61, 41))
        self.cityLabel.setObjectName("cityLabel")
        self.name = QtWidgets.QLabel(self.frame)
        self.name.setGeometry(QtCore.QRect(170, 40, 281, 41))
        self.name.setStyleSheet("font-size:12pt;")
        self.name.setObjectName("name")
        self.address = QtWidgets.QLabel(self.frame)
        self.address.setGeometry(QtCore.QRect(170, 90, 281, 71))
        self.address.setStyleSheet("font-size:12pt;")
        self.address.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.address.setObjectName("address")
        self.pinCode = QtWidgets.QLabel(self.frame)
        self.pinCode.setGeometry(QtCore.QRect(170, 170, 181, 41))
        self.pinCode.setStyleSheet("font-size:12pt;")
        self.pinCode.setObjectName("pinCode")
        self.state = QtWidgets.QLabel(self.frame)
        self.state.setGeometry(QtCore.QRect(170, 210, 181, 41))
        self.state.setStyleSheet("font-size:12pt;")
        self.state.setObjectName("state")
        self.city = QtWidgets.QLabel(self.frame)
        self.city.setGeometry(QtCore.QRect(170, 260, 181, 41))
        self.city.setStyleSheet("font-size:12pt;")
        self.city.setObjectName("city")
        self.contactNo = QtWidgets.QLabel(self.frame)
        self.contactNo.setGeometry(QtCore.QRect(170, 305, 181, 31))
        self.contactNo.setStyleSheet("font-size:12pt;")
        self.contactNo.setObjectName("contactNo")
        self.IDLabel = QtWidgets.QLabel(self.frame)
        self.IDLabel.setGeometry(QtCore.QRect(25, 10, 141, 41))
        self.IDLabel.setObjectName("IDLabel")
        self.testCenterID = QtWidgets.QLabel(self.frame)
        self.testCenterID.setGeometry(QtCore.QRect(170, 10, 281, 41))
        self.testCenterID.setStyleSheet("font-size:12pt;\n"
                                        "font-weight:bold;")
        self.testCenterID.setObjectName("testCenterID")

        self.retranslateUi(testCenterProfile,data)
        QtCore.QMetaObject.connectSlotsByName(testCenterProfile)

    def retranslateUi(self, testCenterProfile,data):
        _translate = QtCore.QCoreApplication.translate
        testCenterProfile.setWindowTitle(_translate("testCenterProfile", "Test Center Profile"))
        self.OKButton.setText(_translate("testCenterProfile", "OK"))
        self.nameLabel.setText(_translate("testCenterProfile", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Name :</span></p></body></html>"))
        self.addressLabel.setText(_translate("testCenterProfile", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Address :</span></p></body></html>"))
        self.contactLabel.setText(_translate("testCenterProfile", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Contact No. :</span></p></body></html>"))
        self.stateLabel.setText(_translate("testCenterProfile", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">State :</span></p></body></html>"))
        self.pinCodeLabel.setText(_translate("testCenterProfile", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Pin Code :</span></p></body></html>"))
        self.cityLabel.setText(_translate("testCenterProfile", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">City :</span></p></body></html>"))
        self.name.setText(_translate("testCenterProfile", "name"))
        self.address.setText(_translate("testCenterProfile", "address"))
        self.pinCode.setText(_translate("testCenterProfile", "pin_code"))
        self.state.setText(_translate("testCenterProfile", "state"))
        self.city.setText(_translate("testCenterProfile", "city"))
        self.contactNo.setText(_translate("testCenterProfile", "contact_no"))
        self.IDLabel.setText(_translate("testCenterProfile", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Test Center ID :</span></p></body></html>"))
        self.testCenterID.setText(_translate("testCenterProfile", "test_center_ID"))

        self.events(testCenterProfile,data)

    def events(self,parent,data):
        self.address.setText(str(data["address"]))
        self.testCenterID.setText(str(data["id"]))
        self.pinCode.setText(str(data["pin"]))
        self.state.setText(str(data["state"]))
        self.city.setText(str(data["city"]))
        self.contactNo.setText(str(data["contact"]))
        self.name.setText(str(data["name"]))
        
        self.OKButton.clicked.connect(lambda: parent.close())

