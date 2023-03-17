import traceback
from PyQt6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QGridLayout,
    QLineEdit,
    QMessageBox,
    QHeaderView,
    QTableWidget,
    QTableWidgetItem,
)


class FirstWindow(QWidget):
    def __init__(self, for_which_button, sql):
        super().__init__()
        self.sql = sql
        self.setGeometry(500, 350, 300, 200)
        self.layout = QGridLayout()
        self.widgets = []
        match for_which_button:
            case "check":
                self.create_tree()
            case "add":
                self.create_widgets(1)
            case "remove":
                self.create_widgets(2)
        self.setLayout(self.layout)

    def create_widgets(self, var):
        if var == 1:
            text_for_labels = ['Логин (Уникальное имя)', 'ФИО', 'Телефон', 'E-Mail']
            text_for_buttons = ['OK', 'CANCEL']
            position_for_line_edit = [(i, 0) for i in range(len(text_for_labels))]
            position_for_labels = [(i, 1) for i in range(len(text_for_labels))]
            position_for_buttons = [(4, i) for i in range(2)]
            foo = self.press_btn_add
        if var == 2:
            text_for_labels = ['Удалить клиента']
            text_for_buttons = ['OK', 'CANCEL']
            position_for_line_edit = [(i, 0) for i in range(len(text_for_labels))]
            position_for_labels = [(i, 1) for i in range(len(text_for_labels))]
            position_for_buttons = [(3, i) for i in range(len(text_for_buttons))]
            foo = self.press_brn_delete
        try:
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
        except:
            traceback.print_exc()

    def create_tree(self):
        result = self.sql.check_table()
        print(result)
        table = QTableWidget()
        table.setColumnCount(5)
        table.setRowCount(len(result))
        table.setHorizontalHeaderLabels(['ID', 'ФИО', 'Телефон', 'E-Mail', 'Уникальное имя'])
        table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        table.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        for i in range(len(result)):
            table.setItem(i, 0, QTableWidgetItem(str(result[i]["id_customers"])))
            table.setItem(i, 1, QTableWidgetItem(str(result[i]["customer_fio"])))
            table.setItem(i, 2, QTableWidgetItem(str(result[i]["customer_telephone"])))
            table.setItem(i, 3, QTableWidgetItem(str(result[i]["customer_email"])))
            table.setItem(i, 4, QTableWidgetItem(str(result[i]["customer_login"])))
        self.layout.addWidget(table)

    def press_btn_add(self, name):
        try:
            if name == "OK":
                login = self.widgets[0].text()
                FIO = self.widgets[1].text()
                email = self.widgets[2].text()
                telephone = self.widgets[3].text()
                if self.sql.add(login, email, telephone, FIO):
                    QMessageBox.information(self, 'Success', 'User successfully added')
                    for widget in self.widgets:
                        print(self.widgets)
                        widget.setText('')
                        self.hide()
                else:
                    QMessageBox.critical(self, 'Error', 'The user has not been added')
            else:
                self.hide()
        except:
            traceback.print_exc()

    def press_brn_delete(self, name):
        if name == "OK":
            login = self.widgets[0].text()
            if self.sql.delete(login):
                QMessageBox.information(self, 'Success', 'User successfully delete')
                for widget in self.widgets:
                    widget.setText('')
            else:
                QMessageBox.critical(self, 'Error', 'The user has not been deleted')
        else:
            self.hide()
