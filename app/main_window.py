import sys
from PySide6 import QtCore
from PySide6 import QtGui
from PySide6 import QtWidgets
import constants


class MenuBar(QtWidgets.QMenuBar):
    def __init__(self) -> None:
        super().__init__()
        file_menu = self.addMenu('File')

        self.open_action = file_menu.addAction('Open')

        self.save_action = file_menu.addAction('Save')

        file_menu.addSeparator()

        self.quit_action = file_menu.addAction('Quit')


class EditToolBar(QtWidgets.QToolBar):
    def __init__(self) -> None:
        super().__init__()
        
        self.copy_image = QtGui.QIcon(constants.COPY_IMAGE)
        self.copy_action = self.addAction(self.copy_image, 'copy')
        
        self.cut_image = QtGui.QIcon(constants.CUT_IMAGE)
        self.cut_action = self.addAction(self.cut_image, 'cut')
        
        self.paste_image = QtGui.QIcon(constants.PASTE_IMAGE)
        self.paste_action = self.addAction(self.paste_image, 'paste')
        
        self.undo_image = QtGui.QIcon(constants.UNDO_IMAGE)
        self.undo_action = self.addAction(self.undo_image, 'undo')
        
        self.redo_image = QtGui.QIcon(constants.REDO_IMAGE)
        self.redo_action = self.addAction(self.redo_image, 'redo')


class StatusBar(QtWidgets.QStatusBar):
    def __init__(self) -> None:
        super().__init__()


class SearchDock(QtWidgets.QDockWidget):
    def __init__(self) -> None:
        super().__init__()

        self.search_widget = SearchWidget()
        self.setWidget(self.search_widget)
    
    def searched(self) -> str:
        return self.search_widget.searched()
    
    def checked(self) -> bool:
        return self.search_widget.checked()


class SearchWidget(QtWidgets.QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.searched_input = QtWidgets.QLineEdit()

        self.case_checkbox = QtWidgets.QCheckBox('Case Sensitive?')

        self.search_image = QtGui.QIcon(constants.SEARCH_IMAGE)
        self.search_button = QtWidgets.QPushButton('Search')
        self.search_button.setIcon(self.search_image)

        layout = QtWidgets.QFormLayout()
        layout.addRow('Search', self.searched_input)
        layout.addRow(self.case_checkbox)
        layout.addRow(self.search_button)
        self.setLayout(layout)
    
    def searched(self) -> str:
        return self.searched_input.text()
    
    def checked(self) -> bool:
        return self.case_checkbox.checkState() == QtCore.Qt.Checked
        

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.menu_bar = MenuBar()
        self.menu_bar.open_action.triggered.connect(self.open_file)
        self.menu_bar.save_action.triggered.connect(self.save_file)
        self.menu_bar.quit_action.triggered.connect(self.close)
        self.setMenuBar(self.menu_bar)

        self.edit_tool_bar = EditToolBar()
        self.edit_tool_bar.copy_action.triggered.connect(self.copy_text)
        self.edit_tool_bar.paste_action.triggered.connect(self.paste_text)
        self.edit_tool_bar.cut_action.triggered.connect(self.cut_text)
        self.edit_tool_bar.undo_action.triggered.connect(self.undo_text)
        self.edit_tool_bar.redo_action.triggered.connect(self.redo_text)
        self.addToolBar(self.edit_tool_bar)

        self.status_bar = StatusBar()
        self.setStatusBar(self.status_bar)

        self.search_dock = SearchDock()
        self.search_dock.search_widget.search_button.clicked.connect(self.search)
        self.addDockWidget(QtCore.Qt.BottomDockWidgetArea, self.search_dock)

        self.text_editor = QtWidgets.QTextEdit()
        self.setCentralWidget(self.text_editor)

        self.resize(500, 500)
        self.setWindowTitle('Text Editor')
        self.show_status_message('Welcome to my text editor.', 2500)

    def open_file(self) -> None:
        filename, _ = QtWidgets.QFileDialog.getOpenFileName()
        if filename:
            with open(filename, 'r') as file:
                text = file.read()
                self.text_editor.clear()
                self.text_editor.insertPlainText(text)
                self.text_editor.moveCursor(QtGui.QTextCursor.Start)
                self.show_status_message(f'Editing {filename}', 2500) 
    
    def save_file(self) -> None:
        text = self.text_editor.toPlainText()
        filename, _ = QtWidgets.QFileDialog.getSaveFileName()
        if filename:
            with open(filename, 'w') as file:
                file.write(text)
                self.show_status_message(f'Saved to {filename}', 2500)
    
    def copy_text(self) -> None:
        self.text_editor.copy()
        self.show_status_message('copy', 1000)
    
    def paste_text(self) -> None:
        self.text_editor.paste()
        self.show_status_message('paste', 1000)
    
    def cut_text(self) -> None:
        self.text_editor.cut()
        self.show_status_message('cut', 1000)
    
    def undo_text(self) -> None:
        self.text_editor.undo()
        self.show_status_message('undo', 1000)

    def redo_text(self) -> None:
        self.text_editor.redo()
        self.show_status_message('redo', 1000)
    
    def show_status_message(self, message: str, timeout: int) -> None:
        self.status_bar.showMessage(message, timeout)
    
    def search(self) -> None:
        # not working
        searched = self.search_dock.searched()
        is_sensitive = self.search_dock.checked()
        print(f'searched: {searched}, is sensitive? {is_sensitive}')

        finded = self.text_editor.find(searched, QtGui.QTextDocument.FindBackward)
        if not finded:
            self.show_status_message('No matches found',2000)

    
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
