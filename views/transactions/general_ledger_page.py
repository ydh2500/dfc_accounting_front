from PyQt5.QtWidgets import QVBoxLayout, QLabel

from views.common.base_page import BasePage


class AccountLedgerPage(BasePage):
    def __init__(self):
        super().__init__("계정과목별 원장")

        # 이 페이지에만 필요한 추가 구성 요소
        layout = QVBoxLayout()
        test_label = QLabel("AccountLedgerPage")
        layout.addWidget(test_label)