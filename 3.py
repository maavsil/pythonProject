from PyQt6.QtWidgets import QApplication, QLineEdit, QMainWindow, QWidget, QVBoxLayout, QListWidget, QComboBox, QPushButton
class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("simple app")

    #----------text----------#
    self.line_edit = QLineEdit(self)
    self.line_edit.setPlaceholderText("Введите буквы и цифры (например: ABC123)")
    self.line_edit.setInputMask("aaa999")

    self.setCentralWidget(self.line_edit)

    #--------element--------#
    element = QWidget(self)
    layout = QVBoxLayout(element)
    self.list_element = QListWidget(self)
    self.list_element.addItems(["Элемент 1", "Элемент 2", "Элемент 3", "Элемент 4", "Элемент 5"])
    layout.addWidget(self.list_element)

    self.setCentralWidget(element)

    # --------hide--------#
    hide = QWidget(self)
    layout = QVBoxLayout(hide)

    self.combo_box = QComboBox(self)
    self.combo_box.addItems(["Опция 1", "Опция 2", "Опция 3", "Опция 4"])
    layout.addWidget(self.combo_box)
    self.setCentralWidget(hide)

    # --------button--------#
    layout = QVBoxLayout()
    button = QPushButton('Добавить')
    layout.addWidget(button)
    self.setCentralWidget(button)



app = QApplication([])
window = MainWindow()
window.show()
app.exec()





