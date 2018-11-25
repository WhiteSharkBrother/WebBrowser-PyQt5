from PyQt5.QtCore import QUrl, QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QMainWindow, QToolBar, QAction, QLineEdit, QProgressBar


class BrowserWindow(QMainWindow):
    name = "PyBrowser Powered by Y.Wang"
    version = "1.0.20181125"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 窗体
        self.setWindowTitle(self.name)
        self.setWindowIcon(QIcon('Assets/main.png'))
        self.resize(1200, 800)
        # 浏览器窗体
        self.browser = QWebEngineView()
        self.browser.load(QUrl("http://www.baidu.com/"))
        self.setCentralWidget(self.browser)
        # 工具条
        self.navigation_bar = QToolBar('Navigation')
        self.navigation_bar.setIconSize(QSize(32, 32))
        self.navigation_bar.setMovable(False)
        self.addToolBar(self.navigation_bar)
        # 后退前进停止刷新按钮
        self.back_button = QAction(QIcon('Assets/back.png'), '后退', self)
        self.next_button = QAction(QIcon('Assets/forward.png'), '前进', self)
        self.stop_button = QAction(QIcon('Assets/stop.png'), '停止', self)
        self.refresh_button = QAction(QIcon('Assets/refresh.png'), '刷新', self)
        # 地址栏
        self.home_button = QAction(QIcon('Assets/home.png'), '主页', self)
        self.enter_button = QAction(QIcon('Assets/enter.png'), '转到', self)
        self.url_text_bar = QLineEdit()
        self.url_text_bar.setMinimumWidth(300)
        self.site_icon = QAction(self)
        # 进度条
        self.progress_bar = QProgressBar()
        self.progress_bar.setMaximumWidth(120)
        # 设置按钮
        self.set_button = QAction(QIcon('Assets/setting.png'), '设置', self)
        # 工具条添加组件
        self.navigation_bar.addAction(self.back_button)
        self.navigation_bar.addAction(self.next_button)
        self.navigation_bar.addAction(self.stop_button)
        self.navigation_bar.addAction(self.refresh_button)
        self.navigation_bar.addAction(self.home_button)
        self.navigation_bar.addSeparator()
        self.navigation_bar.addAction(self.site_icon)
        self.navigation_bar.addWidget(self.url_text_bar)
        self.navigation_bar.addAction(self.enter_button)
        self.navigation_bar.addSeparator()
        self.navigation_bar.addWidget(self.progress_bar)
        self.navigation_bar.addAction(self.set_button)
        # 事件触发
        self.back_button.triggered.connect(self.browser.back)
        self.next_button.triggered.connect(self.browser.forward)
        self.stop_button.triggered.connect(self.browser.stop)
        self.refresh_button.triggered.connect(self.browser.reload)
        self.home_button.triggered.connect(self.navigate_to_home)
        self.enter_button.triggered.connect(self.navigate_to_url)
        # 触发映射
        self.url_text_bar.returnPressed.connect(self.navigate_to_url)
        self.browser.urlChanged.connect(self.renew_urlbar)
        self.browser.titleChanged.connect(self.renew_title)
        self.browser.iconChanged.connect(self.renew_icon)
        self.browser.loadProgress.connect(self.renew_progress_bar)

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
        self.setWindowTitle(s + " -- " + self.name)

    def renew_icon(self, ico):
        self.site_icon.setIcon(ico)

    def renew_progress_bar(self, p):
        self.progress_bar.setValue(p)
