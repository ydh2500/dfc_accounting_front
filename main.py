from PyQt5.QtWidgets import QApplication
# from region.view import RegionView
import sys

from common.views.main_window import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    # region_view = RegionView()
    # region_view.show()

    sys.exit(app.exec_())
