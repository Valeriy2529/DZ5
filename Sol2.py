# Код позволяет пользователю выбрать блюдо из списка и отображает информацию о выбранном блюде.

# Импортируемые библиотеки
import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QListWidget, QListWidgetItem, QMessageBox
from PyQt6.QtGui import QIcon, QColor

# Класс FoodApp наследуется от класса QWidget и представляет собой основное окно приложения.
class FoodApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Приложение с едой")  # Заголовок приложения
        self.setFixedSize(250, 230)  # Размеры и положение окна
        self.setWindowIcon(QIcon("../Images/cooking.png"))  # Иконка приложения
        # Установка цвета фона
        self.setStyleSheet("background-color:#fffafa;")  # Цвет фона

        # Создание вертикального layout
        self.layout = QVBoxLayout()

        self.label_welcome = QLabel("МЕНЮ (￣﹃￣)")
        self.label_welcome.setStyleSheet("font: bold; font-size: 16pt")
        self.label_welcome.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_welcome.setFixedSize(250, 35)

        # Заголовок
        self.label_title = QLabel("Выберите блюдо:")
        self.label_title.setStyleSheet("font-size: 12px; color: black;")  # Установка цвета и размера шрифта

        # Список блюд
        self.food_list = QListWidget()

        # Добавляем блюда в список
        dishes = [
            "Утка по-пекински",
            "Методовая свинина чар сиу",
            "Жаренный рис с яйцом",
            "Говядина с овощами",
            "Легкий китайский салат"
        ]

        for dish in dishes:
            item = QListWidgetItem(dish)
            item.setBackground(QColor(95, 158, 160))  # Цвет фона элемента
            self.food_list.addItem(item)

        self.layout.addWidget(self.label_welcome)
        self.layout.addWidget(self.label_title)
        self.layout.addWidget(self.food_list)

        # Подключаем метод при выборе блюда
        self.food_list.itemClicked.connect(self.show_food_info)

        self.setLayout(self.layout)
    # Метод отображает информацию о выбранном блюде при клике.
    def show_food_info(self, item):
        dish_name = item.text()
        # Здесь можно добавить логику для получения информации о блюде
        QMessageBox.information(self, "Информация о блюде", f"Вы выбрали: {dish_name}")

# Запуск приложения
if __name__ == '__main__':
    app = QApplication(sys.argv)
    food_window = FoodApp()
    food_window.show()
    sys.exit(app.exec())
