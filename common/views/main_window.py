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
        self.header = HeaderWidget()
        layout.addWidget(self.header)

        # Bottom Layout
        bottomLayout = QHBoxLayout()
        self.leftMenu = LeftMenuWidget()
        bottomLayout.addWidget(self.leftMenu)

        self.contentArea = QStackedWidget()
        bottomLayout.addWidget(self.contentArea)

        layout.addLayout(bottomLayout)
        self.setLayout(layout)

        self.leftMenu.menuClicked.connect(self.on_menu_clicked)

        # 페이지 초기화 및 이동 시그널 연결
        self.initialize_pages()

    def initialize_pages(self):
        # 페이지 선언
        self.userPage = UserPage()
        self.bankAccountPage = BankAccountPage()

        self.pages = {
            "사용자 계정 관리": self.userPage,
            "계좌 관리": self.bankAccountPage,
            # ... 기타 페이지 ...
        }

        for index, page in enumerate(self.pages.values()):
            self.contentArea.addWidget(page)
    def create_page_changer(self, index):
        def page_changer():
            self.contentArea.setCurrentIndex(index)

        return page_changer

    def on_menu_clicked(self, menu_name):
        page = self.pages.get(menu_name)
        if page:
            index = self.contentArea.indexOf(page)
            self.contentArea.setCurrentIndex(index)