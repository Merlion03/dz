import form_order
from PyQt6.QtWidgets import (
    QMainWindow,
    QWidget,
    QLabel,
    QPushButton,
    QGridLayout,
    QGroupBox
)


class Gui(QMainWindow):
    def __init__(self, sql, login):
        super().__init__()
        self.setCentralWidget(QWidget())
        self.sql = sql
        self.login = login

        self.main_layout = QGridLayout()
        self.centralWidget().setLayout(self.main_layout)

        self.groupbox_menu = QGroupBox("Личный кабинет")
        self.groupbox_btn = QGroupBox()
        self.main_layout.addWidget(self.groupbox_menu, 0, 0)
        self.main_layout.addWidget(self.groupbox_btn, 1, 0)

        self.grid_menu = QGridLayout()
        self.grid_btn = QGridLayout()
        self.groupbox_btn.setLayout(self.grid_btn)
        self.groupbox_menu.setLayout(self.grid_menu)
        self.btn_form = QPushButton('Сформировать заказ')
        self.btn_form.clicked.connect(self.press_btn_formed)
        self.grid_btn.addWidget(self.btn_form, 0, 0)
        self.create_widgets()
        self.widgets = []
        self.w = None
        self.setGeometry(500, 350, 300, 200)

    def create_widgets(self):
        text_for_labels = ['Ваш логин:', self.login]
        position_for_labels = [(0, i) for i in range(len(text_for_labels))]
        for label, posl in zip(text_for_labels, position_for_labels):
            l = QLabel(label)
            self.grid_menu.addWidget(l, *posl)

    def press_btn_formed(self):
        self.w = form_order.Gui(self.sql, self)
        self.hide()
        self.w.show()
