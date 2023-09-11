from views.common.base_page import BasePage


class TotalUserAccountManagementPage(BasePage):
    def __init__(self):
        super().__init__("User")

        # UserPage에만 필요한 추가 구성 요소
        # 예: self.layout().addWidget(some_widget)