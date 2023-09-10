from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel


class BasePage(QWidget):
    def __init__(self, title):
        super().__init__()

        # 공통적인 크기 설정
        self.setFixedSize(500, 400)

        layout = QVBoxLayout()

        # 공통적인 구성 요소 예: 페이지 제목
        titleLabel = QLabel(title)
        layout.addWidget(titleLabel)

        self.setLayout(layout)