from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog


class AboutDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 窗体
        self.setWindowTitle("关于")
        self.setWindowIcon(QIcon('Assets/main.png'))
        self.resize(300, 200)
