from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton


class LeftMenuWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        self.bankAccountButton = QPushButton("Bank Account")
        self.userButton = QPushButton("User")
        self.regionButton = QPushButton("Region")

        layout.addWidget(self.bankAccountButton)
        layout.addWidget(self.userButton)
        layout.addWidget(self.regionButton)
        layout.addStretch(1)

        self.setLayout(layout)