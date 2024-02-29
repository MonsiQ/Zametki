import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QTextEdit, QListWidget, QLabel, QMessageBox, QLineEdit
from PyQt5.QtCore import Qt


class NotesApp(QWidget):
    def __init__(self):
        super().__init__()
        self.notes = {}  # Словарь для хранения заметок
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Заметки')
        self.setGeometry(100, 100, 400, 600)
        self.setStyleSheet("background-color: #CCCCCC;")

        # Создание кнопок
        self.create_note_button = QPushButton('Создать заметку', self)
        self.view_notes_button = QPushButton('Просмотр заметок', self)

        # Настройка стилей кнопок
        self.create_note_button.setStyleSheet('QPushButton {background-color: #4CAF50; color: white; border: none; padding: 10px; font-size: 16px; border-radius: 5px;}'
                                              'QPushButton:hover {background-color: #45a049;}'
                                              'QPushButton:pressed {background-color: #388E3C;}')
        self.view_notes_button.setStyleSheet('QPushButton {background-color: #008CBA; color: white; border: none; padding: 10px; font-size: 16px; border-radius: 5px;}'
                                             'QPushButton:hover {background-color: #007B9D;}'
                                             'QPushButton:pressed {background-color: #005F79;}')

        # Настройка макета
        main_layout = QVBoxLayout(self)

        # Горизонтальный макет для кнопок
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.create_note_button)
        button_layout.addWidget(self.view_notes_button)

        # Добавление горизонтального макета в вертикальный
        main_layout.addLayout(button_layout)

        # Создание дополнительных виджетов
        self.note_title_edit = QLineEdit(self)
        self.note_content_edit = QTextEdit(self)
        self.save_note_button = QPushButton('Сохранить', self)
        self.note_list_widget = QListWidget(self)
        self.note_view_edit = QTextEdit(self)
        self.note_view_edit.setReadOnly(True)

        # Настройка стилей для дополнительных виджетов
        self.note_title_edit.setStyleSheet('QLineEdit {background-color: rgba(255, 255, 255, 200); padding: 5px; border: none; border-radius: 5px;}'
                                           'QLineEdit:hover {background-color: rgba(255, 255, 255, 220);}'
                                           'QLineEdit:focus {background-color: rgba(255, 255, 255, 220);}'
                                           'QLineEdit:disabled {background-color: rgba(255, 255, 255, 200);}'
                                           'QLineEdit::placeholder {color: rgba(255, 255, 255, 150);}')
        self.note_content_edit.setStyleSheet('QTextEdit {background-color: rgba(255, 255, 255, 200); padding: 5px; border: none; border-radius: 5px;}'
                                             'QTextEdit:hover {background-color: rgba(255, 255, 255, 220);}'
                                             'QTextEdit:focus {background-color: rgba(255, 255, 255, 220);}'
                                             'QTextEdit:disabled {background-color: rgba(255, 255, 255, 200);}')
        self.save_note_button.setStyleSheet('QPushButton {background-color: #4CAF50; color: white; border: none; padding: 8px; font-size: 14px; border-radius: 5px;}'
                                            'QPushButton:hover {background-color: #45a049;}'
                                            'QPushButton:pressed {background-color: #388E3C;}')
        self.note_list_widget.setStyleSheet('QListWidget {background-color: rgba(255, 255, 255, 200); padding: 5px; border: none; border-radius: 5px;}'
                                            'QListWidget:item {color: #333; font-size: 14px;}')
        self.note_view_edit.setStyleSheet('QTextEdit {background-color: rgba(255, 255, 255, 200); padding: 5px; border: none; border-radius: 5px;}')

        # Скрытие дополнительных виджетов
        self.note_title_edit.hide()
        self.note_content_edit.hide()
        self.save_note_button.hide()
        self.note_list_widget.hide()
        self.note_view_edit.hide()

        # Добавление дополнительных виджетов на основной макет
        main_layout.addWidget(self.note_title_edit)
        main_layout.addWidget(self.note_content_edit)
        main_layout.addWidget(self.save_note_button)
        main_layout.addWidget(self.note_list_widget)
        main_layout.addWidget(self.note_view_edit)

        # Подсказки для создания заметки
        self.note_title_edit.setPlaceholderText('Введите заголовок заметки')
        self.note_content_edit.setPlaceholderText('Введите содержание заметки')

        # Подключение функций-обработчиков к кнопкам
        self.create_note_button.clicked.connect(self.show_note_creation)
        self.save_note_button.clicked.connect(self.save_note)
        self.view_notes_button.clicked.connect(self.show_note_list)

        # Подключение обработчика событий для открытия заметки
        self.note_list_widget.itemDoubleClicked.connect(self.view_note)

    def show_note_creation(self):
        # Показать поля для создания заметки
        self.note_title_edit.show()
        self.note_content_edit.show()
        self.save_note_button.show()
        self.note_list_widget.hide()
        self.note_view_edit.hide()

    def show_note_list(self):
        # Показать список заметок
        self.note_title_edit.hide()
        self.note_content_edit.hide()
        self.save_note_button.hide()
        self.note_list_widget.show()
        self.note_view_edit.hide()

    def save_note(self):
        # Сохранить заметку
        title = self.note_title_edit.text()
        content = self.note_content_edit.toPlainText()
        if title and content:
            self.notes[title] = content  # Добавляем заметку в словарь
            self.note_list_widget.addItem(title)
            self.note_content_edit.clear()
            self.note_title_edit.clear()

    def view_note(self, item):
        # Просмотр заметки при двойном щелчке на элементе списка
        title = item.text()
        content = self.notes.get(title)  # Получаем содержание заметки по заголовку из словаря
        if content:
            self.note_view_edit.setPlainText(content)
            self.note_view_edit.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    notes_app = NotesApp()
    notes_app.show()
    sys.exit(app.exec_())
