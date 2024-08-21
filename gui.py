import sys
import os
import time

from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QListWidgetItem
from PyQt5.QtGui import QColor, QPixmap, QIcon
from PyQt5.QtCore import Qt, QThread, pyqtSignal, pyqtSlot
from PyQt5 import uic

import models


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
COLORS = {
    "none": "#FFFFFF",
    "undefined": "#FFFFAA",
    "real": "#99FFAA",
    "fake": "#FFAA99",
}
MODELS = [
    "resnet18",
    "resnet50",
    "efficientnet_b0"
]
FORM = {
    "main": uic.loadUiType(BASE_DIR + "/UI/Main.ui")[0]
}


class Progressor(QThread):
    signal_update = pyqtSignal(int)

    def __init__(self, parent=None):
        super().__init__()
        self.main = parent

        self.value = 0
        self.value_target = 0
        self.value_max = 1
        self.value_velocity = 4

        self.main.signal_ready.connect(self.ready)
        self.main.signal_set.connect(self.setTarget)
    
    def run(self):
        while self.value <= 1000:
            time.sleep(0.01)
            self.value += (self.value_target - self.value)/self.value_velocity
            self.signal_update.emit(round(self.value / self.value_max * 1000))
    
    @pyqtSlot(int)
    def ready(self, value):
        self.value = 0
        self.value_target = 0
        self.value_max = max(value, 1)
        self.signal_update.emit(0)
    
    @pyqtSlot(int)
    def setTarget(self, value):
        self.value_target = value


class Predictor(QThread):
    signal_y = pyqtSignal(int, int)
    signal_done = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__()
        self.main = parent
        
        self.main.signal_x.connect(self.load)
        self.model = 0
        self.images = list()
    
    def run(self):
        for index, image in enumerate(self.images):
            if(self.main.listImage.item(index).checkState() or self.main.cbxAllImageValidate.checkState()):
                result = -4
                try:
                    print("Validate Image:", image)
                    result = models.model[MODELS[self.model]].predict(image)
                except Exception as e:
                    print(e)
                    result = -1
                finally:
                    self.signal_y.emit(index, result)
            time.sleep(0.01)
        self.signal_done.emit()
    
    @pyqtSlot(int, list)
    def load(self, model, images):
        self.model = model
        self.images.clear()
        self.images.extend(images)


class MainWindow(QMainWindow, FORM["main"]):
    signal_x = pyqtSignal(int, list)
    signal_ready = pyqtSignal(int)
    signal_set = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.images = list()

        self.validation = False
        
        self.label_text_image = self.labelImage.text()
        self.label_text_imageName = self.labelImageName.text()

        self.predictor = Predictor(parent=self)
        self.predictor.signal_y.connect(self.update)
        self.predictor.signal_done.connect(self.done)

        self.progressor = Progressor(parent=self)
        self.progressor.signal_update.connect(self.updateProgress)
        
        self.ready()
        self.show()
        
    def ready(self):
        self.setWindowIcon(QIcon(BASE_DIR + "/icon.png"))

        self.btnLoad.clicked.connect(self.load)
        self.btnRemove.clicked.connect(self.remove)
        self.btnValidate.clicked.connect(self.validate)
        
        self.listImage.itemClicked.connect(self.showImage)
        
        self.cbxModel.clear()
        for model in MODELS:
            self.cbxModel.addItem(model)
    
    def validator(self, enabled):
        self.btnValidate.setEnabled(not enabled)
        self.btnLoad.setEnabled(not enabled)
        self.btnRemove.setEnabled(not enabled)
        self.listImage.setEnabled(not enabled)
        self.cbxAllImageValidate.setEnabled(not enabled)
        self.cbxModel.setEnabled(not enabled)

        if(not enabled):
            self.predictor.wait()
        else:
            self.predictor.start()
            self.progressor.start()
    
    def validate(self):
        if(self.validation):
            self.validation = False
        else:
            for index in range(len(self.images)):
                self.listImage.item(index).setBackground(QColor(COLORS["none"]))

            self.pgbProgress.setMinimum(0)
            self.pgbProgress.setMaximum(0)
            self.pgbProgress.setValue(0)
            self.signal_ready.emit(len(self.images))

            self.signal_x.emit(self.cbxModel.currentIndex(), self.images)
            self.validation = True
        self.validator(self.validation)
    
    @pyqtSlot(int, int)
    def update(self, index, result):
        self.listImage.setCurrentRow(index)
        self.showImage()

        color = COLORS["none"]
        if(result >= 0):
            if(result == 0):
                color = COLORS["real"]
            else:
                color = COLORS["fake"]
        elif(result == -1):
            color = COLORS["undefined"]
        else:
            color = COLORS["none"]
        
        self.listImage.currentItem().setBackground(QColor(color))
        self.signal_set.emit(index + 1)

    @pyqtSlot(int)
    def updateProgress(self, value):
        if(self.pgbProgress.maximum() != 1000):
            self.pgbProgress.setMaximum(1000)
        
        self.pgbProgress.setValue(value)
    
    @pyqtSlot()
    def done(self):
        self.validation = False
        self.validator(self.validation)
    
    def load(self):
        try:
            ilist = QFileDialog.getOpenFileNames(self, '이미지 선택', 'C:', '이미지 파일(*.png *.jpeg *.jpg)')
            for i in ilist[0]:
                self.images.append(i)
        except Exception as e:
                print(e)
        finally:
            self.images.sort()
            self.refresh()
    
    def showImage(self):
        index = self.listImage.currentRow()
        if(index == -1):
            self.labelImage.clear()
            self.labelImage.setText(self.label_text_image)
            self.labelImageName.setText(self.label_text_imageName)
        else:
            if(index < len(self.images)):
                image = self.images[index]
                pixmap = QPixmap(image).scaled(self.labelImage.width(), self.labelImage.height(), Qt.KeepAspectRatio)
                
                self.labelImage.setText("")
                self.labelImage.setPixmap(pixmap)
                self.labelImageName.setText(os.path.basename(image))

    def refresh(self):
        index = self.listImage.currentRow()
        self.listImage.clear()
        for image in self.images:
            item = QListWidgetItem()
            item.setText(os.path.basename(image))
            item.setCheckState(2)
            self.listImage.addItem(item)
        self.listImage.setCurrentRow(index)
    
    def remove(self):
        if(len(self.images) > 0):
            index = self.listImage.currentRow()
            self.images.pop(index)
            self.listImage.takeItem(index)
            self.showImage()
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    app.exec_()