from PyQt5.QtWidgets import QApplication, QDialog
# from region.view import RegionView
import sys

from services.api_client import APIClient
from services.token_manager import TokenManager
from views.common.main_window import MainWindow
from views.user.login_window import LoginWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)

    BaseURL = "http://127.0.0.1:8000"
    api_client = APIClient(BaseURL)
    token_manager = TokenManager(api_client=api_client)
    main_window = MainWindow(api_client=api_client, token_manager=token_manager)
    # 1. 저장된 토큰 불러오기
    token = token_manager.load_token()
    # 2. 토큰이 유효한지 확인
    is_valid_token = api_client.check_token_validity(token)
    # 3. 유효하다면 메인 윈도우를 띄우고, 그렇지 않다면 로그인 윈도우를 띄움
    if is_valid_token:
        main_window.show()

        sys.exit(app.exec_())

    else:
        login_window = LoginWindow(api_client=api_client, token_manager=token_manager)

        def show_main_window(token):
            main_window.show()

        login_window.authenticated.connect(show_main_window)

        login_window.show()
        if login_window.exec_() == QDialog.Accepted:
            sys.exit(app.exec_())

    # login_window = LoginWindow(api_client=api_client, token_manager=token_manager)
    # main_window = MainWindow()
    #
    # def show_main_window(token):
    #     main_window.show()
    #
    # login_window.authenticated.connect(show_main_window)
    #
    # login_window.show()
    # if login_window.exec_() == QDialog.Accepted:
    #     sys.exit(app.exec_())