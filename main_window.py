from PyQt5.QtWidgets import (QWidget, QApplication, QPushButton, QLabel, QLineEdit)
from PyQt5.QtGui import QPixmap
from database.birthday_database import BirthdayDatabase
from datetime import datetime


# РАЗРОБОТАТЬ НОРМАЛЬНУЮ back_btn
# СОЗДАТЬ МЕТОДЫ ДЛЯ СКРЫТИЯ ВСЕХ ОКОН (main_window, *crud)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Birthday calendar")
        self.setFixedSize(500, 500)

        self.background_image = QPixmap("images/background_2.png")
        self.db = BirthdayDatabase()

        self.buttons_stylesheet = """
            QPushButton {
                background-color: transparent;
                font-family: 'Lastri';
                font-size: 20px
            }

            QPushButton:hover {
                color: rgb(9, 211, 237);
                font-weight: 700;
            }
            """
        self.buttons_width = 170
        self.buttons_height = 25
        self.buttons_margin = 25

        self.lines_edit_stylesheet = """
            QLineEdit { 
                background-color: transparent;
                font-family: 'Lastri';
                font-size: 20px;
                width: 150px;
                border: 1px solid transparent;
                border-bottom: 2px solid black;
            }
            """
        self.lines_edit_margin = 30

        self.labels_stylesheet = """
            QLabel { 
                font-family: 'Lastri';
                font-size: 20px;
            }
            """
        self.labels_margin = self.lines_edit_margin

        self.background_label = QLabel(self)
        self.title_label = QLabel(self)
        self.action_label = QLabel(self)

        self.add_birthday_btn = QPushButton(self)
        self.get_birthdays_btn = QPushButton(self)
        self.get_birthday_btn = QPushButton(self)
        self.edit_birthday_btn = QPushButton(self)
        self.delete_birthday_btn = QPushButton(self)

        self.main_lbls = [self.title_label, self.action_label]

        self.main_btns = {self.add_birthday_btn: ["Add birthday", self.add_birthday_btn_clicked],
                          self.get_birthday_btn: ["Get birthday", self.get_birthday_btn_clicked],
                          self.get_birthdays_btn: ["Get all birthdays", self.get_birthdays_btn_clicked],
                          self.edit_birthday_btn: ["Edit birthday", self.edit_birthday_btn_clicked],
                          self.delete_birthday_btn: ["Remove birthday", self.delete_birthday_btn_clicked]}

        self.main_labels()
        self.main_buttons()
        self.show()

    def main_labels(self):
        self.title_label.setText("HAPPY BIRTHDAY!")
        self.title_label.move(120, 50)
        self.title_label.setStyleSheet("font-family: 'Lastri'; font-size: 30px;")

        self.action_label.setText("Choose the action!")
        self.action_label.move(110, 130)
        self.action_label.setStyleSheet("font-family: 'Lastri'; font-size: 25px")

        self.background_label.setPixmap(self.background_image)

    def main_buttons(self):
        x = 165
        y = 190

        self.set_buttons_settings(self.main_btns)

        for button in self.main_btns.keys():
            button.move(x, y)
            y += self.buttons_margin

    def set_buttons_settings(self, current_buttons):
        for button in current_buttons.keys():
            button.setStyleSheet(self.buttons_stylesheet)
            button.clicked.connect(current_buttons[button][1])
            button.setText(current_buttons[button][0])
            button.resize(self.buttons_width, self.buttons_height)

    def set_labels_settings(self, current_labels):
        for label in current_labels.keys():
            label.setStyleSheet(self.labels_stylesheet)
            label.setText(current_labels[label])

    def add_birthday_btn_clicked(self):

        def submit_btn_clicked():
            try:
                if len(date_le.text()) == 0 or len(last_name_le.text()) == 0 or len(first_name_le.text()) == 0:
                    raise ValueError

                date = datetime.strptime(date_le.text(), "%d.%m.%Y")
                self.db.add(first_name_le.text(), last_name_le.text(), date)
            except ValueError:
                print("ValueError")
                self.hide_widgets(*inner_btns.keys(), *inner_lse.keys(), *inner_lbls.keys())

                warning_lbl = QLabel(self)
                warning_lbl.setStyleSheet(self.labels_stylesheet)
                warning_lbl.setText("You entered too big\nfirst name or last name,\nor date format was incorrect")
                warning_lbl.move(110, 200)
                warning_lbl.show()

        def buttons():
            self.set_buttons_settings(inner_btns)
            self.show_widgets(*inner_btns.keys())
            submit_btn.move(165, 300)

        def labels():
            x = 100
            y = 160

            self.set_labels_settings(inner_lbls)

            for label in inner_lbls:
                label.move(x, y)
                y += self.labels_margin

            self.show_widgets(*inner_lbls)

        def lines_edit():
            x = 240
            y = 159

            for line in inner_lse.keys():
                line.setStyleSheet(self.lines_edit_stylesheet)
                line.setPlaceholderText(inner_lse[line])
                line.move(x, y)
                y += self.lines_edit_margin

            self.show_widgets(*inner_lse)

        self.hide_widgets(*self.main_btns.keys(), *self.main_lbls)

        submit_btn = QPushButton(self)

        first_name_lbl = QLabel(self)
        last_name_lbl = QLabel(self)
        date_lbl = QLabel(self)

        first_name_le = QLineEdit(self)
        last_name_le = QLineEdit(self)
        date_le = QLineEdit(self)

        inner_btns = {submit_btn: ["Submit", submit_btn_clicked]}
        inner_lbls = {first_name_lbl: "First name", last_name_lbl: "Last name", date_lbl: "Date"}
        inner_lse = {first_name_le: "Vladimir", last_name_le: "Putin", date_le: "07.10.1952"}

        buttons()
        labels()
        lines_edit()

    def get_birthday_btn_clicked(self):
        pass

    def get_birthdays_btn_clicked(self):
        pass

    def edit_birthday_btn_clicked(self):
        pass

    def delete_birthday_btn_clicked(self):
        pass

    @staticmethod
    def hide_widgets(*widgets):
        for widget in widgets:
            widget.hide()

    @staticmethod
    def show_widgets(*widgets):
        for widget in widgets:
            widget.show()


if __name__ == "__main__":
    app = QApplication([])
    main_window = MainWindow()
    app.exec_()
