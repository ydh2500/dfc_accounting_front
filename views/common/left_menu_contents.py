from views.reports.annual_balance_sheet_page import AnnualBalanceSheetPage
from views.reports.monthly_financial_report_page import MonthlyFinancialReportPage
from views.bank_accounts.account_type_management_page import AccountTypeManagementPage
from views.reports.financial_report_status_management_page import FinancialReportStatusManagementPage
from views.regions.total_region_management_page import TotalRegionManagementPage
from views.transactions.transaction_type_management_page import TransactionTypeManagementPage
from views.bank_accounts.bank_account_management_page import BankAccountManagementPage
from views.users.total_user_management_page import TotalUserManagementPage
from views.users.member_management_page import MemberManagementPage
from views.regions.region_management_page import RegionManagementPage
from views.transactions.transaction_registration_page import TransactionRegistrationPage
from views.transactions.account_ledger_page import GeneralLedgerPage
from views.transactions.bank_transaction_report_page import BankTransactionReportPage
from views.transactions.cash_book_page import CashBookPage
from views.transactions.general_ledger_page import AccountLedgerPage


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
            "입출금 등록": TransactionRegistrationPage(),
            "월별 재정보고서": MonthlyFinancialReportPage(),
            "연도별 대차대조표": AnnualBalanceSheetPage(),
            "총 계정원장": GeneralLedgerPage(),
            "현금 출납부": CashBookPage(),
            "통장 거래내역서": BankTransactionReportPage(),
            "계정과목별 원장": AccountLedgerPage(),
            "계좌 관리": BankAccountManagementPage(),
            "지구 관리": RegionManagementPage(),
            "멤버 관리": MemberManagementPage(),
            "계정과목 관리": AccountTypeManagementPage(),
            "거래유형 관리": TransactionTypeManagementPage(),
            "전체 사용자 계정 관리": TotalUserManagementPage(),
            "전체 지구 관리": TotalRegionManagementPage(),
            "재정보고서 현황 관리": FinancialReportStatusManagementPage(),
            # ... (기타 페이지 매핑)
        }

    def get_contents(self):
        return self.contents

    def get_page(self, menu_name):
        return self.page_map.get(menu_name)