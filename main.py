import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QGridLayout
from PyQt5.QtCore import Qt

class Calculator(QWidget):


    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setFixedSize(600, 600)
        self.answer_line = QLineEdit(self)
        self.button_1 = QPushButton("1", self)
        self.button_2 = QPushButton("2", self)
        self.button_3 = QPushButton("3", self)
        self.button_4 = QPushButton("4", self)
        
        self.button_5 = QPushButton("5", self)
        self.button_6 = QPushButton("6", self)
        self.button_7 = QPushButton("7", self)
        self.button_8 = QPushButton("8", self)

        self.button_9 = QPushButton("9", self)
        self.button_0 = QPushButton("0", self)

        self.button_plus = QPushButton("+", self)
        self.button_minus = QPushButton("-", self)
        self.button_multiply = QPushButton("x", self)
        self.button_divide = QPushButton(":", self)

        self.button_clear = QPushButton("C", self)
        self.button_equals = QPushButton("=", self)
        self.button_left_bracket = QPushButton("(", self)
        self.button_right_bracket = QPushButton(")", self)
        self.initUI()
    
    def initUI(self):
        grid = QGridLayout()

        grid.addWidget(self.answer_line, 0, 0, 1, 4)

        grid.addWidget(self.button_1, 1, 0)
        grid.addWidget(self.button_2, 1, 1)
        grid.addWidget(self.button_3, 1, 2)

        grid.addWidget(self.button_4, 2, 0)
        grid.addWidget(self.button_5, 2, 1)
        grid.addWidget(self.button_6, 2, 2)

        grid.addWidget(self.button_7, 3, 0)
        grid.addWidget(self.button_8, 3, 1)
        grid.addWidget(self.button_9, 3, 2)

        grid.addWidget(self.button_0, 4, 1)

        grid.addWidget(self.button_plus, 1, 3)
        grid.addWidget(self.button_minus, 2, 3)
        grid.addWidget(self.button_multiply, 3, 3)
        grid.addWidget(self.button_divide, 4, 3)

        grid.addWidget(self.button_clear, 5, 0, 1, 2)
        grid.addWidget(self.button_equals, 5, 2, 1, 2)
        grid.addWidget(self.button_left_bracket, 4, 0)
        grid.addWidget(self.button_right_bracket, 4, 2)

        self.setLayout(grid)

        self.setStyleSheet("""
            QWidget {
                background-color: #2d4873;
            }
            QLineEdit {
                font-size: 30px;
                font-family: Arial;
                color: black;
                background-color: #b5d2ff;
                border-radius: 10px;
                border: 3px solid #78acfa;
                font-weight: bold;
                padding: 30px;
            }

            QPushButton {
                font-size: 30px;
                font-family: Arial;
                padding: 10px;
                border: 3px solid #78acfa;
                border-radius: 20px;
                background-color: #b5d2ff;
            }

            QPushButton:hover {
                background-color: #cce0ff;
            }
        """)

        self.button_0.clicked.connect(self.update_label)
        self.button_1.clicked.connect(self.update_label)
        self.button_2.clicked.connect(self.update_label)
        self.button_3.clicked.connect(self.update_label)
        self.button_4.clicked.connect(self.update_label)
        self.button_5.clicked.connect(self.update_label)
        self.button_6.clicked.connect(self.update_label)
        self.button_7.clicked.connect(self.update_label)
        self.button_8.clicked.connect(self.update_label)
        self.button_9.clicked.connect(self.update_label)

        self.button_plus.clicked.connect(self.update_label)
        self.button_minus.clicked.connect(self.update_label)
        self.button_multiply.clicked.connect(self.update_label)
        self.button_divide.clicked.connect(self.update_label)

        self.button_clear.clicked.connect(self.clear)
        self.button_equals.clicked.connect(self.evaluate)
        self.button_left_bracket.clicked.connect(self.update_label)
        self.button_right_bracket.clicked.connect(self.update_label)

    def update_label(self):
        if self.sender().text() == "x":
            self.answer_line.setText(self.answer_line.text() + "*")
        elif self.sender().text() == ":":
            self.answer_line.setText(self.answer_line.text() + "/")
        else:
            self.answer_line.setText(self.answer_line.text() + self.sender().text())
    
    def evaluate(self):
        if self.answer_line.text() == "9/11":
            self.answer_line.setText(f"✈️🏢🏢")
        else:
            self.answer_line.setText(f"{eval(self.answer_line.text())}")
        if self.answer_line.text() == "":
            return


    def clear(self):
        self.answer_line.setText("")

def main():
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()