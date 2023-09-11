from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton


class HeaderWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QHBoxLayout()

        self.titleLabel = QLabel("DFC Accounting")
        self.titleLabel.setAlignment(Qt.AlignCenter)

        self.logoutButton = QPushButton("Logout")

        layout.addWidget(self.titleLabel)
        layout.addStretch(1)
        layout.addWidget(self.logoutButton)

        self.setLayout(layout)
