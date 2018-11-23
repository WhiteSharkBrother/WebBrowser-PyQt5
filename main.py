import sys

from PyQt5.QtCore import QUrl, QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QMainWindow, QToolBar, QAction, QLineEdit, QApplication


class MainWindow(QMainWindow):
    name = "基于Qt5的 Python 浏览器 "
    version = "0.9 Beta"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 窗体
        self.setWindowTitle(self.name + self.version)
        self.setWindowIcon(QIcon('Assets/main.png'))
        self.resize(1200, 800)
        # 浏览器窗体
        self.browser = QWebEngineView()
        self.browser.load(QUrl("http://www.baidu.com/"))
        self.setCentralWidget(self.browser)
        # 工具条
        navigation_bar = QToolBar('Navigation')
        navigation_bar.setIconSize(QSize(32, 32))
        self.addToolBar(navigation_bar)
        # 后退前进停止刷新主页转到按钮
        back_button = QAction(QIcon('Assets/back.png'), '后退', self)
        next_button = QAction(QIcon('Assets/forward.png'), '前进', self)
        stop_button = QAction(QIcon('Assets/stop.png'), '停止', self)
        refresh_button = QAction(QIcon('Assets/refresh.png'), '刷新', self)
        home_button = QAction(QIcon('Assets/home.png'), '主页', self)
        enter_button = QAction(QIcon('Assets/enter.png'), '转到', self)
        # 其他组件
        self.url_text_bar = QLineEdit()
        # 工具条添加组件
        navigation_bar.addAction(back_button)
        navigation_bar.addAction(next_button)
        navigation_bar.addAction(stop_button)
        navigation_bar.addAction(refresh_button)
        navigation_bar.addSeparator()
        navigation_bar.addAction(home_button)
        navigation_bar.addSeparator()
        navigation_bar.addWidget(self.url_text_bar)
        navigation_bar.addSeparator()
        navigation_bar.addAction(enter_button)
        # 事件触发
        back_button.triggered.connect(self.browser.back)
        next_button.triggered.connect(self.browser.forward)
        stop_button.triggered.connect(self.browser.stop)
        refresh_button.triggered.connect(self.browser.reload)
        home_button.triggered.connect(self.navigate_to_home)
        enter_button.triggered.connect(self.navigate_to_url)
        # 触发映射
        self.url_text_bar.returnPressed.connect(self.navigate_to_url)
        self.browser.urlChanged.connect(self.renew_urlbar)
        self.browser.titleChanged.connect(self.renew_title)
        self.browser.iconChanged.connect(self.renew_icon)

    def navigate_to_url(self):
        s = QUrl(self.url_text_bar.text())
        if s.scheme() == '':
            s.setScheme('http')
        self.browser.load(s)

    def navigate_to_home(self):
        s = QUrl("https://www.baidu.com/")
        self.browser.load(s)

    def renew_urlbar(self, s):
        self.url_text_bar.setText(s.toString())
        self.url_text_bar.setCursorPosition(0)

    def renew_title(self, s):
        self.setWindowTitle(self.name + self.version + " -- " + s)

    def renew_icon(self, ico):
        self.setWindowIcon(ico)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())
