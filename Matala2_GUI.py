# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ido2.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
from PyQt4 import QtCore, QtGui
import sys
import M1 as m
import nmea_to_csv as c
import nema_to_kml_3 as kml

from PyQt4.QtGui import QFileDialog

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_NMEA(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
    def setupUi(self, NMEA):
        NMEA.setObjectName(_fromUtf8("NMEA"))
        NMEA.resize(866, 566)
        self.label = QtGui.QLabel(NMEA)
        self.label.setGeometry(QtCore.QRect(230, 0, 421, 61))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.openFile = QtGui.QPushButton(NMEA)
        self.openFile.setGeometry(QtCore.QRect(20, 110, 93, 28))
        self.openFile.setObjectName(_fromUtf8("openFile"))
        self.label_2 = QtGui.QLabel(NMEA)
        self.label_2.setGeometry(QtCore.QRect(20, 76, 241, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.fileText = QtGui.QTextEdit(NMEA)
        self.fileText.setGeometry(QtCore.QRect(260, 110, 591, 31))
        self.fileText.setObjectName(_fromUtf8("fileText"))
        self.label_3 = QtGui.QLabel(NMEA)
        self.label_3.setGeometry(QtCore.QRect(30, 480, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.box_kml = QtGui.QCheckBox(NMEA)
        self.box_kml.setGeometry(QtCore.QRect(200, 480, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.box_kml.setFont(font)
        self.box_kml.setChecked(True)
        self.box_kml.setObjectName(_fromUtf8("box_kml"))
        self.box_csv = QtGui.QCheckBox(NMEA)
        self.box_csv.setGeometry(QtCore.QRect(260, 480, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.box_csv.setFont(font)
        self.box_csv.setChecked(True)
        self.box_csv.setObjectName(_fromUtf8("box_csv"))
        self.label_4 = QtGui.QLabel(NMEA)
        self.label_4.setGeometry(QtCore.QRect(20, 250, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.box_lat = QtGui.QCheckBox(NMEA)
        self.box_lat.setGeometry(QtCore.QRect(320, 260, 71, 20))
        self.box_lat.setCheckable(True)
        self.box_lat.setChecked(True)
        self.box_lat.setObjectName(_fromUtf8("box_lat"))
        self.box_time = QtGui.QCheckBox(NMEA)
        self.box_time.setGeometry(QtCore.QRect(260, 260, 51, 20))
        self.box_time.setChecked(True)
        self.box_time.setObjectName(_fromUtf8("box_time"))
        self.box_quality = QtGui.QCheckBox(NMEA)
        self.box_quality.setGeometry(QtCore.QRect(720, 260, 61, 20))
        self.box_quality.setChecked(True)
        self.box_quality.setObjectName(_fromUtf8("box_quality"))
        self.box_long = QtGui.QCheckBox(NMEA)
        self.box_long.setGeometry(QtCore.QRect(400, 260, 81, 20))
        self.box_long.setChecked(True)
        self.box_long.setTristate(False)
        self.box_long.setObjectName(_fromUtf8("box_long"))
        self.box_speed = QtGui.QCheckBox(NMEA)
        self.box_speed.setGeometry(QtCore.QRect(790, 260, 61, 20))
        self.box_speed.setChecked(True)
        self.box_speed.setObjectName(_fromUtf8("box_speed"))
        self.box_nos = QtGui.QCheckBox(NMEA)
        self.box_nos.setGeometry(QtCore.QRect(570, 260, 141, 21))
        self.box_nos.setChecked(True)
        self.box_nos.setObjectName(_fromUtf8("box_nos"))
        self.box_altitude = QtGui.QCheckBox(NMEA)
        self.box_altitude.setGeometry(QtCore.QRect(490, 260, 71, 20))
        self.box_altitude.setChecked(True)
        self.box_altitude.setObjectName(_fromUtf8("box_altitude"))
        self.box_date = QtGui.QCheckBox(NMEA)
        self.box_date.setGeometry(QtCore.QRect(200, 260, 51, 20))
        self.box_date.setChecked(True)
        self.box_date.setObjectName(_fromUtf8("box_date"))
        self.label_5 = QtGui.QLabel(NMEA)
        self.label_5.setGeometry(QtCore.QRect(20, 165, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.folderText = QtGui.QTextEdit(NMEA)
        self.folderText.setGeometry(QtCore.QRect(260, 200, 591, 31))
        self.folderText.setObjectName(_fromUtf8("folderText"))
        self.openOutput = QtGui.QPushButton(NMEA)
        self.openOutput.setGeometry(QtCore.QRect(20, 200, 141, 28))
        self.openOutput.setObjectName(_fromUtf8("openOutput"))
        self.label_6 = QtGui.QLabel(NMEA)
        self.label_6.setGeometry(QtCore.QRect(750, 530, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.pushButton_3 = QtGui.QPushButton(NMEA)
        self.pushButton_3.setGeometry(QtCore.QRect(750, 500, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.openFolder = QtGui.QPushButton(NMEA)
        self.openFolder.setGeometry(QtCore.QRect(150, 110, 93, 28))
        self.openFolder.setObjectName(_fromUtf8("openFolder"))
        self.label_8 = QtGui.QLabel(NMEA)
        self.label_8.setGeometry(QtCore.QRect(120, 120, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(NMEA)
        self.label_9.setGeometry(QtCore.QRect(570, 310, 16, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_11 = QtGui.QLabel(NMEA)
        self.label_11.setGeometry(QtCore.QRect(20, 310, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_12 = QtGui.QLabel(NMEA)
        self.label_12.setGeometry(QtCore.QRect(200, 310, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.dateStart = QtGui.QDateTimeEdit(NMEA)
        self.dateStart.setGeometry(QtCore.QRect(410, 320, 151, 22))
        self.dateStart.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.dateStart.setObjectName(_fromUtf8("dateStart"))
        self.dateEnd = QtGui.QDateTimeEdit(NMEA)
        self.dateEnd.setGeometry(QtCore.QRect(590, 320, 151, 22))
        self.dateEnd.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.dateEnd.setDateTime(QtCore.QDateTime(QtCore.QDate(2017, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEnd.setObjectName(_fromUtf8("dateEnd"))
        self.altStart = QtGui.QSpinBox(NMEA)
        self.altStart.setGeometry(QtCore.QRect(410, 360, 61, 22))
        self.altStart.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.altStart.setMaximum(10000)
        self.altStart.setObjectName(_fromUtf8("altStart"))
        self.altEnd = QtGui.QSpinBox(NMEA)
        self.altEnd.setGeometry(QtCore.QRect(500, 360, 61, 22))
        self.altEnd.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.altEnd.setMaximum(99999)
        self.altEnd.setProperty("value", 99999)
        self.altEnd.setObjectName(_fromUtf8("altEnd"))
        self.label_13 = QtGui.QLabel(NMEA)
        self.label_13.setGeometry(QtCore.QRect(200, 350, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.label_10 = QtGui.QLabel(NMEA)
        self.label_10.setGeometry(QtCore.QRect(480, 350, 16, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_14 = QtGui.QLabel(NMEA)
        self.label_14.setGeometry(QtCore.QRect(200, 430, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.nosStart = QtGui.QSpinBox(NMEA)
        self.nosStart.setGeometry(QtCore.QRect(410, 440, 41, 22))
        self.nosStart.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.nosStart.setMaximum(8)
        self.nosStart.setObjectName(_fromUtf8("nosStart"))
        self.label_15 = QtGui.QLabel(NMEA)
        self.label_15.setGeometry(QtCore.QRect(470, 430, 16, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.nosEnd = QtGui.QSpinBox(NMEA)
        self.nosEnd.setGeometry(QtCore.QRect(500, 440, 41, 22))
        self.nosEnd.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.nosEnd.setMaximum(8)
        self.nosEnd.setProperty("value", 8)
        self.nosEnd.setObjectName(_fromUtf8("nosEnd"))
        self.label_16 = QtGui.QLabel(NMEA)
        self.label_16.setGeometry(QtCore.QRect(200, 390, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_16.setFont(font)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.speedStart = QtGui.QSpinBox(NMEA)
        self.speedStart.setGeometry(QtCore.QRect(410, 400, 61, 22))
        self.speedStart.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.speedStart.setMaximum(10000)
        self.speedStart.setObjectName(_fromUtf8("speedStart"))
        self.label_18 = QtGui.QLabel(NMEA)
        self.label_18.setGeometry(QtCore.QRect(480, 390, 16, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_18.setFont(font)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.speedEnd = QtGui.QSpinBox(NMEA)
        self.speedEnd.setGeometry(QtCore.QRect(500, 400, 61, 22))
        self.speedEnd.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.speedEnd.setMaximum(10000)
        self.speedEnd.setProperty("value", 10000)
        self.speedEnd.setObjectName(_fromUtf8("speedEnd"))

        self.retranslateUi(NMEA)
        QtCore.QMetaObject.connectSlotsByName(NMEA)

    def retranslateUi(self, NMEA):
        NMEA.setWindowTitle(_translate("NMEA", "NMEA TO KML/CSV", None))
        self.label.setText(_translate("NMEA", "NMEA TO KML/CSV", None))
        self.openFile.setText(_translate("NMEA", "Select File", None))
        self.label_2.setText(_translate("NMEA", "Select Input Folder or File:", None))
        self.label_3.setText(_translate("NMEA", "Convert to:", None))
        self.box_kml.setText(_translate("NMEA", "KML ", None))
        self.box_csv.setText(_translate("NMEA", "CSV", None))
        self.label_4.setText(_translate("NMEA", "Values to display:", None))
        self.box_lat.setText(_translate("NMEA", "Latitude", None))
        self.box_time.setText(_translate("NMEA", "Time", None))
        self.box_quality.setText(_translate("NMEA", "Quality", None))
        self.box_long.setText(_translate("NMEA", "Longtitude", None))
        self.box_speed.setText(_translate("NMEA", "Speed", None))
        self.box_nos.setText(_translate("NMEA", "Number of Satellites", None))
        self.box_altitude.setText(_translate("NMEA", "Altitude", None))
        self.box_date.setText(_translate("NMEA", "Date", None))
        self.label_5.setText(_translate("NMEA", "Select Output Folder:", None))
        self.openOutput.setText(_translate("NMEA", "Select Output Folder", None))
        self.label_6.setText(_translate("NMEA", "Created By R.I.O", None))
        self.pushButton_3.setText(_translate("NMEA", "Convert", None))
        self.openFolder.setText(_translate("NMEA", "Select Folder", None))
        self.label_8.setText(_translate("NMEA", "or", None))
        self.label_9.setText(_translate("NMEA", "_", None))
        self.label_11.setText(_translate("NMEA", "Filter by:", None))
        self.label_12.setText(_translate("NMEA", "Date and time:", None))
        self.dateStart.setDisplayFormat(_translate("NMEA", "HH:mm:ss dd/MM/yyyy", None))
        self.dateEnd.setDisplayFormat(_translate("NMEA", "HH:mm:ss dd/MM/yyyy", None))
        self.label_13.setText(_translate("NMEA", "Altitude (0-99999 m):", None))
        self.label_10.setText(_translate("NMEA", "_", None))
        self.label_14.setText(_translate("NMEA", "Number of Satellites (0-8):", None))
        self.label_15.setText(_translate("NMEA", "_", None))
        self.label_16.setText(_translate("NMEA", "Speed (km/h):", None))
        self.label_18.setText(_translate("NMEA", "_", None))
        self.pushButton_3.clicked.connect(self.convert)
        self.openFolder.clicked.connect(self.openFolderDialog)
        self.openOutput.clicked.connect(self.selectOutputFolder)
        self.openFile.clicked.connect(self.openFileDialog)
        self.folderText.setText('C:\\')
        self.fileText.setText('C:\\')
    def printd(self):
        print("ido")

    def openFileDialog(self):
        filter = "Nmea(*.nmea)"
        filename = QtGui.QFileDialog.getOpenFileNameAndFilter(self,"Open File", "C:\\nmea",filter)
        self.fileText.setText(filename[0])

    def openFolderDialog(self):
        foldername = QtGui.QFileDialog.getExistingDirectory(self, 'Select a folder:', 'C:\\', QtGui.QFileDialog.ShowDirsOnly)
        self.fileText.setText(foldername)
    def selectOutputFolder(self):
        foldername = QtGui.QFileDialog.getExistingDirectory(self, 'Select a folder:', 'C:\\', QtGui.QFileDialog.ShowDirsOnly)
        self.folderText.setText(foldername)

    def checkValues(self):
        arr=[0,0,0,0,0,0,0,0,0,0,0]

        if (self.box_time.isChecked()):
            arr[0] = 1
        if (self.box_date.isChecked()):
            arr[10] = 1
        if (self.box_lat.isChecked()):
            arr[1] = 1
        if (self.box_long.isChecked()):
            arr[3] = 1
        if (self.box_altitude.isChecked()):
            arr[8] = 1
        if (self.box_speed.isChecked()):
            arr[9] = 1
        if (self.box_quality.isChecked()):
            arr[5] = 1
        if (self.box_nos.isChecked()):
            arr[6]=1
        return arr

    def convert(self):
        fileText = self.fileText.toPlainText()
        outputText = self.folderText.toPlainText()
        arr = self.checkValues()
        #filter=[Date and time start, Date and time end, altitude start, altitude end, speed start, speed end, nos start, nos end]
        filter=[self.dateStart.text(),self.dateEnd.text(),self.altStart.text(),self.altEnd.text(),self.speedStart.text(),self.speedEnd.text(), self.nosStart.text(),self.nosEnd.text()]

        if (fileText==''):
            self.folderText.setText("Pleasse select a vaild path")
            print("1")
        elif ".nmea" in fileText :

            m.read_file(fileText,0)
            if self.box_csv.isChecked():
                    c.create_csv(0, outputText,arr)
            if self.box_kml.isChecked():
                    kml.create_kml(0, outputText,arr)
            print("2")
        else:
            i=  m.read_dir(fileText)
            if self.box_csv.isChecked():
                for x in range(1, i + 1):
                     c.create_csv(x,outputText,arr,filter)
            if self.box_kml.isChecked():
                for x in range(1, i + 1):
                    kml.create_kml(x,outputText,arr,filter)
            print("3")


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Ui_NMEA()
    ex.show()
    sys.exit(app.exec_())