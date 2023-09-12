from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QDialogButtonBox, QDialog, QVBoxLayout, QLineEdit, QLabel, QCheckBox

from services.api_client import APIClient
from services.token_manager import TokenManager


class LoginWindow(QDialog):
    authenticated = pyqtSignal(str)
    def __init__(self, api_client: APIClient, token_manager: TokenManager):
        super().__init__()

        self.api_client = api_client
        self.token_manager = token_manager

        layout = QVBoxLayout()

        self.username = QLineEdit(self)
        self.password = QLineEdit(self)
        self.password.setEchoMode(QLineEdit.Password)

        self.auto_login = QCheckBox("자동 로그인")
        self.auto_login.setChecked(True)

        layout.addWidget(QLabel("Username:"))
        layout.addWidget(self.username)

        layout.addWidget(QLabel("Password:"))
        layout.addWidget(self.password)

        layout.addWidget(self.auto_login)

        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)
        button_box.accepted.connect(self.check_credentials)
        button_box.rejected.connect(self.reject)

        layout.addWidget(button_box)

        self.setLayout(layout)

        #if self.api_client.token:
        #    is_valid_token = self.api_client.check_token_validity(self.api_client.token)
        #    if is_valid_token:
        #        self.on_login_success(self.api_client.token)

    def check_credentials(self):
        username = self.username.text()
        password = self.password.text()

        # APIClient를 사용하여 실제 로그인 로직 구현
        # 예: result = self.api_client.login(username, password)
        result = self.api_client.login(username, password)  # 가정: login 메서드가 서버로 로그인 요청을 하고 토큰을 반환

        if result and 'token' in result:
            token = result['token']
            self.on_login_success(token)
            # self.api_client.set_token(token)
            # self.token_manager.save_token(token)
            # self.authenticated.emit(token)  # 인증 성공 시그널을 토큰과 함께 발생
            # self.accept()
        else:
            self.username.setText("")
            self.password.setText("")


    def on_login_success(self, token):
        self.api_client.set_token(token)
        self.token_manager.save_token(token)
        self.authenticated.emit(token)  # 인증 성공 시그널을 토큰과 함께 발생
        self.accept()

    def exec_(self):
        return QDialog.Accepted
