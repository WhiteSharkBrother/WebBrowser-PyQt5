import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import *


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('基于Qt5的 Python 浏览器 Version 0.9')
        self.setWindowIcon(QIcon('Assets/main.png'))
        self.resize(1200, 800)

        self.browser = QWebEngineView()
        url = 'http://www.hao123.com'
        self.browser.setUrl(QUrl(url))
        self.setCentralWidget(self.browser)

        navigation_bar = QToolBar('Navigation')
        navigation_bar.setIconSize(QSize(32, 32))
        self.addToolBar(navigation_bar)

        back_button = QAction(QIcon('Assets/back.png'), '后退', self)
        back_button.triggered.connect(self.browser.back)
        navigation_bar.addAction(back_button)

        next_button = QAction(QIcon('Assets/forward.png'), '前进', self)
        next_button.triggered.connect(self.browser.forward)
        navigation_bar.addAction(next_button)

        stop_button = QAction(QIcon('Assets/stop.png'), '停止', self)
        stop_button.triggered.connect(self.browser.stop)
        navigation_bar.addAction(stop_button)

        refresh_button = QAction(QIcon('Assets/refresh.png'), '刷新', self)
        refresh_button.triggered.connect(self.browser.reload)
        navigation_bar.addAction(refresh_button)

        self.url_text_bar = QLineEdit()
        self.url_text_bar.returnPressed.connect(self.navigate_to_url)
        navigation_bar.addSeparator()
        navigation_bar.addWidget(self.url_text_bar)
        self.browser.urlChanged.connect(self.renew_urlbar)

    def navigate_to_url(self):
        s = QUrl(self.url_text_bar.text())
        if s.scheme() == '':
            s.setScheme('http')
        self.browser.setUrl(s)

    def renew_urlbar(self, s):
        self.url_text_bar.setText(s.toString())
        self.url_text_bar.setCursorPosition(0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())
