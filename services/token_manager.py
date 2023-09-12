from PyQt5.QtCore import QSettings

from services.api_client import APIClient


class TokenManager:
    def __init__(self, api_client: APIClient):
        self.api_client = api_client
        self.settings = QSettings("DFC", "DFCAccountingSystem")
        auth_token = self.settings.value("auth_token", type=str)

        if auth_token:
            self.api_client.set_token(auth_token)

    def save_token(self, token):
        self.settings.setValue("auth_token", token)

    def load_token(self):
        return self.settings.value("auth_token", type=str)

    def delete_token(self):
        self.settings.remove("auth_token")