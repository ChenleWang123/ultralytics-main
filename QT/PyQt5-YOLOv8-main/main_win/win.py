from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(1394, 762)
        mainWindow.setMouseTracking(True)
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap("E:/Programme/Python_Projects/ultralytics-main/QT/PyQt5-YOLOv8-main/icon/图片.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainWindow.setWindowIcon(icon)
        mainWindow.setStyleSheet("#mainWindow{border:none;}")
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_main = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_main.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_main.setSpacing(0)
        self.verticalLayout_main.setObjectName("verticalLayout_main")

        # 标题栏
        self.groupBox_18 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_18.setStyleSheet("#groupBox_18{border-image: url(file:///E:/Programme/Python_Projects/ultralytics-main/QT/PyQt5-YOLOv8-main/icon/background1.jpg);\n"
                                       "border: 0px solid #42adff;\n"
                                       "border-radius:5px;}")
        self.groupBox_18.setTitle("")
        self.groupBox_18.setObjectName("groupBox_18")
        self.verticalLayout_main_2 = QtWidgets.QVBoxLayout(self.groupBox_18)
        self.verticalLayout_main_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_main_2.setSpacing(0)
        self.verticalLayout_main_2.setObjectName("verticalLayout_main_2")
        self.groupBox = QtWidgets.QGroupBox(self.groupBox_18)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 90))
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 90))
        self.groupBox.setStyleSheet("#groupBox{\n"
                                    "background-color: rgba(75, 75, 75, 200);\n"
                                    "border: 0px solid #42adff;\n"
                                    "border-left: 0px solid rgba(29, 83, 185, 255);\n"
                                    "border-right: 0px solid rgba(29, 83, 185, 255);\n"
                                    "border-bottom: 1px solid rgba(200, 200, 200,100);\n"
                                    ";\n"
                                    "border-radius:0px;}")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_icon = QtWidgets.QLabel(self.groupBox)
        self.label_icon.setMinimumSize(QtCore.QSize(40, 40))
        self.label_icon.setMaximumSize(QtCore.QSize(40, 40))
        # self.label_icon.setStyleSheet("image: url(:/img/icon/conan.png);")
        self.label_icon.setStyleSheet(
            "image: url('E:/Programme/Python_Projects/ultralytics-main/QT/PyQt5-YOLOv8-main/icon/图片.png');")
        self.label_icon.setText("")
        self.label_icon.setObjectName("label_icon")
        self.horizontalLayout.addWidget(self.label_icon)
        self.label_title = QtWidgets.QLabel(self.groupBox)
        self.label_title.setStyleSheet("QLabel\n"
                                       "{\n"
                                       "    font-size: 42px;\n"
                                       "    font-family: \"Microsoft YaHei\";\n"
                                       "    font-weight: bold;\n"
                                       "         border-radius:9px;\n"
                                       "        background:rgba(66, 195, 255, 0);\n"
                                       "color: rgb(218, 218, 218);\n"
                                       "    margin: 10px; /* 设置内边距为10像素 */\n"
                                       "}\n"
                                       "")
        self.label_title.setObjectName("label_title")
        self.horizontalLayout.addWidget(self.label_title)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.minButton = QtWidgets.QPushButton(self.groupBox)
        self.minButton.setMinimumSize(QtCore.QSize(50, 28))
        self.minButton.setMaximumSize(QtCore.QSize(50, 28))
        self.minButton.setStyleSheet("QPushButton {\n"
                                     "border-style: solid;\n"
                                     "border-width: 0px;\n"
                                     "border-radius: 0px;\n"
                                     "background-color: rgba(223, 223, 223, 0);}\n"
                                     "QPushButton::focus{outline: none;}\n"
                                     "QPushButton::hover {\n"
                                     "border-style: solid;\n"
                                     "border-width: 0px;\n"
                                     "border-radius: 0px;\n"
                                     "background-color: rgba(223, 223, 223, 150);}")
        self.minButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/img/icon/最小化.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.minButton.setIcon(icon1)
        self.minButton.setObjectName("minButton")
        self.horizontalLayout_5.addWidget(self.minButton)
        self.maxButton = QtWidgets.QPushButton(self.groupBox)
        self.maxButton.setMinimumSize(QtCore.QSize(50, 28))
        self.maxButton.setMaximumSize(QtCore.QSize(50, 28))
        self.maxButton.setStyleSheet("QPushButton {\n"
                                     "border-style: solid;\n"
                                     "border-width: 0px;\n"
                                     "border-radius: 0px;\n"
                                     "background-color: rgba(223, 223, 223, 0);}\n"
                                     "QPushButton::focus{outline: none;}\n"
                                     "QPushButton::hover {\n"
                                     "border-style: solid;\n"
                                     "border-width: 0px;\n"
                                     "border-radius: 0px;\n"
                                     "background-color: rgba(223, 223, 223, 150);}")
        self.maxButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/img/icon/正方形.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2.addPixmap(QtGui.QPixmap(":/img/icon/还原.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        icon2.addPixmap(QtGui.QPixmap(":/img/icon/还原.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.maxButton.setIcon(icon2)
        self.maxButton.setCheckable(True)
        self.maxButton.setObjectName("maxButton")
        self.horizontalLayout_5.addWidget(self.maxButton)
        self.closeButton = QtWidgets.QPushButton(self.groupBox)
        self.closeButton.setMinimumSize(QtCore.QSize(50, 28))
        self.closeButton.setMaximumSize(QtCore.QSize(50, 28))
        self.closeButton.setStyleSheet("QPushButton {\n"
                                       "border-style: solid;\n"
                                       "border-width: 0px;\n"
                                       "border-radius: 0px;\n"
                                       "background-color: rgba(223, 223, 223, 0);}\n"
                                       "QPushButton::focus{outline: none;}\n"
                                       "QPushButton::hover {\n"
                                       "border-style: solid;\n"
                                       "border-width: 0px;\n"
                                       "border-radius: 0px;\n"
                                       "background-color: rgba(223, 223, 223, 150);}")
        self.closeButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/img/icon/关闭.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closeButton.setIcon(icon3)
        self.closeButton.setObjectName("closeButton")
        self.horizontalLayout_5.addWidget(self.closeButton)
        self.horizontalLayout.addLayout(self.horizontalLayout_5)
        self.verticalLayout_main_2.addWidget(self.groupBox)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.groupBox_8 = QtWidgets.QGroupBox(self.groupBox_18)
        self.groupBox_8.setMinimumSize(QtCore.QSize(520, 0))
        self.groupBox_8.setMaximumSize(QtCore.QSize(520, 16777215))
        self.groupBox_8.setStyleSheet("#groupBox_8{\n"
                                      "background-color: rgba(75, 75, 75, 200);\n"
                                      "border: 0px solid #42adff;\n"
                                      "border-radius:0px;}\n"
                                      "")
        self.groupBox_8.setTitle("")
        self.groupBox_8.setObjectName("groupBox_8")

        # 垂直边距
        self.verticalLayout_sidebar = QtWidgets.QVBoxLayout(self.groupBox_8)
        self.verticalLayout_sidebar.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_sidebar.setSpacing(41)
        self.verticalLayout_sidebar.setObjectName("verticalLayout_sidebar")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox_8)
        self.groupBox_2.setMinimumSize(QtCore.QSize(0, 60))
        self.groupBox_2.setMaximumSize(QtCore.QSize(16777215, 60))
        self.groupBox_2.setStyleSheet("#groupBox_2{\n"
                                      "border: 0px solid #42adff;\n"
                                      "border-bottom: 1px solid rgba(200, 200, 200,100);\n"
                                      "border-radius:0px;}")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_setting = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_setting.setContentsMargins(11, 0, 11, 0)
        self.horizontalLayout_setting.setObjectName("horizontalLayout_setting")
        self.label_setting = QtWidgets.QLabel(self.groupBox_2)
        self.label_setting.setMinimumSize(QtCore.QSize(0, 0))
        self.label_setting.setMaximumSize(QtCore.QSize(16777215, 60))
        self.label_setting.setStyleSheet("QLabel\n"
                                         "{\n"
                                         "    font-size: 42px;\n"
                                         "    font-family: \"Microsoft YaHei\";\n"
                                         "    font-weight: bold;\n"
                                         "         border-radius:9px;\n"
                                         "        background:rgba(66, 195, 255, 0);\n"
                                         "color: rgb(218, 218, 218);\n"
                                         "\n"
                                         "}\n"
                                         "")
        self.label_setting.setObjectName("label_setting")
        self.horizontalLayout_setting.addWidget(self.label_setting)
        spacerItem1 = QtWidgets.QSpacerItem(37, 39, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_setting.addItem(spacerItem1)
        self.verticalLayout_sidebar.addWidget(self.groupBox_2)
        self.horizontalLayout_model = QtWidgets.QHBoxLayout()
        self.horizontalLayout_model.setContentsMargins(11, -1, 11, -1)
        self.horizontalLayout_model.setObjectName("horizontalLayout_model")
        self.label_model = QtWidgets.QLabel(self.groupBox_8)
        self.label_model.setMinimumSize(QtCore.QSize(0, 40))
        self.label_model.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label_model.setStyleSheet("QLabel\n"
                                       "{\n"
                                       "    font-size: 38px;\n"
                                       "    font-family: \"Microsoft YaHei\";\n"
                                       "    font-weight: bold;\n"
                                       "         border-radius:9px;\n"
                                       "        background:rgba(66, 195, 255, 0);\n"
                                       "color: rgb(218, 218, 218);\n"
                                       "}\n"
                                       "")
        self.label_model.setObjectName("label_model")
        self.horizontalLayout_model.addWidget(self.label_model)
        self.comboBox = QtWidgets.QComboBox(self.groupBox_8)
        self.comboBox.setMinimumSize(QtCore.QSize(0, 38))
        self.comboBox.setStyleSheet("QComboBox QAbstractItemView {\n"
                                    "font-family: \"Microsoft YaHei\";\n"
                                    "font-size: 38px;\n"
                                    "background:rgba(200, 200, 200,150);\n"
                                    "selection-background-color: rgba(200, 200, 200,50);\n"
                                    "color: rgb(218, 218, 218);\n"
                                    "outline:none;\n"
                                    "border:none;}\n"
                                    "QComboBox{\n"
                                    "font-family: \"Microsoft YaHei\";\n"
                                    "font-size: 38px;\n"
                                    "color: rgb(218, 218, 218);\n"
                                    "border-width:0px;\n"
                                    "border-color:white;\n"
                                    "border-style:solid;\n"
                                    "background-color: rgba(200, 200, 200,0);}\n"
                                    "\n"
                                    "QComboBox::drop-down {\n"
                                    "margin-top:8;\n"
                                    "height:20;\n"
                                    "background:rgba(255,255,255,0);\n"
                                    "border-image: url(:/img/icon/下拉_白色.png);\n"
                                    "}\n"
                                    "")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_model.addWidget(self.comboBox)
        self.verticalLayout_sidebar.addLayout(self.horizontalLayout_model)
        self.horizontalLayout_chose_file2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_chose_file2.setContentsMargins(11, -1, 0, -1)
        self.horizontalLayout_chose_file2.setObjectName("horizontalLayout_chose_file2")
        self.label_chose_file = QtWidgets.QLabel(self.groupBox_8)
        self.label_chose_file.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_chose_file.setStyleSheet("QLabel\n"
                                            "{\n"
                                            "    font-size: 38px;\n"
                                            "    font-family: \"Microsoft YaHei\";\n"
                                            "    font-weight: bold;\n"
                                            "         border-radius:9px;\n"
                                            "        background:rgba(66, 195, 255, 0);\n"
                                            "color: rgb(218, 218, 218);\n"
                                            "}\n"
                                            "")
        self.label_chose_file.setObjectName("label_chose_file")
        self.horizontalLayout_chose_file2.addWidget(self.label_chose_file)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox_8)
        self.groupBox_5.setStyleSheet("#groupBox_5{\n"
                                      "background-color: rgba(48,148,243,0);\n"
                                      "border: 0px solid #42adff;\n"
                                      "border-left: 0px solid #d9d9d9;\n"
                                      "border-right: 0px solid rgba(29, 83, 185, 255);\n"
                                      "border-radius:0px;}")
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        # 选择文件
        self.horizontalLayout_chose_file = QtWidgets.QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_chose_file.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_chose_file.setObjectName("horizontalLayout_chose_file")
        self.fileButton = QtWidgets.QPushButton(self.groupBox_5)
        self.fileButton.setMinimumSize(QtCore.QSize(55, 28))
        self.fileButton.setMaximumSize(QtCore.QSize(16777215, 28))
        self.fileButton.setStyleSheet("QPushButton{font-family: \"Microsoft YaHei\";\n"
                                      "font-size: 38px;\n"
                                      "font-weight: bold;\n"
                                      "color:white;\n"
                                      "text-align: center center;\n"
                                      "padding-left: 5px;\n"
                                      "padding-right: 5px;\n"
                                      "padding-top: 4px;\n"
                                      "padding-bottom: 4px;\n"
                                      "border-style: solid;\n"
                                      "border-width: 0px;\n"
                                      "border-color: rgba(255, 255, 255, 255);\n"
                                      "border-radius: 3px;\n"
                                      "background-color: rgba(200, 200, 200,0);}\n"
                                      "\n"
                                      "QPushButton:focus{outline: none;}\n"
                                      "\n"
                                      "QPushButton::pressed{font-family: \"Microsoft YaHei\";\n"
                                      "                     font-size: 24px;\n"
                                      "                     font-weight: bold;\n"
                                      "                     color:rgb(200,200,200);\n"
                                      "                     text-align: center center;\n"
                                      "                     padding-left: 5px;\n"
                                      "                     padding-right: 5px;\n"
                                      "                     padding-top: 4px;\n"
                                      "                     padding-bottom: 4px;\n"
                                      "                     border-style: solid;\n"
                                      "                     border-width: 0px;\n"
                                      "                     border-color: rgba(255, 255, 255, 255);\n"
                                      "                     border-radius: 3px;\n"
                                      "                     background-color:  #bf513b;}\n"
                                      "\n"
                                      "QPushButton::disabled{font-family: \"Microsoft YaHei\";\n"
                                      "                     font-size: 24px;\n"
                                      "                     font-weight: bold;\n"
                                      "                     color:rgb(200,200,200);\n"
                                      "                     text-align: center center;\n"
                                      "                     padding-left: 5px;\n"
                                      "                     padding-right: 5px;\n"
                                      "                     padding-top: 4px;\n"
                                      "                     padding-bottom: 4px;\n"
                                      "                     border-style: solid;\n"
                                      "                     border-width: 0px;\n"
                                      "                     border-color: rgba(255, 255, 255, 255);\n"
                                      "                     border-radius: 3px;\n"
                                      "                     background-color:  #bf513b;}\n"
                                      "QPushButton::hover {\n"
                                      "border-style: solid;\n"
                                      "border-width: 0px;\n"
                                      "border-radius: 0px;\n"
                                      "background-color: rgba(48,148,243,80);}")
        self.fileButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/img/icon/打开.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fileButton.setIcon(icon4)
        self.fileButton.setObjectName("fileButton")
        self.horizontalLayout_chose_file.addWidget(self.fileButton)
        self.horizontalLayout_11.addWidget(self.groupBox_5)
        self.horizontalLayout_chose_file2.addLayout(self.horizontalLayout_11)
        self.verticalLayout_sidebar.addLayout(self.horizontalLayout_chose_file2)
        self.verticalLayout_IoU = QtWidgets.QVBoxLayout()
        self.verticalLayout_IoU.setContentsMargins(11, -1, 11, -1)
        self.verticalLayout_IoU.setSpacing(4)
        self.verticalLayout_IoU.setObjectName("verticalLayout_IoU")
        self.label_IoU = QtWidgets.QLabel(self.groupBox_8)
        self.label_IoU.setStyleSheet("QLabel\n"
                                     "{\n"
                                     "    font-size: 38px;\n"
                                     "    font-family: \"Microsoft YaHei\";\n"
                                     "    font-weight: bold;\n"
                                     "         border-radius:9px;\n"
                                     "        background:rgba(66, 195, 255, 0);\n"
                                     "color: rgb(218, 218, 218);\n"
                                     "}\n"
                                     "")
        self.label_IoU.setObjectName("label_IoU")
        self.verticalLayout_IoU.addWidget(self.label_IoU)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.iouSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox_8)
        self.iouSpinBox.setMinimumSize(QtCore.QSize(100, 0))
        self.iouSpinBox.setMaximumSize(QtCore.QSize(100, 16777215))
        self.iouSpinBox.setStyleSheet("QDoubleSpinBox{\n"
                                      "background:rgba(200, 200, 200,50);\n"
                                      "color:white;\n"
                                      "font-size: 32px;\n"
                                      "font-family: \"Microsoft YaHei UI\";\n"
                                      "border-style: solid;\n"
                                      "border-width: 1px;\n"
                                      "border-color: rgba(200, 200, 200,100);\n"
                                      "border-radius: 3px;}\n"
                                      "\n"
                                      "QDoubleSpinBox::down-button{\n"
                                      "background:rgba(200, 200, 200,0);\n"
                                      "border-image: url(:/img/icon/箭头_列表展开.png);}\n"
                                      "QDoubleSpinBox::down-button::hover{\n"
                                      "background:rgba(200, 200, 200,100);\n"
                                      "border-image: url(:/img/icon/箭头_列表展开.png);}\n"
                                      "\n"
                                      "QDoubleSpinBox::up-button{\n"
                                      "background:rgba(200, 200, 200,0);\n"
                                      "border-image: url(:/img/icon/箭头_列表收起.png);}\n"
                                      "QDoubleSpinBox::up-button::hover{\n"
                                      "background:rgba(200, 200, 200,100);\n"
                                      "border-image: url(:/img/icon/箭头_列表收起.png);}\n"
                                      "")
        self.iouSpinBox.setMaximum(1.0)
        self.iouSpinBox.setSingleStep(0.01)
        self.iouSpinBox.setProperty("value", 0.45)
        self.iouSpinBox.setObjectName("iouSpinBox")
        self.horizontalLayout_4.addWidget(self.iouSpinBox)
        self.iouSlider = QtWidgets.QSlider(self.groupBox_8)
        self.iouSlider.setStyleSheet("QSlider{\n"
                                     "border-color: #bcbcbc;\n"
                                     "color:#d9d9d9;\n"
                                     "}\n"
                                     "QSlider::groove:horizontal {                                \n"
                                     "     border: 1px solid #999999;                             \n"
                                     "     height: 3px;                                           \n"
                                     "    margin: 0px 0;                                         \n"
                                     "     left: 5px; right: 5px; \n"
                                     " }\n"
                                     "QSlider::handle:horizontal {                               \n"
                                     "     border: 0px ; \n"
                                     "     border-image: url(:/img/icon/圆.png);\n"
                                     "     width:15px;\n"
                                     "     margin: -7px -7px -7px -7px;                  \n"
                                     "} \n"
                                     "QSlider::add-page:horizontal{\n"
                                     "background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #d9d9d9, stop:0.25 #d9d9d9, stop:0.5 #d9d9d9, stop:1 #d9d9d9); \n"
                                     "\n"
                                     "}\n"
                                     "QSlider::sub-page:horizontal{                               \n"
                                     " background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #373737, stop:0.25 #373737, stop:0.5 #373737, stop:1 #373737);                     \n"
                                     "}")
        self.iouSlider.setMaximum(100)
        self.iouSlider.setProperty("value", 45)
        self.iouSlider.setOrientation(QtCore.Qt.Horizontal)
        self.iouSlider.setObjectName("iouSlider")
        self.horizontalLayout_4.addWidget(self.iouSlider)
        self.verticalLayout_IoU.addLayout(self.horizontalLayout_4)
        self.verticalLayout_sidebar.addLayout(self.verticalLayout_IoU)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(11, -1, 11, -1)
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_conf = QtWidgets.QLabel(self.groupBox_8)
        self.label_conf.setStyleSheet("QLabel\n"
                                 "{\n"
                                 "    font-size: 38px;\n"
                                 "    font-family: \"Microsoft YaHei\";\n"
                                 "    font-weight: bold;\n"
                                 "         border-radius:9px;\n"
                                 "        background:rgba(66, 195, 255, 0);\n"
                                 "color: rgb(218, 218, 218);\n"
                                 "}\n"
                                 "")
        self.label_conf.setObjectName("label_conf")
        self.verticalLayout.addWidget(self.label_conf)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.confSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox_8)
        self.confSpinBox.setMinimumSize(QtCore.QSize(100, 0))
        self.confSpinBox.setMaximumSize(QtCore.QSize(100, 16777215))
        self.confSpinBox.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.confSpinBox.setStyleSheet("QDoubleSpinBox{\n"
                                       "background:rgba(200, 200, 200,50);\n"
                                       "color:white;\n"
                                       "font-size: 32px;\n"
                                       "font-family: \"Microsoft YaHei UI\";\n"
                                       "border-style: solid;\n"
                                       "border-width: 1px;\n"
                                       "border-color: rgba(200, 200, 200,100);\n"
                                       "border-radius: 3px;}\n"
                                       "\n"
                                       "QDoubleSpinBox::down-button{\n"
                                       "background:rgba(200, 200, 200,0);\n"
                                       "border-image: url(:/img/icon/箭头_列表展开.png);}\n"
                                       "QDoubleSpinBox::down-button::hover{\n"
                                       "background:rgba(200, 200, 200,100);\n"
                                       "border-image: url(:/img/icon/箭头_列表展开.png);}\n"
                                       "\n"
                                       "QDoubleSpinBox::up-button{\n"
                                       "background:rgba(200, 200, 200,0);\n"
                                       "border-image: url(:/img/icon/箭头_列表收起.png);}\n"
                                       "QDoubleSpinBox::up-button::hover{\n"
                                       "background:rgba(200, 200, 200,100);\n"
                                       "border-image: url(:/img/icon/箭头_列表收起.png);}\n"
                                       "")
        self.confSpinBox.setMaximum(1.0)
        self.confSpinBox.setSingleStep(0.01)
        self.confSpinBox.setProperty("value", 0.25)
        self.confSpinBox.setObjectName("confSpinBox")
        self.horizontalLayout_3.addWidget(self.confSpinBox)
        self.confSlider = QtWidgets.QSlider(self.groupBox_8)
        self.confSlider.setStyleSheet("QSlider{\n"
                                      "border-color: #bcbcbc;\n"
                                      "color:#d9d9d9;\n"
                                      "}\n"
                                      "QSlider::groove:horizontal {                                \n"
                                      "     border: 1px solid #999999;                             \n"
                                      "     height: 3px;                                           \n"
                                      "    margin: 0px 0;                                         \n"
                                      "     left: 5px; right: 5px; \n"
                                      " }\n"
                                      "QSlider::handle:horizontal {                               \n"
                                      "     border: 0px ; \n"
                                      "     border-image: url(:/img/icon/圆.png);\n"
                                      "     width:15px;\n"
                                      "     margin: -7px -7px -7px -7px;                  \n"
                                      "} \n"
                                      "QSlider::add-page:horizontal{\n"
                                      "background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #d9d9d9, stop:0.25 #d9d9d9, stop:0.5 #d9d9d9, stop:1 #d9d9d9); \n"
                                      "\n"
                                      "}\n"
                                      "QSlider::sub-page:horizontal{                               \n"
                                      " background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #373737, stop:0.25 #373737, stop:0.5 #373737, stop:1 #373737);                     \n"
                                      "}")
        self.confSlider.setMaximum(100)
        self.confSlider.setProperty("value", 25)
        self.confSlider.setOrientation(QtCore.Qt.Horizontal)
        self.confSlider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.confSlider.setObjectName("confSlider")
        self.horizontalLayout_3.addWidget(self.confSlider)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_sidebar.addLayout(self.verticalLayout)
        self.verticalLayout_latency = QtWidgets.QVBoxLayout()
        self.verticalLayout_latency.setContentsMargins(11, -1, 11, -1)
        self.verticalLayout_latency.setSpacing(4)
        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox_8)
        self.groupBox_6.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox_6.setMaximumSize(QtCore.QSize(16777215, 42))
        self.groupBox_6.setStyleSheet("#groupBox_6{\n"
                                      "border: 0px solid #42adff;\n"
                                      "border-radius:0px;}")
        self.groupBox_6.setTitle("")
        self.groupBox_6.setObjectName("groupBox_6")
        self.verticalLayout_sidebar.addWidget(self.groupBox_6)
        self.verticalLayout_autosave = QtWidgets.QVBoxLayout()
        self.verticalLayout_autosave.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_autosave.setObjectName("verticalLayout_autosave")
        self.groupBox_10 = QtWidgets.QGroupBox(self.groupBox_8)
        self.groupBox_10.setMinimumSize(QtCore.QSize(0, 42))
        self.groupBox_10.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.groupBox_10.setStyleSheet("#groupBox_10{\n"
                                       "border: 0px solid #42adff;\n"
                                       "\n"
                                       "border-radius:0px;}")
        self.groupBox_10.setTitle("")
        self.groupBox_10.setObjectName("groupBox_10")
        self.horizontalLayout_39 = QtWidgets.QHBoxLayout(self.groupBox_10)
        self.horizontalLayout_39.setContentsMargins(11, 0, 11, 0)
        self.horizontalLayout_39.setObjectName("horizontalLayout_39")
        self.resultWidget = QtWidgets.QListWidget(self.groupBox_10)
        self.resultWidget.setStyleSheet("QListWidget{\n"
                                        "background-color: rgba(12, 28, 77, 0);\n"
                                        "\n"
                                        "border-radius:0px;\n"
                                        "font-family: \"Microsoft YaHei\";\n"
                                        "font-size: 24px;\n"
                                        "color: rgb(218, 218, 218);\n"
                                        "}\n"
                                        "")
        self.resultWidget.setObjectName("resultWidget")
        self.horizontalLayout_39.addWidget(self.resultWidget)
        self.verticalLayout_autosave.addWidget(self.groupBox_10)
        self.verticalLayout_autosave.setStretch(1, 1)
        self.verticalLayout_sidebar.addLayout(self.verticalLayout_autosave)
        self.horizontalLayout_7.addWidget(self.groupBox_8)
        self.groupBox_201 = QtWidgets.QGroupBox(self.groupBox_18)
        self.groupBox_201.setStyleSheet("#groupBox_201{\n"
                                        "background-color: rgba(95, 95, 95, 200);\n"
                                        "border: 0px solid #42adff;\n"
                                        "border-left: 1px solid rgba(200, 200, 200,100);\n"
                                        "border-right: 0px solid rgba(29, 83, 185, 255);\n"
                                        "border-radius:0px;}")
        self.groupBox_201.setTitle("")
        self.groupBox_201.setObjectName("groupBox_201")
        self.verticalLayout_show = QtWidgets.QVBoxLayout(self.groupBox_201)
        self.verticalLayout_show.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_show.setObjectName("verticalLayout_show")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_201)
        self.groupBox_3.setMinimumSize(QtCore.QSize(0, 60))
        self.groupBox_3.setMaximumSize(QtCore.QSize(16777215, 60))
        self.groupBox_3.setStyleSheet("#groupBox_3{\n"
                                      "border: 0px solid #42adff;\n"
                                      "border-bottom: 1px solid rgba(200, 200, 200,100);\n"
                                      "border-radius:0px;}")
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_show = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_show.setContentsMargins(11, 0, 11, 0)
        self.horizontalLayout_show.setObjectName("horizontalLayout_show")
        self.label_show = QtWidgets.QLabel(self.groupBox_3)
        self.label_show.setMinimumSize(QtCore.QSize(0, 0))
        self.label_show.setMaximumSize(QtCore.QSize(16777215, 60))
        self.label_show.setStyleSheet("QLabel\n"
                                      "{\n"
                                      "    font-size: 42px;\n"
                                      "    font-family: \"Microsoft YaHei\";\n"
                                      "    font-weight: bold;\n"
                                      "         border-radius:9px;\n"
                                      "        background:rgba(66, 195, 255, 0);\n"
                                      "color: rgb(218, 218, 218);\n"
                                      "}\n"
                                      "")
        self.label_show.setObjectName("label_show")
        self.horizontalLayout_show.addWidget(self.label_show)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_show.addItem(spacerItem3)
        self.fps_label = QtWidgets.QLabel(self.groupBox_3)
        self.fps_label.setMinimumSize(QtCore.QSize(100, 40))
        self.fps_label.setMaximumSize(QtCore.QSize(100, 40))
        self.fps_label.setStyleSheet("QLabel\n"
                                     "{\n"
                                     "    font-size: 24px;\n"
                                     "    font-family: \"Microsoft YaHei\";\n"
                                     "    font-weight: bold;\n"
                                     "         border-radius:9px;\n"
                                     "        background:rgba(66, 195, 255, 0);\n"
                                     "color: rgb(218, 218, 218);\n"
                                     "}\n"
                                     "")
        self.fps_label.setText("")
        self.fps_label.setAlignment(QtCore.Qt.AlignCenter)
        self.fps_label.setObjectName("fps_label")
        self.horizontalLayout_show.addWidget(self.fps_label)
        self.verticalLayout_show.addWidget(self.groupBox_3)
        self.splitter = QtWidgets.QSplitter(self.groupBox_201)
        self.splitter.setEnabled(True)
        self.splitter.setStyleSheet("#splitter::handle{background: 1px solid  rgba(200, 200, 200,100);}")
        self.splitter.setFrameShape(QtWidgets.QFrame.NoFrame)
        # Splitter 展示分割器配置
        self.splitter.setLineWidth(10)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setHandleWidth(1)
        self.splitter.setObjectName("splitter")
        self.raw_video = Label_click_Mouse(self.splitter)
        self.raw_video.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.raw_video.sizePolicy().hasHeightForWidth())
        self.raw_video.setSizePolicy(sizePolicy)
        self.raw_video.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(36)
        self.raw_video.setFont(font)
        self.raw_video.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.raw_video.setStyleSheet("color: rgb(218, 218, 218);\n"
                                     "")
        self.raw_video.setText("")
        self.raw_video.setScaledContents(False)
        self.raw_video.setAlignment(QtCore.Qt.AlignCenter)
        self.raw_video.setObjectName("raw_video")
        self.out_video = Label_click_Mouse(self.splitter)
        self.out_video.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.out_video.sizePolicy().hasHeightForWidth())
        self.out_video.setSizePolicy(sizePolicy)
        self.out_video.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(36)
        self.out_video.setFont(font)
        self.out_video.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.out_video.setStyleSheet("color: rgb(218, 218, 218);\n"
                                     "")
        self.out_video.setText("")
        self.out_video.setScaledContents(False)
        self.out_video.setAlignment(QtCore.Qt.AlignCenter)
        self.out_video.setObjectName("out_video")
        self.verticalLayout_show.addWidget(self.splitter)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setContentsMargins(11, -1, 11, -1)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.runButton = QtWidgets.QPushButton(self.groupBox_201)
        self.runButton.setMinimumSize(QtCore.QSize(40, 40))
        self.runButton.setStyleSheet("QPushButton {\n"
                                     "border-style: solid;\n"
                                     "border-width: 0px;\n"
                                     "border-radius: 0px;\n"
                                     "background-color: rgba(223, 223, 223, 0);\n"
                                     "}\n"
                                     "QPushButton::focus{outline: none;}\n"
                                     "QPushButton::hover {\n"
                                     "border-style: solid;\n"
                                     "border-width: 0px;\n"
                                     "border-radius: 0px;\n"
                                     "background-color: rgba(223, 223, 223, 150);}")
        self.runButton.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/img/icon/运行.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon7.addPixmap(QtGui.QPixmap(":/img/icon/暂停.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon7.addPixmap(QtGui.QPixmap(":/img/icon/运行.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        icon7.addPixmap(QtGui.QPixmap(":/img/icon/暂停.png"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        icon7.addPixmap(QtGui.QPixmap(":/img/icon/运行.png"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon7.addPixmap(QtGui.QPixmap(":/img/icon/暂停.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        icon7.addPixmap(QtGui.QPixmap(":/img/icon/运行.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        icon7.addPixmap(QtGui.QPixmap(":/img/icon/暂停.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.runButton.setIcon(icon7)
        self.runButton.setIconSize(QtCore.QSize(30, 30))
        self.runButton.setCheckable(True)
        self.runButton.setObjectName("runButton")
        self.horizontalLayout_12.addWidget(self.runButton)
        self.progressBar = QtWidgets.QProgressBar(self.groupBox_201)
        self.progressBar.setMaximumSize(QtCore.QSize(16777215, 5))
        self.progressBar.setStyleSheet(
            "QProgressBar{ color: rgb(255, 255, 255); font:12pt; border-radius:2px; text-align:center; border:none; background-color: rgba(215, 215, 215,100);} \n"
            "QProgressBar:chunk{ border-radius:0px; background: rgba(55, 55, 55, 200);}")
        self.progressBar.setMaximum(1000)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_12.addWidget(self.progressBar)
        self.stopButton = QtWidgets.QPushButton(self.groupBox_201)
        self.stopButton.setMinimumSize(QtCore.QSize(40, 40))
        self.stopButton.setStyleSheet("QPushButton {\n"
                                      "border-style: solid;\n"
                                      "border-width: 0px;\n"
                                      "border-radius: 0px;\n"
                                      "background-color: rgba(223, 223, 223, 0);\n"
                                      "}\n"
                                      "QPushButton::focus{outline: none;}\n"
                                      "QPushButton::hover {\n"
                                      "border-style: solid;\n"
                                      "border-width: 0px;\n"
                                      "border-radius: 0px;\n"
                                      "background-color: rgba(223, 223, 223, 150);}")
        self.stopButton.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/img/icon/终止.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stopButton.setIcon(icon8)
        self.stopButton.setIconSize(QtCore.QSize(30, 30))
        self.stopButton.setObjectName("stopButton")
        self.horizontalLayout_12.addWidget(self.stopButton)
        self.verticalLayout_show.addLayout(self.horizontalLayout_12)
        self.verticalLayout_show.setStretch(1, 1)
        self.horizontalLayout_7.addWidget(self.groupBox_201)
        self.verticalLayout_main_2.addLayout(self.horizontalLayout_7)
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_18)
        self.groupBox_4.setMinimumSize(QtCore.QSize(0, 30))
        self.groupBox_4.setMaximumSize(QtCore.QSize(16777215, 30))
        self.groupBox_4.setStyleSheet("#groupBox_4{\n"
                                      "background-color: rgba(75, 75, 75, 200);\n"
                                      "border: 0px solid #42adff;\n"
                                      "border-left: 0px solid rgba(29, 83, 185, 255);\n"
                                      "border-right: 0px solid rgba(29, 83, 185, 255);\n"
                                      "border-top: 1px solid rgba(200, 200, 200,100);\n"
                                      "border-radius:0px;}")
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_10.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.statistic_label = QtWidgets.QLabel(self.groupBox_4)
        self.statistic_label.setMouseTracking(False)
        self.statistic_label.setStyleSheet("QLabel\n"
                                           "{\n"
                                           "    font-size: 24px;\n"
                                           "    font-family: \"Microsoft YaHei\";\n"
                                           "    font-weight: light;\n"
                                           "         border-radius:9px;\n"
                                           "        background:rgba(66, 195, 255, 0);\n"
                                           "color: rgb(218, 218, 218);\n"
                                           "}\n"
                                           "")
        self.statistic_label.setText("")
        self.statistic_label.setObjectName("statistic_label")
        self.horizontalLayout_10.addWidget(self.statistic_label)
        self.verticalLayout_main_2.addWidget(self.groupBox_4)
        self.verticalLayout_main.addWidget(self.groupBox_18)
        mainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "YOLOv8检测界面"))
        self.label_title.setText(_translate("mainWindow", "无人驾驶视觉环境感知多目标检测系统"))
        self.label_setting.setText(_translate("mainWindow", "设置"))
        self.label_model.setText(_translate("mainWindow", "模型"))
        self.comboBox.setItemText(0, _translate("mainWindow", "yolov5s.pt"))
        self.comboBox.setItemText(1, _translate("mainWindow", "yolov5m.pt"))
        self.comboBox.setItemText(2, _translate("mainWindow", "yolov5l.pt"))
        self.comboBox.setItemText(3, _translate("mainWindow", "yolov5x.pt"))
        self.label_chose_file.setText(_translate("mainWindow", "选择文件"))
        self.fileButton.setToolTip(_translate("mainWindow", "选择文件"))
        self.label_IoU.setText(_translate("mainWindow", "交并比"))
        self.label_conf.setText(_translate("mainWindow", "置信度"))
        self.label_show.setText(_translate("mainWindow", "展示"))


from MouseLabel import Label_click_Mouse
import apprcc_rc
