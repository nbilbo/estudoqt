import sys

from PySide6 import QtCore
from PySide6 import QtGui
from PySide6 import QtWidgets


class Form(QtWidgets.QWidget):
    def __init__(self, main_window: 'MainWindow') -> None:
        super().__init__()
        self.main_window = main_window

        self.text_input = QtWidgets.QLineEdit()
        confirm_button = QtWidgets.QPushButton('confirm')
        confirm_button.clicked.connect(self.confirm)
        cancel_button = QtWidgets.QPushButton('cancel')
        cancel_button.clicked.connect(self.close)
        buttons = QtWidgets.QWidget()
        buttons.setLayout(QtWidgets.QHBoxLayout())
        buttons.layout().addWidget(confirm_button)
        buttons.layout().addWidget(cancel_button)

        layout = QtWidgets.QFormLayout()
        layout.addRow('type here', self.text_input)
        layout.addRow('', buttons)
        self.setLayout(layout)
    
    def confirm(self) -> None:
        self.main_window.set_username(self.text_input.text())
        self.close()

    def set_text(self, text: str) -> None:
        self.text_input.setText(text)


class MainWindow(QtWidgets.QWidget):
    def __init__(self) -> None:
        super().__init__()
        
        self.username_label = QtWidgets.QLabel()
        self.username_label.setText('Ola, mundo.')
        self.username_label.setAlignment(QtCore.Qt.AlignCenter)

        self.button = QtWidgets.QPushButton()
        self.button.setText('Open form')
        self.button.clicked.connect(self.open_form)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.username_label)
        layout.addWidget(self.button)
        self.setLayout(layout)
    
    def open_form(self) -> None:
        self.form = Form(self)
        self.form.set_text(self.username_label.text())
        self.form.show()
    
    def set_username(self, username: str) -> None:
        self.username_label.setText(username)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
