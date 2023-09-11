from PyQt5.QtWidgets import QVBoxLayout, QLabel

from views.common.base_page import BasePage


class BankAccountManagementPage(BasePage):
    def __init__(self):
        super().__init__("계좌 관리")

        # 이 페이지에만 필요한 추가 구성 요소
        layout = QVBoxLayout()
        test_label = QLabel("BankAccountManagementPage")
        layout.addWidget(test_label)

        self.add_scroll_layout(layout)