from PyQt5.QtWidgets import QWidget, QVBoxLayout, QStackedWidget, QHBoxLayout

from bank_account.views import BankAccountPage
from common.views.header_widget import HeaderWidget
from common.views.left_menu_widget import LeftMenuWidget
from user.views import UserPage


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("DFC Accounting")

        layout = QVBoxLayout()

        # Top Layout
        top_layout = QVBoxLayout()
        self.header = HeaderWidget()
        top_layout.addWidget(self.header)
        layout.addLayout(top_layout)

        # Bottom Layout
        bottomLayout = QHBoxLayout()
        # Bottom Left Menu
        self.leftMenu = LeftMenuWidget()
        bottomLayout.addWidget(self.leftMenu)
        # Bottom Right Content
        self.contentArea = QStackedWidget()
        bottomLayout.addWidget(self.contentArea)

        # 페이지 선언
        self.userPage = UserPage()
        self.bankAccountPage = BankAccountPage()

        # 페이지 이동 시그널 연결
        self.leftMenu.userButton.clicked.connect(lambda: self.change_content(0))
        self.leftMenu.bankAccountButton.clicked.connect(lambda: self.change_content(1))


        # 페이지 contentArea에 추가
        self.contentArea.addWidget(self.userPage)
        self.contentArea.addWidget(self.bankAccountPage)

        # Layout
        layout.addLayout(bottomLayout)
        self.setLayout(layout)

    def change_content(self, index):
        self.contentArea.setCurrentIndex(index)

