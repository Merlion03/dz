from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QMainWindow,
    QWidget,
    QLabel,
    QPushButton,
    QGridLayout,
    QLineEdit,
    QMessageBox,
    QGroupBox,
)

import widgets_for_admin


class Gui(QMainWindow):
    def __init__(self, sql, parent):
        super().__init__()
        self.setCentralWidget(QWidget())
        self.setGeometry(500, 350, 300, 200)
        self.sql = sql

        self.main_layout = QGridLayout()
        self.centralWidget().setLayout(self.main_layout)

        self.groupbox_menu = QGroupBox("Формирование заказа")
        self.groupbox_btn = QGroupBox()
        self.main_layout.addWidget(self.groupbox_menu, 0, 0)
        self.main_layout.addWidget(self.groupbox_btn, 1, 0)

        self.grid_menu = QGridLayout()
        self.grid_btn = QGridLayout()
        self.groupbox_btn.setLayout(self.grid_btn)
        self.groupbox_menu.setLayout(self.grid_menu)
        self.btn_form = QPushButton('Формировать заказ')
        self.btn_form.clicked.connect(self.press_btn_formed)
        self.btn_cansel = QPushButton('Отменить')
        self.btn_cansel.clicked.connect(self.press_btn_cansel)
        self.btn_names = QPushButton('Посмотреть ФИО всех клиентов в базе данных')
        self.btn_names.clicked.connect(self.check_sql)
        self.grid_btn.addWidget(self.btn_form, 0, 0)
        self.grid_btn.addWidget(self.btn_names, 1, 0)
        self.grid_btn.addWidget(self.btn_cansel, 2, 0)
        self.line_edit_price = None
        self.line_edit_uq_name = None
        self.create_widgets()
        self.w = parent

    def create_widgets(self):
        self.login = QLabel('Уникальное имя заказчика:')
        self.price = QLabel('Цена:')
        self.services = QLabel('Дополнительные услуги:')
        self.line_edit_uq_name = QLineEdit()
        self.line_edit_price = QLineEdit()
        self.grid_menu.addWidget(self.login, 0, 0)
        self.grid_menu.addWidget(self.price, 1, 0)
        self.grid_menu.addWidget(self.services, 2, 0)
        self.grid_menu.addWidget(self.line_edit_uq_name, 0, 1)
        self.grid_menu.addWidget(self.line_edit_price, 1, 1)

    def press_btn_formed(self, ):
        login = self.line_edit_uq_name.text()
        price = self.line_edit_price.text()
        if not self.sql.form_order(login, price):
            self.w = widgets_for_admin.FirstWindow("add", self.sql)
            self.w.setWindowModality(Qt.WindowModality.ApplicationModal)
            self.w.show()
        else:
            QMessageBox.information(self, 'Success', 'Заказ сформирован')

    def press_btn_cansel(self, name):
        self.w.show()
        self.hide()

    def check_sql(self):
        self.w = widgets_for_admin.FirstWindow("check", self.sql)
        self.w.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.w.show()
