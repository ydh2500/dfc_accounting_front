'''
api/api_client.py 에서는 API 서버에 요청을 보내는 코드를 작성합니다.
API는 다음과 같은 URL을 사용합니다.
1. api/accounts/
    1) api/accounts/bank_accounts/
    2) api/accounts/bank_account_details/
    3) api/accounts/account_types/
2. api/regions/
    1) api/regions/regions/
3. api/reports/
    1) api/reports/reports/
    2) api/reports/report_details/
4. api/transactions/
    1) api/transactions/transactions/
    2) api/transactions/transaction_types/
5. api/users/
    1) api/users/users/
    2) api/users/roles/

함수의 명칭의 규칙과 이에대한 설명은 다음과 같습니다.
1. get_모델명s(): 모델의 리스트를 가져옵니다.
2. get_모델명_details(): 모델의 상세 정보를 가져옵니다.
3. create_모델명(data): 모델을 생성합니다. data는 모델의 필드에 대한 정보를 담고 있습니다.
4. update_모델명(data): 모델을 수정합니다. data는 모델의 필드에 대한 정보를 담고 있습니다.
5. delete_모델명(data): 모델을 삭제합니다. data는 모델의 필드에 대한 정보를 담고 있습니다.

'''

import requests
from requests.exceptions import RequestException


class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.token = None  # 초기에는 토큰이 없음

    def set_token(self, token):
        self.token = token  # 로그인 성공 후 토큰 설정

    def login(self, username, password):
        login_url = f"{self.base_url}/api/users/login/"  # 로그인 API 엔드포인트에 맞게 변경해주세요.
        payload = {
            "username": username,
            "password": password
        }

        headers = {'Content-Type': 'application/json'}

        response = requests.post(login_url, json=payload, headers=headers)

        if response.status_code == 200:  # HTTP 상태 코드가 200 (성공)인 경우
            data = response.json()
            return data  # 예를 들어, {'token': 'your_token_here'}를 반환
        else:
            return None

    def logout(self):
        logout_url = f"{self.base_url}/api/users/logout/"  # 실제 로그아웃 엔드포인트 URL에 맞게 수정하세요
        headers = {'Authorization': f'Token {self.token}'} if self.token else {}
        response = requests.post(logout_url, headers=headers)

        if response.status_code == 200:  # 성공적으로 로그아웃이 이루어졌을 경우
            self.token = None  # 클라이언트 측에서 토큰 제거
            return True
        else:
            # 로그아웃 실패에 대한 처리
            return False

    def check_token_validity(self, token):
        check_token_url = f"{self.base_url}/api/users/check_token_validity/"
        response = requests.get(check_token_url, headers={'Authorization': f'Token {token}'})

        if response.status_code == 200:
            return True  # Token is valid
        elif response.status_code == 401:
            return False  # Token is invalid or not provided
        else:
            # Handle other possible HTTP status codes and exceptions
            return False


    def _make_request(self, method, endpoint, params=None, json=None):
        url = f"{self.base_url}/{endpoint}"
        headers = {}

        if self.token:
            headers['Authorization'] = f'Token {self.token}'  # 토큰이 있을 경우 헤더에 추가

        try:
            response = requests.request(method, url, params=params, json=json, headers=headers)
            response.raise_for_status()
            return response.json()
        except RequestException as e:
            print(f"An error occurred while making the request: {e}")
            return None

    # Account related methods
    def get_bank_accounts(self):
        return self._make_request("GET", "api/accounts/bank_accounts/")

    def get_account_types(self):
        return self._make_request("GET", "api/accounts/account_types/")

    # Region related methods
    def get_regions(self):
        return self._make_request("GET", "api/regions/regions/")

    # Report related methods
    def get_reports(self):
        return self._make_request("GET", "api/reports/reports/")

    # Transaction related methods
    def get_transactions(self):
        return self._make_request("GET", "api/transactions/transactions/")

    def get_transaction_types(self):
        return self._make_request("GET", "api/transactions/transaction_types/")

    # User related methods
    def get_users(self):
        return self._make_request("GET", "api/users/users/")

    def get_roles(self):
        return self._make_request("GET", "api/users/roles/")


if __name__ == "__main__":
    client = APIClient("http://127.0.0.1:8000")
    print(client.get_bank_accounts())