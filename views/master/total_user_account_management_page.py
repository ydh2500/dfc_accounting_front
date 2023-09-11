from PyQt5.QtWidgets import QVBoxLayout, QLabel

from views.common.base_page import BasePage


class TotalUserAccountManagementPage(BasePage):
    def __init__(self):
        super().__init__("전체 사용자 계정 관리")

        # 이 페이지에만 필요한 추가 구성 요소
        layout = QVBoxLayout()
        test_label = QLabel("TotalUserAccountManagementPage")
        layout.addWidget(test_label)