from config import DEFAULT_WIDTH, DEFAULT_OUTPUT_FILE, ASCII_RAMPS, DEFAULT_RAMP_NAME
from image_processor import ImageProcessor
from ascii_mapper import AsciiMapper
from ascii_renderer import AsciiRenderer

from PyQt6.QtWidgets import QApplication
import sys
from gui import AsciiArtGUI

def main():
    app = QApplication(sys.argv)
    window = AsciiArtGUI()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
