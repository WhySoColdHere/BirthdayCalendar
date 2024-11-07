from PyQt5.QtWidgets import (QWidget, QApplication, QPushButton, QLabel, QDialog)
from PyQt5.QtGui import QPixmap


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Birthday calendar")
        self.setFixedSize(500, 500)

        self.background_image = QPixmap("images/background.png")
        self.buttons_stylesheet = """
            QPushButton {
                background-color: transparent;
                font-family: 'Lastri';
                font-size: 15px
            }

            QPushButton:hover {
                color: rgb(9, 211, 237);
                font-weight: 700;
            }
            """

        self.background_label = QLabel(self)
        self.title_label = QLabel(self)
        self.action_label = QLabel(self)

        self.add_birthday_btn = QPushButton(self)
        self.get_birthdays_btn = QPushButton(self)
        self.get_birthday_btn = QPushButton(self)
        self.edit_birthday_btn = QPushButton(self)
        self.delete_birthday_btn = QPushButton(self)

        self.main_btns = {self.add_birthday_btn: ["Add birthday", self.add_birthday_btn_clicked],
                          self.get_birthday_btn: ["Get birthday", self.get_birthday_btn_clicked],
                          self.get_birthdays_btn: ["Get all birthdays", self.get_birthdays_btn_clicked],
                          self.edit_birthday_btn: ["Edit birthday", self.edit_birthday_btn_clicked],
                          self.delete_birthday_btn: ["Remove birthday", self.delete_birthday_btn_clicked]}

        self.main_labels()
        self.main_buttons()
        self.show()

    def main_buttons(self):
        x = 165
        y = 190
        width = 170
        height = 25
        buttons_margin = 25

        for button in self.main_btns.keys():
            button.setStyleSheet(self.buttons_stylesheet)

            button.clicked.connect(self.main_btns[button][1])
            button.setText(self.main_btns[button][0])
            button.resize(width, height)
            button.move(x, y)
            y += buttons_margin

    def add_birthday_btn_clicked(self):
        pass

    def get_birthday_btn_clicked(self):
        pass

    def get_birthdays_btn_clicked(self):
        pass

    def edit_birthday_btn_clicked(self):
        pass

    def delete_birthday_btn_clicked(self):
        pass

    def main_labels(self):
        self.title_label.setText("HAPPY BIRTHDAY!")
        self.title_label.move(120, 50)
        self.title_label.setStyleSheet("font-family: 'Lastri'; font-size: 30px;")

        self.action_label.setText("Choose the action!")
        self.action_label.move(140, 130)
        self.action_label.setStyleSheet("font-family: 'Lastri'; font-size: 20px")

        self.background_label.setPixmap(self.background_image)

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
