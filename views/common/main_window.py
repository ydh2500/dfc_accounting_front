from PyQt5.QtWidgets import QWidget, QVBoxLayout, QStackedWidget, QHBoxLayout

from views.common.left_menu_contents import LeftMenuContents
from views.common.header_widget import HeaderWidget
from views.common.left_menu_widget import LeftMenuWidget


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

        self.menu_contents = LeftMenuContents()  # LeftMenuContents 인스턴스 생성
        # 페이지 초기화 및 이동 시그널 연결
        self.initialize_pages()

    def initialize_pages(self):
        self.pages = {}
        for main_menu, sub_menus in self.menu_contents.get_contents():
            main_page = self.menu_contents.get_page(main_menu)
            self.pages[main_menu] = main_page
            for sub_menu in sub_menus:
                sub_page = self.menu_contents.get_page(sub_menu)
                self.pages[sub_menu] = sub_page

        for index, page in enumerate(self.pages.values()):
            if page:  # 페이지가 None이 아닌 경우에만 추가
                self.contentArea.addWidget(page)

    def on_menu_clicked(self, menu_name):
        page = self.pages.get(menu_name)
        if page:
            index = self.contentArea.indexOf(page)
            self.contentArea.setCurrentIndex(index)