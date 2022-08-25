import sys
from PySide6 import QtCore
from PySide6 import QtWidgets


class LoginForm(QtWidgets.QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.username_input = QtWidgets.QLineEdit()
        self.password_input = QtWidgets.QLineEdit()
        self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login_button = QtWidgets.QPushButton()
        self.login_button.setText('Login')
        self.register_button = QtWidgets.QPushButton()
        self.register_button.setText('Dont have an accout? Sign up')

        layout = QtWidgets.QFormLayout()
        layout.addRow('Username', self.username_input)
        layout.addRow('Password', self.password_input)
        layout.addRow('', self.login_button)
        layout.addRow('', self.register_button)
        self.setLayout(layout)


class RegisterForm(QtWidgets.QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.name_input = QtWidgets.QLineEdit()
        self.email_input = QtWidgets.QLineEdit()
        self.username_input = QtWidgets.QLineEdit()
        self.password_input = QtWidgets.QLineEdit()
        self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.register_button = QtWidgets.QPushButton()
        self.register_button.setText('Register')
        self.login_button = QtWidgets.QPushButton()
        self.login_button.setText('Already have an account? Sign in')

        layout = QtWidgets.QFormLayout()
        layout.addRow('Full name', self.name_input)
        layout.addRow('Email', self.email_input)
        layout.addRow('Username', self.username_input)
        layout.addRow('Password', self.password_input)
        layout.addRow('', self.register_button)
        layout.addRow('', self.login_button)
        self.setLayout(layout)


class MainWindow(QtWidgets.QWidget):
    def __init__(self) -> None:
        super().__init__()
        welcome_label = QtWidgets.QLabel()
        welcome_label.setAlignment(QtCore.Qt.AlignCenter)
        welcome_label.setText('Welcome')

        self.logout_button = QtWidgets.QPushButton()
        self.logout_button.setText('Logout')

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(welcome_label)
        layout.addWidget(self.logout_button)
        self.setLayout(layout)


class App(QtWidgets.QApplication):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.main_window = MainWindow()
        self.login_form = LoginForm()
        self.register_form = RegisterForm()

        self.container = QtWidgets.QStackedWidget()
        self.container.addWidget(self.main_window)
        self.container.addWidget(self.login_form)
        self.container.addWidget(self.register_form)
        self.container.setCurrentWidget(self.login_form)
        self.container.show()

        self.button_open_register.clicked.connect(self.show_register_form)
        self.button_open_login.clicked.connect(self.show_login_form)
        self.login_button.clicked.connect(self.show_main_window)
        self.register_button.clicked.connect(self.show_main_window)
        self.logout_button.clicked.connect(self.show_login_form)


    @property
    def button_open_register(self) -> QtWidgets.QPushButton:
        return self.login_form.register_button

    @property
    def button_open_login(self) -> QtWidgets.QPushButton:
        return self.register_form.login_button
    
    @property
    def login_button(self) -> QtWidgets.QPushButton:
        return self.login_form.login_button

    @property
    def register_button(self) -> QtWidgets.QPushButton:
        return self.register_form.register_button

    @property
    def logout_button(self) -> QtWidgets.QPushButton:
        return self.main_window.logout_button


    def show_login_form(self) -> None:
        self.container.setCurrentWidget(self.login_form)

    def show_register_form(self) -> None:
        self.container.setCurrentWidget(self.register_form)

    def show_main_window(self) -> None:
        self.container.setCurrentWidget(self.main_window)


def main() -> None:
    app = App(sys.argv)
    sys.exit(app.exec())


if __name__ == '__main__':
    main()

