from views.settings.bank_account_management_page import BankAccountManagementPage
from views.master.total_user_account_management_page import TotalUserAccountManagementPage


class LeftMenuContents:
    def __init__(self):
        self.contents = [
            ("입출금 등록", []),
            ("재정 보고서", ["월별 재정보고서", "연도별 대차대조표"]),
            ("내역 보고서", ["총 계정원장", "현금 출납부", "통장 거래내역서", "계정과목별 원장"]),
            ("설정", ["계좌 관리", "지구 관리", "멤버 관리"]),
            ("마스터", ["계정과목 관리", "거래유형 관리", "전체 사용자 계정 관리", "전체 지구 관리", "재정보고서 현황 관리"]),
        ]
        self.page_map = {
            "입출금 등록": None,
            "월별 재정보고서": None,
            "연도별 대차대조표": None,
            "총 계정원장": None,
            "현금 출납부": None,
            "통장 거래내역서": None,
            "계정과목별 원장": None,
            "계좌 관리": BankAccountManagementPage(),
            "지구 관리": None,
            "멤버 관리": None,
            "계정과목 관리": None,
            "거래유형 관리": None,
            "전체 사용자 계정 관리": TotalUserAccountManagementPage(),
            "전체 지구 관리": None,
            "재정보고서 현황 관리": None,
            # ... (기타 페이지 매핑)
        }

    def get_contents(self):
        return self.contents

    def get_page(self, menu_name):
        return self.page_map.get(menu_name)