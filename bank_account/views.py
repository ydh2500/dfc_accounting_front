from common.views.base_page import BasePage


class BankAccountPage(BasePage):
    def __init__(self):
        super().__init__("Bank Account")

        # BankAccountPage에만 필요한 추가 구성 요소
        # 예: self.layout().addWidget(some_widget)