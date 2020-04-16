import sys
#from PyQt5.QtCore import QUrl
#from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow
#from PyQt5 import QtGui
#from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from EasyBrowser import *

class EasyBrowserApp(Ui_MainWindow, QMainWindow):
    def __init__(self, parent=None):
        super(EasyBrowserApp, self).__init__(parent)
        self.setupUi(self)
        self.showMaximized()
        self.setWindowTitle("EasyBrowser")

        #Setting the font size of the url link and prefix text
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditUrl.setFont(font)
        self.lineEditUrl.setText("http://")

        #Action Settings for Buttons
        self.pushButtonGo.clicked.connect(self.browseWeb)
        self.pushButtonReload.clicked.connect(self.reloadPage)
        self.pushButtonStop.clicked.connect(self.stopPage)
        self.pushButtonZoom.clicked.connect(self.zoomPage)
        self.pushButtonZoomOut.clicked.connect(self.zoomOutPage)
        self.pushButtonGoBack.clicked.connect(self.goBackPage)
        self.pushButtonGoForward.clicked.connect(self.goForwardPage)

        #Defining the action for Enter Key in Url field
        self.lineEditUrl.returnPressed.connect(self.browseWeb)

        #Action Settings for Menu
        self.actionGo_Back.triggered.connect(self.goBackPage)
        self.actionGo_Forward.triggered.connect(self.goForwardPage)
        self.actionZoom.triggered.connect(self.zoomPage)
        self.actionZoom_Out.triggered.connect(self.zoomOutPage)
        self.actionReload.triggered.connect(self.reloadPage)
        self.actionStop.triggered.connect(self.stopPage)

    def browseWeb(self):
        self.widgetBrowse.load(QUrl(self.lineEditUrl.text()))

    def reloadPage(self):
        self.widgetBrowse.reload()

    def stopPage(self):
        self.widgetBrowse.stop()

    def zoomPage(self):
        self.widgetBrowse.setZoomFactor(2)

    def zoomOutPage(self):
        self.widgetBrowse.setZoomFactor(1)

    def goBackPage(self):
        self.widgetBrowse.back()

    def goForwardPage(self):
        self.widgetBrowse.forward()




if __name__== '__main__':
    app = QApplication(sys.argv)
    browserApp = EasyBrowserApp()
    browserApp.show()
    sys.exit(app.exec_())


