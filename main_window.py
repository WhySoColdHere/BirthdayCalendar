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
        self.buttons_width = 220
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
        self.labels_margin = self.lines_edit_margin + 1

        self.background_label = QLabel(self)
        self.background_label.setPixmap(self.background_image)

        self.main_lbls = {
            QLabel(self): ["HAPPY BIRTHDAY!", "font-family: 'Lastri'; font-size: 30px;", (120, 50)],
            QLabel(self): ["Choose the action!", "font-family: 'Lastri'; font-size: 25px", (110, 130)]
        }

        self.main_btns = {
            QPushButton(self): ["Add birthday", self.add_birthday_btn_clicked],
            QPushButton(self): ["Get birthday", self.get_birthday_btn_clicked],
            QPushButton(self): ["Get all birthdays", self.get_birthdays_btn_clicked],
            QPushButton(self): ["Edit birthday", self.edit_birthday_btn_clicked],
            QPushButton(self): ["Remove birthday", self.delete_birthday_btn_clicked]
        }

        self.add_birthday_lbls = {
            QLabel(self): "First name",
            QLabel(self): "Last name",
            QLabel(self): "Date"
        }

        self.add_birthday_btns = {
            QPushButton(self): ["Submit", self.add_birthday_submit_btn_clicked],
        }

        self.add_birthday_lines_ed = {
            QLineEdit(self): "Vladimir",
            QLineEdit(self): "Putin",
            QLineEdit(self): "07.10.1952"
        }

        self.back_btn = QPushButton(self)

        self.hide_widgets(
            self.back_btn,
            *self.main_btns,
            *self.main_lbls,
            *self.add_birthday_lbls.keys(),
            *self.add_birthday_btns.keys(),
            *self.add_birthday_lines_ed.keys()
        )

        self.main_window_gui_show()
        self.show()

    def main_window_gui_show(self):
        def main_labels():
            for label in self.main_lbls:
                label.setText(self.main_lbls[label][0])
                label.setStyleSheet(self.main_lbls[label][1])
                label.move(self.main_lbls[label][2][0], self.main_lbls[label][2][1])

        def main_buttons():
            x = 140
            y = 190

            self.set_buttons_settings(self.main_btns)

            for button in self.main_btns.keys():
                button.move(x, y)
                y += self.buttons_margin

        main_labels()
        main_buttons()

        self.show_widgets(
            *self.main_lbls.keys(),
            *self.main_btns.keys(),
        )

    def main_window_gui_hide(self):
        self.hide_widgets(
            *self.main_lbls.keys(),
            *self.main_btns.keys()
        )

    def add_birthday_gui_show(self):
        def labels():
            x = 100
            y = 160

            self.set_labels_settings(self.add_birthday_lbls)
            for label in self.add_birthday_lbls.keys():
                label.move(x, y)
                y += self.labels_margin

        def buttons():
            x = 135
            y = 300

            self.set_buttons_settings(self.add_birthday_btns)
            for button in self.add_birthday_btns.keys():
                button.move(x, y)
                y += self.buttons_margin

        def lines_edit():
            x = 240
            y = 160  # 159

            self.set_lines_edit_settings(self.add_birthday_lines_ed)
            for line_edit in self.add_birthday_lines_ed.keys():
                line_edit.move(x, y)
                y += self.lines_edit_margin

        labels()
        buttons()
        lines_edit()

        self.back_button(self.back_btn, self.add_birthday_gui_hide, self.main_window_gui_show)

        self.show_widgets(
            *self.add_birthday_lbls.keys(),
            *self.add_birthday_btns.keys(),
            *self.add_birthday_lines_ed.keys()
        )

    def add_birthday_gui_hide(self):
        self.hide_widgets(
            *self.add_birthday_lines_ed.keys(),
            *self.add_birthday_btns.keys(),
            *self.add_birthday_lbls.keys()
        )

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

    def set_lines_edit_settings(self, current_lines_edit):
        for line_edit in current_lines_edit.keys():
            line_edit.setStyleSheet(self.lines_edit_stylesheet)
            line_edit.setPlaceholderText(current_lines_edit[line_edit])

    def back_button(self, back_btn, *args):
        x = 200
        y = 50

        back_btns = {self.back_btn: ["Back", lambda: self.back_btn_clicked(back_btn, args)]}
        self.set_buttons_settings(back_btns)
        self.back_btn.move(x, y)
        self.back_btn.show()

    @staticmethod
    def back_btn_clicked(back_btn, args):
        for func in args:
            func()
        back_btn.hide()

    def add_birthday_submit_btn_clicked(self):
        pass
        # self.add_birthday_gui_hide()
        #
        # try:
        #     lines_edit = []
        #     for line_edit in zip(self.add_birthday_lines_ed, range(len(self.add_birthday_lines_ed))):
        #         if len(line_edit[0].text()) == 0:
        #             raise ValueError
        #
        #         if line_edit[1] == len(self.add_birthday_lines_ed) - 1:
        #             lines_edit.append(datetime.strptime(line_edit[0].text(), "%d.%m.%Y"))
        #         else:
        #             lines_edit.append(line_edit[0].text())
        #
        #     self.db.add(lines_edit[0], lines_edit[1], lines_edit[2])
        # except ValueError:
        #     self.back_btn.hide()
        #
        #     warning_lbl = QLabel(self)
        #     warning_lbl.setStyleSheet(self.labels_stylesheet)
        #     warning_lbl.setText("You entered too big\nfirst name or last name,\nor date format was incorrect")
        #     warning_lbl.move(110, 200)
        #     warning_lbl.show()
        #
        #
        #
        #     self.back_button(self.back_btn, lambda: warning_lbl.hide())

    def add_birthday_btn_clicked(self):
        self.main_window_gui_hide()
        self.add_birthday_gui_show()

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
