from typing import List

from qgis.PyQt.QtCore import (QRunnable, QObject, pyqtSignal, pyqtSlot, QThread)


class WaitWorker(QRunnable):

    def __init__(self, percent: int):

        super(WaitWorker, self).__init__()

        self.signals = WorkerSignals()

        self.percent = percent

    @pyqtSlot()
    def run(self):

        QThread.msleep(200)

        self.signals.percent.emit(self.percent)


class WorkerSignals(QObject):
    result = pyqtSignal()
    percent = pyqtSignal(int)
