'''
작성자 : 윤두현
작성일 : 23.09.12.

본 파일은 user app의 controllers.py 파일입니다.

이 파일에서는 user app에서 사용되는 컨트롤러를 정의합니다.
컨트롤러의 역할은 api_client.py을 통해 데이터베이스에 접근하여 데이터를 가져오거나,
데이터베이스에 데이터를 저장하는 것입니다.

'''

# api_client.py 파일을 import 합니다.

# user app의 모델을 import 합니다.
from models import User, Role

