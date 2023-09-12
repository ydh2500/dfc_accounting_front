'''
작성자 : 윤두현
작성일 : 23.09.12.

본 파일은 user app의 models.py 파일입니다.

이 파일에서는 user app에서 사용되는 모델을 정의합니다.

1. User
    1) username
    2) password
    3) email
    4) phone
    5) created_at
    6) updated_at
    7) role
    8) region

2. Role
    1) name
    2) description
'''

# pydantic 라이브러리를 사용하여 모델을 정의합니다.

from pydantic import BaseModel


class User(BaseModel):
    username: str
    password: str
    email: str
    phone: str = None
    created_at: str = None
    updated_at: str = None
    role: int = None
    region: int = None
    
class Role(BaseModel):
    name: str
    description: str = None



