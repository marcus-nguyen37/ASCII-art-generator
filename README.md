# ASCII-art-generator
Image to ASCII art generator. Done in Python, using PyQt6 for GUI.

## Features

- **Image Selection**: Select any image (.png, .jpg, etc.) from File Explorer to be used.
- **Adjustable Width**: Desired output width (in characters). Note that aspect ratio will always be preserved, so the GUI doesn't ask for height.
- **Different Palettes & Inverse Mapping**: Different ASCII character maps to output your image as! And also option to inverse the ASCII mapping.
- **User-Friendly GUI**: Easily comprehensible GUI made from PyQT6.

## Basic installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/marcus-nguyen37/ascii-art-generator.git
   cd ascii-art-generator
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv .venv
   .venv\Scripts\Activate.ps1  # On Windows PowerShell
   # or
   source .venv/bin/activate  # On Linux/macOS
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Requirements

- **Python 3.10+**
- **PyQt6** - For GUI
- **PIL (pillow)** - For image processing

Please see `requirements.txt` for exact versions needed.

## Future Enhancements That I Might Add...

- [ ] Implement functionality to ASCII-ify gifs or videos.
