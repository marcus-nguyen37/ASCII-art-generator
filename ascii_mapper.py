from PIL import Image
from config import DEFAULT_RAMP

class AsciiMapper:
    """
    Maps grayscale pixels to ASCII characters.
    """

    def __init__(self, ramp: str = DEFAULT_RAMP, reverse: bool = False):
        self.ramp = ramp
        self.ramp_len = len(ramp)
        self.reverse = reverse

    def map_pixel(self, value: int) -> str:
        # Maps a grayscale pixel value (0-255) to ASCII char
        index = value * (self.ramp_len - 1) // 255
        if self.reverse:
            index = self.ramp_len - 1 - index
        return self.ramp[index]

    def map_image(self, image: Image) -> list[list[str]]:
        # Convert entire loaded image to a matrix of ASCII chars

        pixels = list(image.getdata())
        width, height = image.size
        ascii_matrix = []

        for i in range(height):
            row = []
            for j in range(width):
                pixel_value = pixels[i*width + j]
                row.append(self.map_pixel(pixel_value))

            ascii_matrix.append(row)
        
        return ascii_matrix