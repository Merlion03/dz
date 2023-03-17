import three_btn_for_admins
import personal_account
import sql
from PyQt6.QtWidgets import (
    QMainWindow,
    QWidget,
    QLabel,
    QPushButton,
    QGridLayout,
    QLineEdit,
    QMessageBox,
)

config = {
    "host": 'localhost',
    "user": 'root',
    "password": '1123581321',
    "database": 'db'
}


class Gui(QMainWindow):
    def __init__(self):
        super().__init__()
        self.sql = sql.MyDb(config)
        self.layout = QGridLayout()
        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)
        self.widgets = []
        self.create_widgets(1)
        self.w = None
        self.login = None
        self.setGeometry(500, 350, 300, 200)

    def create_widgets(self, var):
        if var == 1:
            text_for_labels = ['Ваш логин', 'Ваш пароль']
            text_for_buttons = ['Login']
            position_for_line_edit = [(i, 0) for i in range(len(text_for_labels))]
            position_for_labels = [(i, 1) for i in range(len(text_for_labels))]
            position_for_buttons = [(3, i) for i in range(len(text_for_buttons))]
            foo = self.press_btn_login
        if var == 2:
            text_for_labels = ['Delete User']
            text_for_buttons = ['OK', 'CANCEL']
            position_for_line_edit = [(i, 0) for i in range(len(text_for_labels))]
            position_for_labels = [(i, 1) for i in range(len(text_for_labels))]
            position_for_buttons = [(3, i) for i in range(len(text_for_buttons))]
            foo = self.press_btn_sign_up
        for label, posl in zip(text_for_labels, position_for_labels):
            l = QLabel(label)
            self.layout.addWidget(l, *posl)
        for pose in position_for_line_edit:
            le = QLineEdit()
            self.layout.addWidget(le, *pose)
            self.widgets.append(le)
        for name, posb in zip(text_for_buttons, position_for_buttons):
            b = QPushButton(name)
            b.clicked.connect(lambda ch, name=name: foo(name))
            self.layout.addWidget(b, *posb)

    def press_btn_login(self, name):
        if name == "Login":
            self.login = self.widgets[0].text()
            password = self.widgets[1].text()
            sql = self.sql.login(self.login, password)
            if isinstance(sql, tuple):
                if sql[1] == 1:
                    self.admin_panel()
                    QMessageBox.information(self, 'Success', 'You successfully join your account')
                else:
                    self.hide()
                    self.w = personal_account.Gui(self.sql, self.login)
                    self.w.show()
                    QMessageBox.information(self, 'Success', 'You successfully join your account')
            else:
                QMessageBox.critical(self, 'Error', 'Incorrect login and password')
        else:
            self.hide()

    def admin_panel(self):
        button = QMessageBox.question(self, "Question dialog", "Do you want to open the admin panel?")

        if button == QMessageBox.StandardButton.Yes:
            self.hide()
            self.w = three_btn_for_admins.Gui(self.sql)
            self.w.show()
        else:
            self.hide()
            self.w = personal_account.Gui(self.sql, self.login)
            self.w.show()
