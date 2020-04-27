# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_multitabs.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, \
    QSlider, QStyle, QSizePolicy, QFileDialog
import sys
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import Qt, QUrl
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(772, 440)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.labelip1 = QtWidgets.QLabel(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelip1.sizePolicy().hasHeightForWidth())
        self.labelip1.setSizePolicy(sizePolicy)
        self.labelip1.setMinimumSize(QtCore.QSize(360, 240))
        self.labelip1.setMaximumSize(QtCore.QSize(16777215, 500))
        self.labelip1.setSizeIncrement(QtCore.QSize(3, 2))
        self.labelip1.setScaledContents(True)
        self.labelip1.setObjectName("labelip1")
        self.verticalLayout_2.addWidget(self.labelip1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.startbtn1 = QtWidgets.QPushButton(self.tab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.startbtn1.setFont(font)
        self.startbtn1.setObjectName("startbtn1")
        self.horizontalLayout.addWidget(self.startbtn1)
        self.prbtn1 = QtWidgets.QPushButton(self.tab)
        self.prbtn1.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.prbtn1.setFont(font)
        self.prbtn1.setObjectName("prbtn1")
        self.horizontalLayout.addWidget(self.prbtn1)
        self.frbtn1 = QtWidgets.QPushButton(self.tab)
        self.frbtn1.setMinimumSize(QtCore.QSize(150, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.frbtn1.setFont(font)
        self.frbtn1.setObjectName("frbtn1")
        self.horizontalLayout.addWidget(self.frbtn1)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.stopbtn1 = QtWidgets.QPushButton(self.tab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.stopbtn1.setFont(font)
        self.stopbtn1.setObjectName("stopbtn1")
        self.horizontalLayout_2.addWidget(self.stopbtn1)
        self.apbtn1 = QtWidgets.QPushButton(self.tab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.apbtn1.setFont(font)
        self.apbtn1.setObjectName("apbtn1")
        self.horizontalLayout_2.addWidget(self.apbtn1)
        self.fdbtn1 = QtWidgets.QPushButton(self.tab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.fdbtn1.setFont(font)
        self.fdbtn1.setObjectName("fdbtn1")
        self.horizontalLayout_2.addWidget(self.fdbtn1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.setStretch(0, 4)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 1)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.labelip2 = QtWidgets.QLabel(self.tab)
        self.labelip2.setMinimumSize(QtCore.QSize(360, 240))
        self.labelip2.setScaledContents(True)
        self.labelip2.setObjectName("labelip2")
        self.verticalLayout_3.addWidget(self.labelip2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.startbtn2 = QtWidgets.QPushButton(self.tab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.startbtn2.setFont(font)
        self.startbtn2.setObjectName("startbtn2")
        self.horizontalLayout_3.addWidget(self.startbtn2)
        self.prbtn2 = QtWidgets.QPushButton(self.tab)
        self.prbtn2.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.prbtn2.setFont(font)
        self.prbtn2.setObjectName("prbtn2")
        self.horizontalLayout_3.addWidget(self.prbtn2)
        self.frbtn2 = QtWidgets.QPushButton(self.tab)
        self.frbtn2.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.frbtn2.setFont(font)
        self.frbtn2.setObjectName("frbtn2")
        self.horizontalLayout_3.addWidget(self.frbtn2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.stopbtn2 = QtWidgets.QPushButton(self.tab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.stopbtn2.setFont(font)
        self.stopbtn2.setObjectName("stopbtn2")
        self.horizontalLayout_4.addWidget(self.stopbtn2)
        self.apbtn2 = QtWidgets.QPushButton(self.tab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.apbtn2.setFont(font)
        self.apbtn2.setObjectName("apbtn2")
        self.horizontalLayout_4.addWidget(self.apbtn2)
        self.fdbtn2 = QtWidgets.QPushButton(self.tab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.fdbtn2.setFont(font)
        self.fdbtn2.setObjectName("fdbtn2")
        self.horizontalLayout_4.addWidget(self.fdbtn2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.verticalLayout_3.setStretch(0, 4)
        self.verticalLayout_3.setStretch(1, 1)
        self.verticalLayout_3.setStretch(2, 1)
        self.horizontalLayout_5.addLayout(self.verticalLayout_3)
        self.tabWidget.addTab(self.tab, "")
        self.tab2 = QtWidgets.QWidget()
        self.tab2.setObjectName("tab2")
        self.videoslider = QtWidgets.QSlider(self.tab2)
        self.videoslider.setGeometry(QtCore.QRect(540, 20, 160, 22))
        self.videoslider.setOrientation(QtCore.Qt.Horizontal)
        self.videoslider.setObjectName("videoslider")
        self.widget = QtWidgets.QWidget(self.tab2)
        self.widget.setGeometry(QtCore.QRect(10, 10, 490, 40))
        self.widget.setObjectName("widget")
        self.hboxlayout = QtWidgets.QHBoxLayout(self.widget)
        self.hboxlayout.setContentsMargins(0, 0, 0, 0)
        self.hboxlayout.setObjectName("hboxlayout")
        self.open = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.open.setFont(font)
        self.open.setObjectName("open")
        self.hboxlayout.addWidget(self.open)
        self.stop = QtWidgets.QPushButton(self.widget)
        self.stop.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/syop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stop.setIcon(icon)
        self.stop.setIconSize(QtCore.QSize(30, 30))
        self.stop.setObjectName("stop")
        self.hboxlayout.addWidget(self.stop)
        self.prev = QtWidgets.QPushButton(self.widget)
        self.prev.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.prev.setIcon(icon1)
        self.prev.setIconSize(QtCore.QSize(30, 30))
        self.prev.setObjectName("prev")
        self.hboxlayout.addWidget(self.prev)
        self.start = QtWidgets.QPushButton(self.widget)
        self.start.setText("")
        global icon2
        global icon5
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.start.setIcon(icon2)
        self.start.setIconSize(QtCore.QSize(30, 30))
        self.start.setObjectName("start")
        self.hboxlayout.addWidget(self.start)
        self.next = QtWidgets.QPushButton(self.widget)
        self.next.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/forward.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.next.setIcon(icon3)
        self.next.setIconSize(QtCore.QSize(30, 30))
        self.next.setObjectName("next")
        self.hboxlayout.addWidget(self.next)
        self.sound = QtWidgets.QPushButton(self.widget)
        self.sound.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/audio-icon-music-icon-sound-icon-speaker-icon-volume-icon-logo-symbol-png-clip-art.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sound.setIcon(icon4)
        self.sound.setIconSize(QtCore.QSize(30, 30))
        self.sound.setObjectName("sound")
        self.hboxlayout.addWidget(self.sound)
        self.volslider = QtWidgets.QSlider(self.widget)
        self.volslider.setOrientation(QtCore.Qt.Horizontal)
        self.volslider.setObjectName("volslider")
        self.hboxlayout.addWidget(self.volslider)
        self.fsbtn = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.fsbtn.setFont(font)
        self.fsbtn.setObjectName("fsbtn")
        self.hboxlayout.addWidget(self.fsbtn)
        self.tabWidget.addTab(self.tab2, "")
        self.tab3 = QtWidgets.QWidget()
        self.tab3.setObjectName("tab3")
        self.tabWidget.addTab(self.tab3, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 772, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        
        
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        
        videowidget = QVideoWidget()
        
        self.start.setEnabled(False)
        self.start.clicked.connect(self.play_video)
        self.open.clicked.connect(self.open_file)
        
        self.videoslider.setRange(0,0)
        self.videoslider.sliderMoved.connect(self.set_position)
        
        vboxlayout =QVBoxLayout()
        vboxlayout.addWidget(videowidget)
        vboxlayout.addWidget(self.videoslider)
        vboxlayout.addLayout(self.hboxlayout)
        self.tab2.setLayout(vboxlayout)
        
        self.mediaPlayer.setVideoOutput(videowidget)
        
        self.mediaPlayer.stateChanged.connect(self.mediastate_changed)
        self.mediaPlayer.positionChanged.connect(self.position_changed)
        self.mediaPlayer.durationChanged.connect(self.duration_changed)
 
        
 

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(self.tab2, "Open Video")
 
        if filename != '':
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(filename)))
            self.start.setEnabled(True)
 
 
    def play_video(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
 
        else:
            self.mediaPlayer.play()
 
 
    def mediastate_changed(self, state):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.start.setIcon(icon5)
 
        else:
            self.start.setIcon(icon2)

    def position_changed(self, position):
        self.videoslider.setValue(position)
 
 
    def duration_changed(self, duration):
        self.videoslider.setRange(0, duration)
 
 
    def set_position(self, position):
        self.mediaPlayer.setPosition(position)
 


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelip1.setText(_translate("MainWindow", "TextLabel"))
        self.startbtn1.setText(_translate("MainWindow", "Start"))
        self.prbtn1.setText(_translate("MainWindow", "Person ReID"))
        self.frbtn1.setText(_translate("MainWindow", "Face Recognition"))
        self.stopbtn1.setText(_translate("MainWindow", "Stop"))
        self.apbtn1.setText(_translate("MainWindow", "Area Protection"))
        self.fdbtn1.setText(_translate("MainWindow", "Fall Detection"))
        self.labelip2.setText(_translate("MainWindow", "TextLabel"))
        self.startbtn2.setText(_translate("MainWindow", "Start"))
        self.prbtn2.setText(_translate("MainWindow", "Person ReID"))
        self.frbtn2.setText(_translate("MainWindow", "Face Recognition"))
        self.stopbtn2.setText(_translate("MainWindow", "Stop"))
        self.apbtn2.setText(_translate("MainWindow", "Area Protection"))
        self.fdbtn2.setText(_translate("MainWindow", "Fall Detection"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "2 IP CAMs"))
        self.open.setText(_translate("MainWindow", "Open"))
        self.fsbtn.setText(_translate("MainWindow", "Full Screen"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), _translate("MainWindow", "PLAY RECORD"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab3), _translate("MainWindow", "SETTINGS"))

import icons_rc

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

