from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel




def main(): 
    app = QApplication([])
    welcomeWindow = QWidget()
    welcomeWindow.setMinimumSize(400,200)
    welcomeWindow.setWindowTitle("Atlas E.X.P")
    layout = QVBoxLayout()

    welcomeLabel = QLabel("Welcome to Atlas E.X.P!")
    layout.addWidget(welcomeLabel)
    layout.addWidget(QPushButton('Continue'))
    layout.addWidget(QPushButton('FAQ'))

    welcomeWindow.setLayout(layout)

    welcomeWindow.show()
    app.exec()

main()
