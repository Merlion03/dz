import traceback

import widgets_for_admin
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QMainWindow,
    QWidget,
    QPushButton,
    QGridLayout,
)


class Gui(QMainWindow):
    def __init__(self, sql):
        super().__init__()
        self.sql = sql
        self.layout = QGridLayout()
        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)
        self.widget = []
        self.create_btn()
        self.w = None
        self.setGeometry(500, 350, 300, 200)

    def create_btn(self):
        text = ['Check user', 'Add user', 'Delete user', 'Remove Order', 'Change Order']
        foo = [self.check_sql, self.add_to_sql, self.delete_from_sql, self.check_sql, self.check_sql]
        position_for_labels = [(i, 2) for i in range(len(text))]
        try:
            for name, position, foo in zip(text, position_for_labels, foo):
                button = QPushButton(name)
                button.clicked.connect(foo)
                self.layout.addWidget(button, *position)
                self.widget.append(button)
        except:
            traceback.print_exc()

    def check_sql(self):
        self.w = widgets_for_admin.FirstWindow("check", self.sql)
        self.w.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.w.show()

    def add_to_sql(self):
        self.w = widgets_for_admin.FirstWindow("add", self.sql)
        self.w.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.w.show()

    def delete_from_sql(self):
        self.w = widgets_for_admin.FirstWindow("remove", self.sql)
        self.w.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.w.show()
