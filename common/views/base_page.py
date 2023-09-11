from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout, QFrame, QPushButton, QScrollArea, QSizePolicy

class BasePage(QWidget):
    def __init__(self, title):
        super().__init__()

        # 공통적인 크기 설정
        # self.setFixedSize(500, 400)
        self.setMinimumSize(500, 400)

        self.layout = QVBoxLayout()

        # 공통적인 헤더 구성
        self.headerLayout = QHBoxLayout()
        self.titleLabel = QLabel(title)
        self.headerLayout.addWidget(self.titleLabel)
        self.headerLayout.addStretch(1)
        self.layout.addLayout(self.headerLayout)

        self.header_horizontal_line = QFrame()
        self.header_horizontal_line.setFrameShape(QFrame.HLine)
        self.header_horizontal_line.setFrameShadow(QFrame.Sunken)
        self.layout.addWidget(self.header_horizontal_line)

        # 하단 구성
        self.footerLayout = QHBoxLayout()
        self.footerLayout.addStretch(1)
        self.layout.addLayout(self.footerLayout)

        # 중앙 컨텐츠 영역
        self.scroll = QScrollArea()  # 스크롤 영역
        self.scrollContent = QWidget()  # 스크롤 내부의 컨텐츠
        self.scroll.setWidget(self.scrollContent)
        self.scroll.setWidgetResizable(True)
        self.layout.addWidget(self.scroll)

        # 이 클래스가 사용하는 레이아웃 설정
        self.setLayout(self.layout)

    def add_header_button(self, button_label):
        button = QPushButton(button_label)
        self.headerLayout.addWidget(button)

    def add_footer_button(self, button_label):
        button = QPushButton(button_label)
        self.footerLayout.addWidget(button)

    def add_scroll_layout(self, layout):
        self.scrollContent.setLayout(layout)

