from PyQt6.QtWidgets import QApplication, QLineEdit, QMainWindow, QWidget, QVBoxLayout, QListWidget
class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("simple app")

    widget = QWidget(self)
    layout = QVBoxLayout(widget)

    self.list_widget = QListWidget(self)
    self.list_widget.addItems(["Элемент 1", "Элемент 2", "Элемент 3", "Элемент 4", "Элемент 5"])
    layout.addWidget(self.list_widget)
    self.setCentralWidget(widget)

    self.line_edit = QLineEdit(self)
    self.line_edit.setInputMask('aaa999')
    self.line_edit.setPlaceholderText("Введите буквы и цифры (например: ABC123)")
    self.setCentralWidget(self.line_edit)
    self.list_widget.setStyleSheet("""
            QListWidget {
                background-color: lightblue;
                font-size: 16px;
                color: darkblue;
            }
        """)
    layout.addWidget(self.list_widget)


app = QApplication([])
window = MainWindow()
window.show()
app.exec()




