#-------Импортируем необходимые классы--------#
from PyQt6.QtWidgets import QApplication, QListWidget, QMainWindow, QVBoxLayout, QPushButton, QWidget, QLineEdit

#-------Создаем класс MainWindow, наследующий от QMainWindow--------#
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QListWidget Example")

        #-------Создаем виджет и QVBoxLayout--------#
        widget = QWidget(self)
        layout = QVBoxLayout(widget)

        #-------Создаем объект QListWidget и добавляем элементы--------#
        self.list_widget = QListWidget(self)
        self.list_widget.addItems(["Элемент 1", "Элемент 2", "Элемент 3", "Элемент 4"])

        self.line_edit = QLineEdit(self)
        self.line_edit.setInputMask('aaa999')
        self.line_edit.setPlaceholderText("Введите буквы и цифры (например: ABC123)")
        self.setCentralWidget(self.line_edit)



        #-------Добавляем виджеты в layout--------#
        layout.addWidget(self.list_widget)


        #-------Устанавливаем layout в основной виджет-------#
        self.setCentralWidget(widget)
        #-------Применение стилей через setStyleSheet--------#
        self.list_widget.setStyleSheet("""
        QListWidget {
            background-color: lightblue;
            font-size: 16px;
            color: darkblue;
        }
    """)


app = QApplication([])
window = MainWindow()
window.show()
app.exec()