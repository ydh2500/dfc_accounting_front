from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QTreeWidget, QTreeWidgetItem, QWidget, QVBoxLayout

from views.common.left_menu_contents import LeftMenuContents


class LeftMenuWidget(QWidget):
    menuClicked = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        # Create Tree Widget
        self.tree = QTreeWidget()
        self.tree.setColumnCount(1)
        self.tree.setHeaderHidden(True)

        # Get menu contents from LeftMenuContents
        menu_contents = LeftMenuContents().get_contents()

        for main_menu, sub_menus in menu_contents:
            self.add_root_item(main_menu, sub_menus)

        layout.addWidget(self.tree)
        self.setLayout(layout)

    def add_root_item(self, name, children=[]):
        root_item = QTreeWidgetItem(self.tree)
        root_item.setText(0, name)
        for child_name in children:
            child_item = QTreeWidgetItem()
            child_item.setText(0, child_name)
            root_item.addChild(child_item)
        self.tree.itemClicked.connect(self.on_item_clicked)

    def on_item_clicked(self, item, column):
        self.menuClicked.emit(item.text(column))