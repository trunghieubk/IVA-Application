# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_multitabs.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QFileDialog, QApplication
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap
import sys
import cv2
from datetime import datetime,date
import os
import numpy as np
iplink=0;
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(772, 410)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.labelip1 = QtWidgets.QLabel(self.tab)
        self.labelip1.setMinimumSize(QtCore.QSize(360, 240))
        self.labelip1.setMaximumSize(QtCore.QSize(16777215, 500))
        self.labelip1.setFrameShape(QtWidgets.QFrame.Box)
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
        self.labelip2.setMaximumSize(QtCore.QSize(16777215, 500))
        self.labelip2.setFrameShape(QtWidgets.QFrame.Box)
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
        self.open = QtWidgets.QPushButton(self.tab2)
        self.open.setGeometry(QtCore.QRect(11, 17, 75, 26))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.open.setFont(font)
        self.open.setObjectName("open")
        self.stop = QtWidgets.QPushButton(self.tab2)
        self.stop.setGeometry(QtCore.QRect(92, 11, 42, 38))
        self.stop.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/syop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stop.setIcon(icon)
        self.stop.setIconSize(QtCore.QSize(30, 30))
        self.stop.setObjectName("stop")
        self.prev = QtWidgets.QPushButton(self.tab2)
        self.prev.setGeometry(QtCore.QRect(140, 11, 42, 38))
        self.prev.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.prev.setIcon(icon1)
        self.prev.setIconSize(QtCore.QSize(30, 30))
        self.prev.setObjectName("prev")
        self.start = QtWidgets.QPushButton(self.tab2)
        self.start.setGeometry(QtCore.QRect(188, 11, 42, 38))
        self.start.setText("")
        global icon2, icon5
        icon2 = QtGui.QIcon()
        icon5 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon5.addPixmap(QtGui.QPixmap(":/icons/pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.start.setIcon(icon2)
        self.start.setIconSize(QtCore.QSize(30, 30))
        self.start.setObjectName("start")
        self.next = QtWidgets.QPushButton(self.tab2)
        self.next.setGeometry(QtCore.QRect(236, 11, 42, 38))
        self.next.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/forward.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.next.setIcon(icon3)
        self.next.setIconSize(QtCore.QSize(30, 30))
        self.next.setObjectName("next")
        self.sound = QtWidgets.QPushButton(self.tab2)
        self.sound.setGeometry(QtCore.QRect(284, 11, 42, 38))
        self.sound.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/audio-icon-music-icon-sound-icon-speaker-icon-volume-icon-logo-symbol-png-clip-art.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sound.setIcon(icon4)
        self.sound.setIconSize(QtCore.QSize(30, 30))
        self.sound.setObjectName("sound")
        self.volslider = QtWidgets.QSlider(self.tab2)
        self.volslider.setGeometry(QtCore.QRect(332, 19, 84, 22))
        self.volslider.setOrientation(QtCore.Qt.Horizontal)
        self.volslider.setObjectName("volslider")
        self.fsbtn = QtWidgets.QPushButton(self.tab2)
        self.fsbtn.setGeometry(QtCore.QRect(422, 17, 77, 26))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.fsbtn.setFont(font)
        self.fsbtn.setObjectName("fsbtn")
        self.tabWidget.addTab(self.tab2, "")
        self.tab3 = QtWidgets.QWidget()
        self.tab3.setObjectName("tab3")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.tab3)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.drlb1 = QtWidgets.QLabel(self.tab3)
        self.drlb1.setMinimumSize(QtCore.QSize(320, 240))
        self.drlb1.setMaximumSize(QtCore.QSize(16777215, 500))
        self.drlb1.setFrameShape(QtWidgets.QFrame.Box)
        self.drlb1.setObjectName("drlb1")
        self.drlb1.resize(int(self.labelip1.width()), int(self.labelip1.height()))
        self.drlb1.setScaledContents(True)
        self.verticalLayout_6.addWidget(self.drlb1)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.draw1 = QtWidgets.QPushButton(self.tab3)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.draw1.setFont(font)
        self.draw1.setObjectName("draw1")
        self.horizontalLayout_11.addWidget(self.draw1)
        self.remove1 = QtWidgets.QPushButton(self.tab3)
        self.remove1.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.remove1.setFont(font)
        self.remove1.setObjectName("remove1")
        self.horizontalLayout_11.addWidget(self.remove1)
        self.verticalLayout_6.addLayout(self.horizontalLayout_11)
        self.verticalLayout_6.setStretch(0, 2)
        self.verticalLayout_6.setStretch(1, 1)
        self.horizontalLayout_13.addLayout(self.verticalLayout_6)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.drlb2 = QtWidgets.QLabel(self.tab3)
        self.drlb2.setMinimumSize(QtCore.QSize(320, 240))
        self.drlb2.setMaximumSize(QtCore.QSize(16777215, 500))
        self.drlb2.setFrameShape(QtWidgets.QFrame.Box)
        self.drlb2.setObjectName("drlb2")
        self.drlb2.resize(self.labelip2.width(), self.labelip2.height())
        self.drlb2.setScaledContents(True)
        self.verticalLayout_7.addWidget(self.drlb2)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.draw2 = QtWidgets.QPushButton(self.tab3)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.draw2.setFont(font)
        self.draw2.setObjectName("draw2")
        self.horizontalLayout_12.addWidget(self.draw2)
        self.remove2 = QtWidgets.QPushButton(self.tab3)
        self.remove2.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.remove2.setFont(font)
        self.remove2.setObjectName("remove2")
        self.horizontalLayout_12.addWidget(self.remove2)
        self.verticalLayout_7.addLayout(self.horizontalLayout_12)
        self.verticalLayout_7.setStretch(0, 2)
        self.verticalLayout_7.setStretch(1, 1)
        self.horizontalLayout_13.addLayout(self.verticalLayout_7)
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
        self.stop.setEnabled(False)
        self.start.clicked.connect(self.play_video)
        self.stop.clicked.connect(self.stop_video)
        self.open.clicked.connect(self.open_file)
        
        self.videoslider.setRange(0,0)
        self.videoslider.sliderMoved.connect(self.set_position)
        
        self.volslider.setRange(0,100)
        self.volslider.setValue(100)
        self.volslider.sliderMoved.connect(self.set_volume)
        
        
        hboxLayout = QHBoxLayout()
        hboxLayout.setContentsMargins(0,0,0,0)
 
        #set widgets to the hbox layout
        hboxLayout.addWidget(self.open)
        hboxLayout.addWidget(self.stop)
        hboxLayout.addWidget(self.prev)
        hboxLayout.addWidget(self.start)
        hboxLayout.addWidget(self.next)
        hboxLayout.addWidget(self.sound)
        hboxLayout.addWidget(self.volslider)
        hboxLayout.addWidget(self.fsbtn)
        vboxlayout =QVBoxLayout()
        vboxlayout.addWidget(videowidget)
        vboxlayout.addWidget(self.videoslider)
        vboxlayout.addLayout(hboxLayout)
        self.tab2.setLayout(vboxlayout)
        
        self.mediaPlayer.setVideoOutput(videowidget)
        
        self.mediaPlayer.stateChanged.connect(self.mediastate_changed)
        self.mediaPlayer.positionChanged.connect(self.position_changed)
        self.mediaPlayer.durationChanged.connect(self.duration_changed)
 
        self.timer = QTimer()
        self.timer1 = QTimer()
        # set timer timeout callback function
        self.timer.timeout.connect(self.viewCam)
        self.timer1.timeout.connect(self.viewCam1)
        # set control_bt callback clicked  function
        self.startbtn1.clicked.connect(self.startTimer1)
        self.stopbtn1.clicked.connect(self.stopTimer1)
        
        self.startbtn2.clicked.connect(self.startTimer2)
        self.stopbtn2.clicked.connect(self.stopTimer2)
        
        self.fsbtn.clicked.connect(self.fullscreen)
        
        self.next.clicked.connect(self.fast)
        self.prev.clicked.connect(self.slow)
        
        self.drlb1.mousePressEvent = self.mouseEventCAM1
        self.drlb2.mousePressEvent = self.mouseEventCAM2


        self.draw1.clicked.connect(self.startDrawAreaCAM1)
        self.remove1.clicked.connect(self.removeAreaCAM1)

        self.draw2.clicked.connect(self.startDrawAreaCAM2)
        self.remove2.clicked.connect(self.removeAreaCAM2)


        self.today = date.today()
        self.now = 0
        self.now1 = 0
        self.dir = os.path.join('IVA','IVA_IPCAM_1',str(self.today.year))
        self.dir1 = os.path.join('IVA','IVA_IPCAM_2',str(self.today.year))
        self.startt = 0
        self.stopt = 0
        self.path = 0
        self.name = 0
        self.startt1 = 0
        self.stopt1 = 0
        self.path1 = 0
        self.name1 = 0 
        self.points_1=[]
        self.points_2=[]

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(self.tab2, "Open Video")
 
        if filename != '':
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(filename)))
            self.start.setEnabled(True)
            self.stop.setEnabled(True)
 
 
    def play_video(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
 
        else:
            self.mediaPlayer.play()
    def stop_video(self):
        self.mediaPlayer.stop()
 
 
 
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
        
    def set_volume(self, volume):
        self.mediaPlayer.setVolume(volume)
    def fullscreen(self):
        if MainWindow.windowState() & Qt.WindowFullScreen:
            MainWindow.showNormal()
            self.fsbtn.setText('Full Screen')
        else:
            MainWindow.showFullScreen()
            self.fsbtn.setText('Normal Screen')


    def fast(self):
        self.mediaPlayer.setPosition(self.mediaPlayer.position() + 10*60)
     
    def slow(self):
        self.mediaPlayer.setPosition(self.mediaPlayer.position() - 10*60)
    
    
    def viewCam(self):
        # read image in BGR format
        ret, image = self.cap.read()
        
        self.out.write(image)
        # convert image to RGB format
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        self.drlb1.setPixmap(QPixmap.fromImage(self.image_to_QImage(self.drawArea(image, self.points_1, self.labelip1), self.drlb1)))
        # show image in img_label
        # get image infos
        height, width, channel = image.shape
        step = channel * width
        # create QImage from image
        qImg = QImage(image.data, width, height, step, QImage.Format_RGB888)
        self.drlb1.setPixmap(QPixmap.fromImage(self.image_to_QImage(self.drawArea(image, self.points_1, self.labelip1), self.drlb1)))
        # show image in img_label
        self.labelip1.setPixmap(QPixmap.fromImage(qImg))
    def viewCam1(self):
        # read image in BGR format
        ret1, image1 = self.cap1.read()
        
        self.out1.write(image1)
        # convert image to RGB format
        image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)
        
        # get image infos
        height1, width1, channel1 = image1.shape
        step1 = channel1 * width1
        # create QImage from image
        qImg1 = QImage(image1.data, width1, height1, step1, QImage.Format_RGB888)
        self.drlb2.setPixmap(QPixmap.fromImage(self.image_to_QImage(self.drawArea(image1, self.points_2, self.labelip2), self.drlb2)))
        # show image in img_label
        self.labelip2.setPixmap(QPixmap.fromImage(qImg1))
    # start/stop timer
    def startTimer1(self):
        # if timer is stopped
        if not self.timer.isActive():
            # create video capture
            self.cap = cv2.VideoCapture(0)
            width = int(self.cap.get(3))
            height = int(self.cap.get(4))
            
            self.out = cv2.VideoWriter('outpy1.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (width,height))
            # start timer
            self.timer.start(20)
            self.now = datetime.now()
            self.startt = str(self.now.hour)+'.'+str(self.now.minute)
    def startTimer2(self):
        # if timer is stopped
        if not self.timer1.isActive():
            # create video capture
            self.cap1 = cv2.VideoCapture(iplink)
            width1 = int(self.cap1.get(3))
            height1 = int(self.cap1.get(4))
            
            self.out1 = cv2.VideoWriter('outpy2.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (width1,height1))
            # start timer
            self.timer1.start(20)
            self.now1 = datetime.now()
            self.startt1 = str(self.now1.hour)+'.'+str(self.now1.minute)       
            
        
    def stopTimer1(self):
        if self.timer.isActive():
            # stop timer
            self.timer.stop()
            # release video capture
            self.cap.release()
            self.out.release()
            self.stopt =str(self.now.hour)+'.'+str(self.now.minute)
            self.name = str(self.startt)+"-"+str(self.stopt)+".avi"
            if not os.path.exists(self.dir):
                os.mkdir(self.dir)
            self.dir = os.path.join(self.dir,str(self.today.month))
            if not os.path.exists(self.dir):
                os.mkdir(self.dir)
            self.path = os.path.join(str(self.dir),str(self.name))
            os.rename('outpy1.avi',self.path)
    def stopTimer2(self):
        if self.timer1.isActive():
            # stop timer
            self.timer1.stop()
            # release video capture
            self.cap1.release()
            self.out1.release()
            self.stopt1 =str(self.now1.hour)+'.'+str(self.now1.minute)
            self.name1 = str(self.startt1)+"-"+str(self.stopt1)+".avi"
            if not os.path.exists(self.dir1):
                os.mkdir(self.dir1)
            self.dir1 = os.path.join(self.dir1,str(self.today1.month))
            if not os.path.exists(self.dir1):
                os.mkdir(self.dir1)
            self.path1 = os.path.join(str(self.dir1),str(self.name1))
            os.rename('outpy2.avi',self.path1)
    def image_to_QImage(self, image, label):
    # image = cv2.resize(image, (label.width(), label.height()))
        height , width, channel = image.shape
        step = channel * width
        return QImage(image.data, width, height, step, QImage.Format_RGB888)
    def mouseEventCAM1(self, event):
        if self.remove1.isEnabled() and self.timer.isActive()==True and self.cap.isOpened() == True:
            x = event.pos().x()
            y = event.pos().y()
            self.points_1.append([x, y])
            print("Position clicked is ({}, {})".format(x, y))
    def mouseEventCAM2(self, event):
        if self.remove2.isEnabled() and self.timer1.isActive == True and self.cap1.isOpened() == True:
            x = event.pos().x()
            y = event.pos().y()
            self.points_2.append([x, y])
            print("Position clicked is ({}, {})".format(x, y))
    def startDrawAreaCAM1(self):
      self.draw1.setEnabled(False)
      self.remove1.setEnabled(True)

    def removeAreaCAM1(self):
      while len(self.points_1):
        self.points_1.pop()
      self.draw1.setEnabled(True)
      self.remove1.setEnabled(False)
    
    def startDrawAreaCAM2(self):
      self.draw2.setEnabled(False)
      self.remove2.setEnabled(True)
    
    def removeAreaCAM2(self):
      while len(self.points_2):
        self.points_CAM2.pop()
      self.draw2.setEnabled(True)
      self.remove2.setEnabled(False)
    def drawArea(self, image, points: list, qlabel: QtWidgets.QLabel):
      image_draw = image.copy()
      image_draw = cv2.resize(image_draw, (qlabel.width(), qlabel.height()))
      # print(len(points))
      if len(points) > 1:
        cv2.polylines(image_draw, np.array([points]), 1, (255, 0, 0), 1)
        b, g, r = cv2.split(image_draw)
        cv2.fillPoly(b, np.array([points]), (0, 255, 0))
        cv2.fillPoly(r, np.array([points]), (0, 255, 0))
        image_draw = cv2.merge([b, g, r])
      return image_draw
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "IVA Application"))
        self.labelip1.setText(_translate("MainWindow", "IP Cam 1"))
        self.startbtn1.setText(_translate("MainWindow", "Start"))
        self.prbtn1.setText(_translate("MainWindow", "Person ReID"))
        self.frbtn1.setText(_translate("MainWindow", "Face Recognition"))
        self.stopbtn1.setText(_translate("MainWindow", "Stop"))
        self.apbtn1.setText(_translate("MainWindow", "Area Protection"))
        self.fdbtn1.setText(_translate("MainWindow", "Fall Detection"))
        self.labelip2.setText(_translate("MainWindow", "IP Cam 2"))
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
        self.drlb1.setText(_translate("MainWindow", "Draw IP Cam 1"))
        self.draw1.setText(_translate("MainWindow", "Draw Area"))
        self.remove1.setText(_translate("MainWindow", "Remove Area "))
        self.drlb2.setText(_translate("MainWindow", "Draw IP Cam 2"))
        self.draw2.setText(_translate("MainWindow", "Draw Area"))
        self.remove2.setText(_translate("MainWindow", "Remove Area"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab3), _translate("MainWindow", "SETTINGS"))

import icons_rc

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

