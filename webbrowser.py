import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5 import QtGui

#from PyQt5.QtWebEngineWidgets import QWebEngineView as QWebView,QWebEnginePage as QWebPage
#from PyQt5.QtWebEngineWidgets import QWebEngineSettings as QWebSettings
#from PyQt5.QWebEngineWidgets import QWebEngineView
from Browser import *
class MyBrowser(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.showMaximized()
        self.setWindowTitle("Web Player")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ui.lineEditURL.setFont(font)
        self.ui.lineEditURL.setText("http://")
        self.ui.pushButtonGo.clicked.connect(self.viewWebsite)
        self.ui.pushButtonZoomIn.clicked.connect(self.zoomIn)
        self.ui.pushButtonZoomOut.clicked.connect(self.zoomOut)
        self.ui.pushButtonBack.clicked.connect(self.goBack)
        self.ui.pushButtonForward.clicked.connect(self.goForward)
        self.ui.pushButtonReload.clicked.connect(self.reloadPage)
        self.ui.pushButtonStop.clicked.connect(self.stopPage)


    def viewWebsite(self):
        self.ui.widget.load(QUrl(self.ui.lineEditURL.text()))
        #self.ui.widget.setZoomFactor(2)

    def zoomIn(self):
        self.ui.widget.setZoomFactor(2)

    def zoomOut(self):
        self.ui.widget.setZoomFactor(1)

    def goBack(self):
        self.ui.widget.back()

    def goForward(self):
        self.ui.widget.forward()

    def reloadPage(self):
        self.ui.widget.reload()

    def stopPage(self):
        self.ui.widget.stop()

if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyBrowser()
    w.show()
    sys.exit(app.exec_())
