# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainrlAhhQ.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QCheckBox,
    QFrame, QLabel, QListView, QListWidget,
    QListWidgetItem, QMainWindow, QProgressBar, QPushButton,
    QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(800, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(800, 600))
        MainWindow.setMaximumSize(QSize(1920, 1080))
        font = QFont()
        font.setFamilies([u"NanumMyeongjo"])
        font.setPointSize(10)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u"../../../../Downloads/outline_camera_front_white_48dp.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.labelImage = QLabel(self.centralwidget)
        self.labelImage.setObjectName(u"labelImage")
        self.labelImage.setGeometry(QRect(10, 10, 551, 551))
        self.labelImage.setFont(font)
        self.labelImage.setStyleSheet(u"background-color:rgb(255, 255, 255);")
        self.labelImage.setScaledContents(False)
        self.labelImage.setAlignment(Qt.AlignCenter)
        self.btnValidate = QPushButton(self.centralwidget)
        self.btnValidate.setObjectName(u"btnValidate")
        self.btnValidate.setGeometry(QRect(580, 520, 211, 31))
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(560, 10, 21, 581))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.listImage = QListWidget(self.centralwidget)
        self.listImage.setObjectName(u"listImage")
        self.listImage.setGeometry(QRect(580, 40, 211, 291))
        font1 = QFont()
        font1.setFamilies([u"NanumMyeongjo"])
        font1.setPointSize(12)
        self.listImage.setFont(font1)
        self.listImage.setAutoFillBackground(False)
        self.listImage.setFrameShape(QFrame.StyledPanel)
        self.listImage.setFrameShadow(QFrame.Sunken)
        self.listImage.setLineWidth(1)
        self.listImage.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.listImage.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.listImage.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.listImage.setAutoScroll(True)
        self.listImage.setEditTriggers(QAbstractItemView.DoubleClicked|QAbstractItemView.EditKeyPressed)
        self.listImage.setTabKeyNavigation(True)
        self.listImage.setProperty("showDropIndicator", False)
        self.listImage.setDragEnabled(False)
        self.listImage.setAlternatingRowColors(True)
        self.listImage.setSelectionMode(QAbstractItemView.SingleSelection)
        self.listImage.setMovement(QListView.Static)
        self.listImage.setFlow(QListView.TopToBottom)
        self.listImage.setProperty("isWrapping", False)
        self.listImage.setResizeMode(QListView.Fixed)
        self.listImage.setLayoutMode(QListView.SinglePass)
        self.listImage.setSpacing(4)
        self.listImage.setViewMode(QListView.ListMode)
        self.listImage.setUniformItemSizes(False)
        self.listImage.setSelectionRectVisible(True)
        self.listImage.setSortingEnabled(False)
        self.pgbProgress = QProgressBar(self.centralwidget)
        self.pgbProgress.setObjectName(u"pgbProgress")
        self.pgbProgress.setGeometry(QRect(580, 560, 211, 31))
        self.pgbProgress.setValue(0)
        self.pgbProgress.setTextVisible(False)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(580, 10, 211, 21))
        self.label_2.setAlignment(Qt.AlignCenter)
        self.btnRemove = QPushButton(self.centralwidget)
        self.btnRemove.setObjectName(u"btnRemove")
        self.btnRemove.setGeometry(QRect(580, 340, 101, 31))
        self.btnLoad = QPushButton(self.centralwidget)
        self.btnLoad.setObjectName(u"btnLoad")
        self.btnLoad.setGeometry(QRect(690, 340, 101, 31))
        self.labelImageName = QLabel(self.centralwidget)
        self.labelImageName.setObjectName(u"labelImageName")
        self.labelImageName.setGeometry(QRect(10, 570, 551, 21))
        self.labelImageName.setScaledContents(True)
        self.labelImageName.setAlignment(Qt.AlignCenter)
        self.cbxAllImageValidate = QCheckBox(self.centralwidget)
        self.cbxAllImageValidate.setObjectName(u"cbxAllImageValidate")
        self.cbxAllImageValidate.setGeometry(QRect(580, 390, 211, 21))
        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(570, 371, 221, 20))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.listImage, self.btnRemove)
        QWidget.setTabOrder(self.btnRemove, self.btnLoad)
        QWidget.setTabOrder(self.btnLoad, self.cbxAllImageValidate)
        QWidget.setTabOrder(self.cbxAllImageValidate, self.btnValidate)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Deep Fake Discriminator", None))
        self.labelImage.setText(QCoreApplication.translate("MainWindow", u"\uc774\ubbf8\uc9c0\ub97c \uc120\ud0dd\ud558\uba74 \uc774\uacf3\uc5d0 \ub098\ud0c0\ub0a9\ub2c8\ub2e4", None))
        self.btnValidate.setText(QCoreApplication.translate("MainWindow", u"\uac80\uc99d", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\ud30c\uc77c \ubaa9\ub85d", None))
        self.btnRemove.setText(QCoreApplication.translate("MainWindow", u"\uc81c\uac70", None))
        self.btnLoad.setText(QCoreApplication.translate("MainWindow", u"\ubd88\ub7ec\uc624\uae30", None))
        self.labelImageName.setText("")
        self.cbxAllImageValidate.setText(QCoreApplication.translate("MainWindow", u"\ubaa8\ub4e0 \uc774\ubbf8\uc9c0 \uac80\uc99d", None))
    # retranslateUi

