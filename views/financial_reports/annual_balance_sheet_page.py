from PyQt5.QtWidgets import QVBoxLayout, QLabel

from views.common.base_page import BasePage


class AnnualBalanceSheetPage(BasePage):
    def __init__(self):
        super().__init__("연도별 대차 대조표")

        # 이 페이지에만 필요한 추가 구성 요소
        layout = QVBoxLayout()
        test_label = QLabel("AnnualBalanceSheetPage")
        layout.addWidget(test_label)
