#uses 'ox' conda environment 
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QLabel, QVBoxLayout, QMessageBox
import sys

class StartPage(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Start Page")
        self.setGeometry(100, 100, 280, 80)

        self.button = QPushButton("Go to Login", self)
        self.button.clicked.connect(self.goToLogin)
        layout = QVBoxLayout()
        layout.addWidget(self.button)
        self.setLayout(layout)

    def goToLogin(self):
        self.loginPage = LoginPage()
        self.loginPage.show()
        self.close()

class LoginPage(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Login")
        self.setGeometry(100, 100, 280, 150)

        layout = QVBoxLayout()

        self.username = QLineEdit(self)
        self.username.setPlaceholderText("Username")
        layout.addWidget(self.username)

        self.password = QLineEdit(self)
        self.password.setPlaceholderText("Password")
        self.password.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.password)

        self.button = QPushButton("Login", self)
        self.button.clicked.connect(self.checkCredentials)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def checkCredentials(self):
        # Here you should implement the login logic
        if self.username.text() == "user" and self.password.text() == "pass":
            self.homePage = HomePage()
            self.homePage.show()
            self.close()
        else:
            QMessageBox.warning(self, "Error", "Wrong username or password")

class HomePage(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Home")
        self.setGeometry(100, 100, 280, 80)
        self.label = QLabel("Welcome to the Home Page", self)
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)

def main():
    app = QApplication(sys.argv)
    startPage = StartPage()
    startPage.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
