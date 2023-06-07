import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtWebEngineWidgets import *

class MainWindow(QMainWindow):
   def __init__(self):
       super(MainWindow, self).__init__()
       self.browser= QWebEngineView()
       self.browser.setUrl(QUrl('https://google.com'))
       self.setCentralWidget(self.browser)
       self.showMaximized()

       navbar = QToolBar()
       self.addToolBar(navbar)

       back_btn = QAction(QIcon('back.png'), 'Back to viraj', self)
       back_btn.triggered.connect(self.browser.back)
       navbar.addAction(back_btn)

       forward_btn = QAction(QIcon('for.png'), 'Forward to viraj', self)
       forward_btn.triggered.connect(self.browser.forward)
       navbar.addAction(forward_btn)

       reload_btn = QAction(QIcon('reload.png'), 'Reload', self)
       reload_btn.triggered.connect(self.browser.reload)
       navbar.addAction(reload_btn)

       forward_btn = QAction(QIcon('path/to/viraj_icon.png'), 'Created by @viraj dilshan yaad8creat', self)
       forward_btn.triggered.connect(self.browser.forward)
       navbar.addAction(forward_btn)


app = QApplication(sys.argv)
QApplication.setApplicationName('VIRAJ cool browser')
window = MainWindow()
app.exec_()
