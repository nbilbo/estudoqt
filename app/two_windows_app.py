import sys
from PySide6 import QtCore
from PySide6 import QtWidgets
from PySide6 import qt_core


class App(QtWidgets.QApplication):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.main_window = MainWindow()
        self.main_window.show()


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()



if __name__ == '__main__':
    app = App(sys.argv)
    sys.exit(app.exec())
