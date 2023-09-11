from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QTreeWidget, QTreeWidgetItem, QWidget, QVBoxLayout

class LeftMenuWidget(QWidget):
    menuClicked = pyqtSignal(str)
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        # Create Tree Widget
        self.tree = QTreeWidget()
        self.tree.setHeaderHidden(True)
        self.tree.setColumnCount(1)

        # StyleSheet for Tree Widget
        qss = """
        QTreeView {
            background-color: #ffffff;
            alternate-background-color: #eeeeee;
            border: 1px solid #dddddd;
        }

        QTreeView::item {
            border: 1px solid #dddddd;
        }

        QTreeView::item:selected {
            background-color: #bbbbbb;
        }
        """

        self.tree.setStyleSheet(qss)


        # Add root items (큰 메뉴)
        self.add_root_item("입출금 등록")
        self.add_root_item("재정 보고서", ["월별 재정보고서", "연도별 대차대조표"])
        self.add_root_item("내역 보고서", ["총 계정원장", "현금 출납부", "통장 거래내역서", "계정과목별 원장"])
        self.add_root_item("설정", ["계좌 관리", "지구 관리", "멤버 관리"])
        self.add_root_item("마스터", ["계정과목 관리", "거래유형 관리", "사용자 계정 관리", "지구 관리", "현황 관리"])

        layout.addWidget(self.tree)
        self.setLayout(layout)

    def add_root_item(self, name, children=[]):
        root_item = QTreeWidgetItem(self.tree)
        root_item.setText(0, name)
        for child_name in children:
            child_item = QTreeWidgetItem()
            child_item.setText(0, child_name)
            root_item.addChild(child_item)

        # Connect the signals here to handle click events
        self.tree.itemClicked.connect(self.on_item_clicked)

    def on_item_clicked(self, item, column):
        self.menuClicked.emit(item.text(column))