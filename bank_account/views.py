from PyQt5.QtWidgets import QVBoxLayout, QLabel

from common.views.base_page import BasePage


class BankAccountPage(BasePage):
    def __init__(self):
        super().__init__("계좌 관리")

        # BankAccountPage에만 필요한 추가 구성 요소 layout에 추가
        layout = QVBoxLayout()
        test_label = QLabel("BankAccountPage")
        layout.addWidget(test_label)

        self.add_scroll_layout(layout)