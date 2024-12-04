from PyQt6.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QMainWindow, QVBoxLayout, QWidget, QCheckBox, QRadioButton, QSlider, QLabel, QHBoxLayout
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QTableWidget Example")  # Установка заголовка окна
        layout1 = QHBoxLayout()
        layout2 = QVBoxLayout()

        main_widget = QWidget(self)
        
        main_layout = QVBoxLayout(main_widget)
        main_layout.addLayout(layout1)



        #--------------QCheckBox---------------#
        self.checkbox1 = QCheckBox('Опция 1')
        self.checkbox2 = QCheckBox('Опция 2')
        layout1.addWidget(self.checkbox1)
        layout1.addWidget(self.checkbox2)

        # --------------QRadioButton---------------#
        self.RadioBox1 = QRadioButton('Вариант 1')
        self.RadioBox2 = QRadioButton('Вариант 2')
        layout2.addWidget(self.RadioBox1)
        layout2.addWidget(self.RadioBox2)
        main_layout.addLayout(layout2)

        # --------------QTableWidget---------------#
        self.table_widget = QTableWidget(self)
        self.table_widget.setRowCount(3)
        self.table_widget.setColumnCount(2)
        self.table_widget.setHorizontalHeaderLabels(["Колонка 1", "Колонка 2"])
        main_layout.addWidget(self.table_widget)

        # --------------QSlider---------------#
        self.slider = QSlider(Qt.Orientation.Horizontal, self)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.setValue(1)
        self.slider.setTickInterval(10)


        main_layout.addWidget(self.slider)

        self.setCentralWidget(main_widget)



app = QApplication([])
window = MainWindow()
window.show()
app.exec()