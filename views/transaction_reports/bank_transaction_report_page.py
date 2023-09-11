from PyQt5.QtWidgets import QVBoxLayout, QLabel

from views.common.base_page import BasePage


class BankTransactionReportPage(BasePage):
    def __init__(self):
        super().__init__("통장 거래내역서")

        # 이 페이지에만 필요한 추가 구성 요소
        layout = QVBoxLayout()
        test_label = QLabel("BankTransactionReportPage")
        layout.addWidget(test_label)