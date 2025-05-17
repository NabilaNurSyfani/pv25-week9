import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QTextEdit,
    QMenuBar, QAction, QFileDialog, QFontDialog, QTabWidget,
    QInputDialog
)
from PyQt5.QtGui import QFont, QCursor
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Week 9 - QDialog, QTabWidget & MenuBar")
        self.setGeometry(200, 100, 600, 300)
        self.current_font = QFont()
        self.label_style = """
            background-color: white;
            font-family: Helvetica, sans-serif;
            border: 2px solid green;
            padding: 5px;
            font-size: 14px;
        """
        self.initUI()

    def initUI(self):
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)
    
        # Tab 1: Input Nama
        self.input_tab = QWidget()
        input_layout = QVBoxLayout()

        self.name_input = QLabel("Input Nama")
        self.name_input.setAlignment(Qt.AlignCenter)
        self.name_input.setStyleSheet(self.label_style)
        self.name_display = QLabel("Nama:")

        input_layout.addWidget(self.name_input)
        input_layout.addSpacing(40)
        input_layout.addWidget(self.name_display)
        input_layout.addStretch()
        self.input_tab.setLayout(input_layout)

        # Tab 2: Pilih Font 
        self.font_tab = QWidget()
        font_layout = QVBoxLayout()

        self.font_button = QLabel("Pilih Font")
        self.font_button.setAlignment(Qt.AlignCenter)
        self.font_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.font_button.setStyleSheet(self.label_style + "color: black;")
        self.font_button.mousePressEvent = self.pilih_font 
        self.font_static_label = QLabel("Nama:")
        self.font_static_label.setFont(QFont())
        self.font_dynamic_label = QLabel("")
        self.font_dynamic_label.setFont(self.current_font)

        font_layout.addWidget(self.font_button)
        font_layout.addSpacing(40)
        font_layout.addWidget(self.font_static_label)
        font_layout.addWidget(self.font_dynamic_label)
        font_layout.addStretch()
        self.font_tab.setLayout(font_layout)

        # Tab 3: Buka File
        self.file_tab = QWidget()
        file_layout = QVBoxLayout()

        self.filename_label = QLabel("Buka File .txt")
        self.filename_label.setStyleSheet(self.label_style)
        self.filename_label.setAlignment(Qt.AlignCenter)
        self.file_content = QTextEdit()
        self.file_content.setReadOnly(True)

        file_layout.addWidget(self.filename_label)
        file_layout.addWidget(self.file_content)
        file_layout.addStretch()
        self.file_tab.setLayout(file_layout)

        # Tambahkan tab
        self.tabs.addTab(self.input_tab, "Input Nama")
        self.tabs.addTab(self.font_tab, "Pilih Font")
        self.tabs.addTab(self.file_tab, "Buka File")

        # Menu Bar
        menubar = self.menuBar()
        file_menu = menubar.addMenu("File")
        keluar_action = QAction("Keluar", self)
        keluar_action.triggered.connect(self.close)
        file_menu.addAction(keluar_action)

        fitur_menu = menubar.addMenu("Fitur")
        fitur_input = QAction("Input Nama", self)
        fitur_input.triggered.connect(self.input_nama)
        fitur_font = QAction("Pilih Font", self)
        fitur_font.triggered.connect(lambda: self.pilih_font(None))
        fitur_file = QAction("Buka File", self)
        fitur_file.triggered.connect(self.buka_file)
        fitur_menu.addAction(fitur_input)
        fitur_menu.addAction(fitur_font)
        fitur_menu.addAction(fitur_file)

    def input_nama(self):
        self.tabs.setCurrentIndex(0) 
        nama, ok = QInputDialog.getText(self, "Masukkan Nama", "Nama:")
        if ok and nama:
            self.name_display.setText(f"Nama: {nama}")
            self.font_dynamic_label.setText(nama)

    def pilih_font(self, event):  
        self.tabs.setCurrentIndex(1) 
        font, ok = QFontDialog.getFont(self.current_font, self, "Pilih Font")
        if ok:
            self.current_font = font
            self.font_dynamic_label.setFont(font)

    def buka_file(self):
        self.tabs.setCurrentIndex(2) 
        fname, _ = QFileDialog.getOpenFileName(self, "Buka File", "", "Text Files (*.txt);;All Files (*)")
        if fname:
            try:
                with open(fname, 'r', encoding='utf-8') as f:
                    content = f.read()
                    self.file_content.setText(content)
            except Exception as e:
                self.file_content.setText(f"Gagal membuka file: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())