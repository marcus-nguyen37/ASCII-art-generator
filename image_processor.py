from PIL import Image

from config import CHAR_SIZE_RATIO

class ImageProcessor:
    """
    Handles loading, resizing and grayscaling images.
    """

    def __init__(self, path: str):
        self.path = path
        self.image = None
    
    def load_image(self):
        # Opens image and stores in self.image  

        try:
            self.image = Image.open(self.path)
        except:
            print("Cannot load image. Path might be invalid, or error with opening file.")

    def resize(self, new_width: int = 150):
        # Resizes loaded image and correcting aspect ratio in accordance with ASCII character height

        if self.image is None:
            raise ValueError("No image loaded to resize. Please load image first.")
        
        width, height = self.image.size
        aspect_ratio = height / width
        new_height = int(new_width * aspect_ratio * CHAR_SIZE_RATIO)
        self.image = self.image.resize((new_width, new_height))

    def grayscale(self):
        # Converts loaded image to grayscale

        if self.image is None:
            raise ValueError("No image loaded to grayscale.")
        
        self.image = self.image.convert('L')