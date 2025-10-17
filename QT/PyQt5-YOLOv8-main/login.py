import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('无人驾驶视觉环境感知多目标检测系统')
        self.setGeometry(100, 100, 400, 300)

        # 设置主布局
        mainLayout = QVBoxLayout()

        # 欢迎标签
        welcomeLabel = QLabel('欢迎登录', self)
        welcomeLabel.setAlignment(Qt.AlignCenter)
        welcomeLabel.setFont(QFont('Arial', 24))

        # 输入框和标签布局
        formLayout = QVBoxLayout()

        # 用户名输入
        usernameLabel = QLabel('用户名', self)
        usernameLabel.setFont(QFont('Arial', 14))
        usernameInput = QLineEdit(self)
        usernameInput.setPlaceholderText('admin')
        usernameInput.setFont(QFont('Arial', 14))
        usernameInput.setObjectName("usernameInput")

        # 密码输入
        passwordLabel = QLabel('密码', self)
        passwordLabel.setFont(QFont('Arial', 14))
        passwordInput = QLineEdit(self)
        passwordInput.setEchoMode(QLineEdit.Password)
        passwordInput.setFont(QFont('Arial', 14))
        passwordInput.setObjectName("passwordInput")

        # 登录按钮
        loginButton = QPushButton('登录', self)
        loginButton.setFont(QFont('Arial', 14))
        loginButton.clicked.connect(self.check_login)

        # 注册和忘记密码标签
        footerLayout = QHBoxLayout()
        registerLabel = QLabel('<a href="#">注册新用户</a>', self)
        registerLabel.setAlignment(Qt.AlignLeft)
        registerLabel.setOpenExternalLinks(True)
        registerLabel.setFont(QFont('Arial', 12))

        forgotPasswordLabel = QLabel('<a href="#">忘记密码</a>', self)
        forgotPasswordLabel.setAlignment(Qt.AlignRight)
        forgotPasswordLabel.setOpenExternalLinks(True)
        forgotPasswordLabel.setFont(QFont('Arial', 12))

        footerLayout.addWidget(registerLabel)
        footerLayout.addWidget(forgotPasswordLabel)

        # 添加到布局
        formLayout.addWidget(usernameLabel)
        formLayout.addWidget(usernameInput)
        formLayout.addWidget(passwordLabel)
        formLayout.addWidget(passwordInput)
        formLayout.addWidget(loginButton)

        mainLayout.addWidget(welcomeLabel)
        mainLayout.addLayout(formLayout)
        mainLayout.addLayout(footerLayout)

        self.setLayout(mainLayout)

        # 设置样式表
        self.setStyleSheet("""
            QLabel {
                color: #333;
            }
            QLineEdit {
                border: 1px solid #ccc;
                border-radius: 4px;
                padding: 8px;
                font-size: 14px;
            }
            QPushButton {
                background-color: #5cb85c;
                color: white;
                border: none;
                padding: 10px 20px;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #4cae4c;
            }
        """)

        self.show()

    def check_login(self):
        username = self.findChild(QLineEdit, "usernameInput").text()
        password = self.findChild(QLineEdit, "passwordInput").text()

        if username == "admin" and password == "password":
            QMessageBox.information(self, "成功", "登录成功")
        else:
            QMessageBox.warning(self, "错误", "用户名或密码错误")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = LoginWindow()
    sys.exit(app.exec_())
