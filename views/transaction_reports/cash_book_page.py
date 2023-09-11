
from PyQt5.QtWidgets import QVBoxLayout, QLabel

from views.common.base_page import BasePage


class CashBookPage(BasePage):
    def __init__(self):
        super().__init__("현금 출납부")

        # 이 페이지에만 필요한 추가 구성 요소
        layout = QVBoxLayout()
        test_label = QLabel("CashBookPage")
        layout.addWidget(test_label)