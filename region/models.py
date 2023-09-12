'''
작성자 : 윤두현
작성일 : 23.09.12.

본 파일은 region app의 models.py 파일입니다.

이 파일에서는 region app에서 사용되는 모델을 정의합니다.

1. Region
    1) name
    2) description

'''

# pydantic 라이브러리를 사용하여 모델을 정의합니다.
from pydantic import BaseModel

class Region(BaseModel):
    name: str
    description: str = None