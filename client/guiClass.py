import sys
from PyQt6.QtWidgets import QApplication, QPushButton, QStackedWidget, QVBoxLayout, QWidget

class MainWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Create the stacked widget
        self.stacked_widget = QStackedWidget()

        # Create the first widget and add it to the stack
        self.first_widget = QWidget()
        self.first_widget_layout = QVBoxLayout(self.first_widget)
        self.switch_to_second = QPushButton("Switch to Second Widget", self.first_widget)
        self.switch_to_second.clicked.connect(self.switchToSecondWidget)
        self.first_widget_layout.addWidget(self.switch_to_second)

        self.stacked_widget.addWidget(self.first_widget)

        # Create the second widget and add it to the stack
        self.second_widget = QWidget()
        self.second_widget_layout = QVBoxLayout(self.second_widget)
        self.switch_to_first = QPushButton("Switch to First Widget", self.second_widget)
        self.switch_to_first.clicked.connect(self.switchToFirstWidget)
        self.second_widget_layout.addWidget(self.switch_to_first)

        self.stacked_widget.addWidget(self.second_widget)

        # Set the layout for the main widget
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(self.stacked_widget)

    def switchToFirstWidget(self):
        self.stacked_widget.setCurrentIndex(0)

    def switchToSecondWidget(self):
        self.stacked_widget.setCurrentIndex(1)

def main():
    app = QApplication(sys.argv)
    main_widget = MainWidget()
    main_widget.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
