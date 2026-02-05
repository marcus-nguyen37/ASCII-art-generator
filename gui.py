from config import *
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QFileDialog,
    QComboBox,
    QCheckBox,
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QPlainTextEdit,
    QPushButton,
    QLabel,
    QSpinBox
)

from image_processor import ImageProcessor
from ascii_mapper import AsciiMapper
from ascii_renderer import AsciiRenderer

class AsciiArtGUI(QMainWindow):
    def __init__(self):
        super().__init__()

        # Setting up window
        self.setWindowTitle("ASCII Art Generator")
        self.resize(1000, 600)

        self.image_path = None
        self.ascii_text = ""

        self.setup_gui()

    def setup_gui(self):
        # Sets up entire GUI
        
        # Setting main widget window
        window = QWidget()
        self.setCentralWidget(window)

        # Sets horizontal layout for window
        main_layout = QHBoxLayout(window)
        
        # Left side: ASCII display
        self.ascii_display = QPlainTextEdit()
        self.ascii_display.setReadOnly(True)
        self.ascii_display.setFont(QFont("Courier New", 5))
        # self.ascii_display.setFontFamily("Courier New")?
        self.ascii_display.setPlaceholderText("ASCII output will appear here...")
        main_layout.addWidget(self.ascii_display, stretch=3)

        # Right side: Controls panel
        controls_layout = QVBoxLayout()
        main_layout.addLayout(controls_layout, stretch=1)

        # Select image button
        select_image_button = QPushButton("Select Image")
        select_image_button.clicked.connect(self.select_image)
        self.image_label = QLabel("No image selected.")
        # Maybe set font and font size as well?
        self.image_label.setWordWrap(True)

        controls_layout.addWidget(select_image_button)
        controls_layout.addWidget(self.image_label)

        # Width input
        self.width_input = QSpinBox()
        self.width_input.setRange(20, 500)
        self.width_input.setValue(DEFAULT_WIDTH)
        self.width_input.setPrefix("Width: ")

        controls_layout.addWidget(self.width_input)

        # Ramp selection + reversed ramp checkbox
        ramp_layout = QHBoxLayout()

        self.ramp_select = QComboBox()
        self.ramp_select.addItems(ASCII_RAMPS.keys())

        self.reverse_checkbox = QCheckBox("Reverse ramp")

        ramp_layout.addWidget(self.ramp_select)
        ramp_layout.addWidget(self.reverse_checkbox)

        controls_layout.addLayout(ramp_layout)

        # Generate button
        generate_button = QPushButton("Generate!")
        generate_button.clicked.connect(self.generate_ascii)
        # self.generate_button.setFixedHeight(40)

        controls_layout.addWidget(generate_button)

        # Save & copy buttons
        save_copy_buttons_layout = QHBoxLayout()

        save_button = QPushButton("💾")
        save_button.clicked.connect(self.save_ascii)
        copy_button = QPushButton("📋")
        copy_button.clicked.connect(self.copy_ascii)
        

        save_copy_buttons_layout.addWidget(save_button)
        save_copy_buttons_layout.addWidget(copy_button)

        controls_layout.addLayout(save_copy_buttons_layout)

        # Push everything up, leave space at bottom
        controls_layout.addStretch()


    def select_image(self):
        path, _ = QFileDialog.getOpenFileName(
            self,
            "Select Image",
            "",
            "Images (*.png *.jpg *.jpeg *.bmp)"
        )

        if path:
            self.image_path = path
            self.image_label.setText(path.split('/')[-1]) # Getting image name
    
    def generate_ascii(self):
        if not self.image_path:
            self.ascii_display.setPlainText("No image selected.")
            return

        # Collecting all inputs
        width = self.width_input.value()
        ramp_name = self.ramp_select.currentText()
        reverse = self.reverse_checkbox.isChecked()

        try:
            processor = ImageProcessor(self.image_path)
            processor.load_image()
            processor.resize(width)
            processor.grayscale()

            mapper = AsciiMapper(ramp_name=ramp_name, reverse=reverse)
            ascii_matrix = mapper.map_image(processor.image)

            renderer = AsciiRenderer(ascii_matrix)
            self.ascii_text = renderer.to_string()

            self.ascii_display.setPlainText(self.ascii_text)

        except Exception as e:
            self.ascii_display.setPlainText(str(e))
        
    def save_ascii(self):
        pass

    def copy_ascii(self):
        pass

