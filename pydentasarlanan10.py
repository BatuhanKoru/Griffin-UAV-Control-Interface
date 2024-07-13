from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)

from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialogButtonBox,
    QGroupBox, QLCDNumber, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QProgressBar,
    QPushButton, QSizePolicy, QTextEdit, QStatusBar, QWidget)
#herzaman ekle1--------------------------
from PySide6.QtMultimedia import QCamera, QMediaCaptureSession, QMediaDevices
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtWebEngineWidgets import QWebEngineView
#herzaman ekle2--------------------------

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1440, 787)
        self.actionGOOGLE = QAction(MainWindow)
        self.actionGOOGLE.setObjectName(u"actionGOOGLE")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(490, 0, 231, 191))
        font = QFont()
        font.setFamilies([u"Helvetica"])
        font.setBold(True)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setAutoFillBackground(True)
        self.label_9 = QLabel(self.groupBox_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 40, 81, 16))
        font1 = QFont()
        font1.setFamilies([u"Helvetica"])
        font1.setPointSize(15)
        font1.setBold(True)
        self.label_9.setFont(font1)
        self.lcdNumber_5 = QLCDNumber(self.groupBox_3)
        self.lcdNumber_5.setObjectName(u"lcdNumber_5")
        self.lcdNumber_5.setGeometry(QRect(110, 30, 111, 31))
        self.lcdNumber_6 = QLCDNumber(self.groupBox_3)
        self.lcdNumber_6.setObjectName(u"lcdNumber_6")
        self.lcdNumber_6.setGeometry(QRect(110, 70, 111, 31))
        self.label_10 = QLabel(self.groupBox_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(10, 80, 81, 16))
        self.label_10.setFont(font1)
        self.lcdNumber_7 = QLCDNumber(self.groupBox_3)
        self.lcdNumber_7.setObjectName(u"lcdNumber_7")
        self.lcdNumber_7.setGeometry(QRect(110, 110, 111, 31))
        self.label_11 = QLabel(self.groupBox_3)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(10, 120, 91, 16))
        self.label_11.setFont(font1)
        self.lcdNumber_8 = QLCDNumber(self.groupBox_3)
        self.lcdNumber_8.setObjectName(u"lcdNumber_8")
        self.lcdNumber_8.setGeometry(QRect(110, 150, 111, 31))
        self.label_12 = QLabel(self.groupBox_3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(10, 160, 81, 16))
        self.label_12.setFont(font1)
        self.groupBox_5 = QGroupBox(self.centralwidget)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(10, 200, 711, 371))
        self.groupBox_5.setFont(font)
        self.groupBox_5.setAutoFillBackground(True)

        # EKLENDİ--------------------------
        self.videoWidget = QVideoWidget(self.groupBox_5)
        self.videoWidget.setGeometry(QRect(10, 30, 691, 331))
        # EKLENDİ--------------------------

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 0, 231, 191))
        self.groupBox.setFont(font)
        self.groupBox.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.groupBox.setAutoFillBackground(True)
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 30, 71, 16))
        self.label_2.setFont(font1)
        self.comboBox_2 = QComboBox(self.groupBox)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(90, 20, 131, 41))
        self.comboBox_2.setFont(font1)
        self.comboBox_3 = QComboBox(self.groupBox)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setGeometry(QRect(90, 60, 131, 41))
        self.comboBox_3.setFont(font1)
        self.lcdNumber = QLCDNumber(self.groupBox)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setGeometry(QRect(100, 100, 111, 31))
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 70, 61, 16))
        self.label_3.setFont(font1)
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 110, 81, 16))
        self.label_4.setFont(font1)

# tamam butonuna basınca text editte yazı yazdırma
        self.pushButton_2 = QPushButton(self.groupBox)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(70, 150, 100, 32))
        self.pushButton_2.clicked.connect(self.yazı)
# tamam butonuna basınca text editte yazı yazdırma

        font2 = QFont()
        font2.setFamilies([u"Helvetica"])
        font2.setPointSize(12)
        font2.setBold(True)
        self.pushButton_2.setFont(font2)
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(250, 0, 231, 191))
        self.groupBox_2.setFont(font)
        self.groupBox_2.setAutoFillBackground(True)
        self.lcdNumber_2 = QLCDNumber(self.groupBox_2)
        self.lcdNumber_2.setObjectName(u"lcdNumber_2")
        self.lcdNumber_2.setGeometry(QRect(110, 60, 111, 31))
        self.lcdNumber_3 = QLCDNumber(self.groupBox_2)
        self.lcdNumber_3.setObjectName(u"lcdNumber_3")
        self.lcdNumber_3.setGeometry(QRect(110, 100, 111, 31))
        self.lcdNumber_4 = QLCDNumber(self.groupBox_2)
        self.lcdNumber_4.setObjectName(u"lcdNumber_4")
        self.lcdNumber_4.setGeometry(QRect(110, 140, 111, 31))
        self.progressBar = QProgressBar(self.groupBox_2)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(110, 20, 111, 31))
        self.progressBar.setValue(24)
        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 30, 101, 16))
        self.label_5.setFont(font1)
        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 70, 101, 16))
        self.label_6.setFont(font1)
        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 110, 101, 16))
        self.label_7.setFont(font1)
        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 150, 101, 16))
        self.label_8.setFont(font1)
        self.groupBox_6 = QGroupBox(self.centralwidget)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setGeometry(QRect(730, 0, 701, 571))
        self.groupBox_6.setFont(font)
        self.groupBox_6.setAutoFillBackground(True)
        self.webEngineView = QWebEngineView(self.groupBox_6)
        self.webEngineView.setObjectName(u"webEngineView")
        self.webEngineView.setGeometry(QRect(0, 20, 701, 551))
        self.webEngineView.setUrl(QUrl(u"about:blank"))
        self.groupBox_4 = QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(730, 580, 711, 91))
        self.groupBox_4.setFont(font)
        self.groupBox_4.setAutoFillBackground(True)
        self.label_13 = QLabel(self.groupBox_4)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(10, 50, 81, 16))
        self.label_13.setFont(font1)
        self.lcdNumber_9 = QLCDNumber(self.groupBox_4)
        self.lcdNumber_9.setObjectName(u"lcdNumber_9")
        self.lcdNumber_9.setGeometry(QRect(110, 40, 111, 31))
        self.lcdNumber_10 = QLCDNumber(self.groupBox_4)
        self.lcdNumber_10.setObjectName(u"lcdNumber_10")
        self.lcdNumber_10.setGeometry(QRect(350, 40, 111, 31))
        self.label_14 = QLabel(self.groupBox_4)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(250, 50, 81, 16))
        self.label_14.setFont(font1)
        self.label_15 = QLabel(self.groupBox_4)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(480, 50, 91, 16))
        self.label_15.setFont(font1)
        self.lcdNumber_11 = QLCDNumber(self.groupBox_4)
        self.lcdNumber_11.setObjectName(u"lcdNumber_11")
        self.lcdNumber_11.setGeometry(QRect(580, 40, 111, 31))
        self.groupBox_7 = QGroupBox(self.centralwidget)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setGeometry(QRect(10, 580, 711, 91))
        self.groupBox_7.setFont(font)
        self.groupBox_7.setAutoFillBackground(True)
        self.label_16 = QLabel(self.groupBox_7)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(10, 50, 81, 16))
        self.label_16.setFont(font1)
        self.lineEdit = QLineEdit(self.groupBox_7)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(100, 40, 201, 31))
        self.label_17 = QLabel(self.groupBox_7)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(320, 50, 58, 16))
        self.label_17.setFont(font1)
        self.lineEdit_2 = QLineEdit(self.groupBox_7)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(370, 40, 201, 31))
        self.pushButton = QPushButton(self.groupBox_7)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(580, 40, 111, 32))
        self.buttonBox = QDialogButtonBox(self.centralwidget)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(10, 690, 341, 32))

        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

#tamam butonuna basınca text editte yazı yazdırma
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(810, 673, 211, 61))
#tamam butonuna basınca text editte yazı yazdırma

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1440, 24))

        #eklendi1--------------------------
        self.menuCamera = QMenu(self.menubar)
        self.menuCamera.setObjectName("menuCamera")
        #eklendi1--------------------------


        # Yeni grup kutusu (Bağlantı Bilgileri)---------------------------

        self.groupBox_7 = QGroupBox(self.centralwidget)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setGeometry(QRect(10, 580, 711, 91))
        self.groupBox_7.setFont(font)
        self.groupBox_7.setAutoFillBackground(True)
        self.groupBox_7.setTitle("VERİTABANI BAĞLANTISI")

        self.label_ip = QLabel(self.groupBox_7)
        self.label_ip.setObjectName(u"label_ip")
        self.label_ip.setGeometry(QRect(10, 50, 81, 16))
        self.label_ip.setFont(font1)
        self.label_ip.setText("IP ADRESİ:")

        self.lineEdit_ip = QLineEdit(self.groupBox_7)
        self.lineEdit_ip.setObjectName(u"lineEdit_ip")
        self.lineEdit_ip.setGeometry(QRect(100, 40, 201, 31))

        self.label_port = QLabel(self.groupBox_7)
        self.label_port.setObjectName(u"label_port")
        self.label_port.setGeometry(QRect(320, 50, 58, 16))
        self.label_port.setFont(font1)
        self.label_port.setText("PORT:")

        self.lineEdit_port = QLineEdit(self.groupBox_7)
        self.lineEdit_port.setObjectName(u"lineEdit_port")
        self.lineEdit_port.setGeometry(QRect(370, 40, 201, 30))

        self.button_connect = QPushButton(self.groupBox_7)
        self.button_connect.setObjectName(u"button_connect")
        self.button_connect.setGeometry(QRect(590, 40, 111, 32))
        self.button_connect.setText("Bağlan")

        self.label_status = QLabel(self.groupBox_7)
        self.label_status.setObjectName(u"label_status")
        self.label_status.setGeometry(QRect(560, 25, 150, 16))
        self.label_status.setFont(font1)
        self.label_status.setText("Durum: Bağlı Değil")

# eklendi---------------------------

        self.menuveritaban = QMenu(self.menubar)
        self.menuveritaban.setObjectName(u"menuveritaban")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuveritaban.menuAction())
        self.menuveritaban.addAction(self.actionGOOGLE)
        self.menuveritaban.addSeparator()
#eklendi---------------------------
        self.menubar.addAction(self.menuCamera.menuAction())
        self.menuCamera.addAction(self.actionGOOGLE)
#eklendi---------------------------
        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
        self.setup_camera()
    # setupUi

#eklendi---------------------------
    def setup_camera(self):
        self.camera = QCamera(QMediaDevices.defaultVideoInput())
        self.capture_session = QMediaCaptureSession()
        self.capture_session.setCamera(self.camera)
        self.capture_session.setVideoOutput(self.videoWidget)
        self.camera.start()

# eklendi---------------------------
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"GRIFFIN YER KONTROL İSTASYONU KULLANICI ARAYÜZÜ", None))
        self.actionGOOGLE.setText(QCoreApplication.translate("MainWindow", u"GOOGLE", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"HEDEF B\u0130LG\u0130LER\u0130", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"MERKEZ X:", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"MERKEZ Y:", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Y\u00dcKSEKL\u0130K:", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"GEN\u0130\u015eL\u0130K:", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"KAMERA G\u00d6R\u00dcNT\u00dcS\u00dc", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"GENEL DURUM", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"MOD:", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"ARM", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"DISEABLE", None))

        self.comboBox_3.setItemText(0, QCoreApplication.translate("MainWindow", u"OTOMAT\u0130K", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("MainWindow", u"MANUEL", None))

        self.label_3.setText(QCoreApplication.translate("MainWindow", u"MOTOR:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"TAKIM NO:", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"TAMAM", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"U\u00c7AK VER\u0130LER\u0130", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"P\u0130L Y\u00dcZDES\u0130:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Y\u00dcKSEKL\u0130K:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"HIZ (m/s):", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"K\u0130TLENME:", None))
#eklendi---------------------------
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", "KAMERA GÖRÜNTÜSÜ", None))
#eklendi---------------------------
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"HAR\u0130TA ve RAK\u0130P ARA\u00c7LARIN KONUMLARI", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"U\u00c7AK KONUM B\u0130LG\u0130LER\u0130", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"ENLEM:", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"BOYLAM:", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"GPS SAAT\u0130:", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"VER\u0130TABANI BA\u011eLANTISI", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"IP ADRES\u0130:", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"PORT:", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"BA\u011eLAN", None))
        self.menuveritaban.setTitle(QCoreApplication.translate("MainWindow", u"Veri Taban\u0131 Ba\u011flant\u0131s\u0131", None))
#eklendi---------------------------
        self.menuCamera.setTitle(QCoreApplication.translate("MainWindow", "Camera", None))

    def connect_to_server(self):
        ip_address = self.lineEdit_ip.text()
        port = self.lineEdit_port.text()
        # Burada sunucuya bağlanma kodunu ekleyin
        # Örneğin: socket.connect((ip_address, int(port)))
        self.label_status.setText("Durum: Bağlandı")

# tamam butonuna basınca text editte yazı yazdırma
    def yazı(self):

        self.textEdit.append("buraya yaz voyn")

#eklendi---------------------------