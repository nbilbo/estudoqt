import sys

from PySide6 import QtCore
from PySide6 import QtGui
from PySide6 import QtWidgets


class LoginForm(QtWidgets.QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.username_input = QtWidgets.QLineEdit()
        self.password_input = QtWidgets.QLineEdit()
        self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)

        self.login_button = QtWidgets.QPushButton('Login')
        self.cancel_button = QtWidgets.QPushButton('Cancel')
        buttons = QtWidgets.QWidget()
        buttons.setLayout(QtWidgets.QHBoxLayout())
        buttons.layout().addWidget(self.login_button)
        buttons.layout().addWidget(self.cancel_button)

        layout = QtWidgets.QFormLayout()
        layout.addRow('Username', self.username_input)
        layout.addRow('Password', self.password_input)
        layout.addRow('', buttons)
        self.setLayout(layout)


class MainWindow(QtWidgets.QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.login_form = LoginForm()
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.login_form)
        self.login_button.clicked.connect(self.authenticate)
        self.cancel_button.clicked.connect(self.cancel)

    def cancel(self) -> None:
        print('Good bye.')
        self.close()

    def authenticate(self) -> None:
        username = self.username_input.text()
        password = self.password_input.text()

        if username == 'admin' and password == 'admin':
            self.success_message('Success', 'You are logged in.')
        else:
            self.failed_message('Failed', 'You are not logged in.')

    def success_message(self, title: str, message: str) -> None:
        QtWidgets.QMessageBox.information(self, title, message)

    def failed_message(self, title: str, message: str) -> None:
        QtWidgets.QMessageBox.critical(self, title, message)

    @property
    def username_input(self) -> QtWidgets.QLineEdit:
        return self.login_form.username_input

    @property
    def password_input(self) -> QtWidgets.QLineEdit:
        return self.login_form.password_input

    @property
    def cancel_button(self) -> QtWidgets.QPushButton:
        return self.login_form.cancel_button

    @property
    def login_button(self) -> QtWidgets.QPushButton:
        return self.login_form.login_button


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
