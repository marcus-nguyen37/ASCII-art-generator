from PIL import Image
from config import ASCII_RAMPS, DEFAULT_RAMP_NAME

class AsciiMapper:
    """
    Maps grayscale pixels to ASCII characters using selected ramp.
    """

    def __init__(self, ramp_name: str = DEFAULT_RAMP_NAME, reverse: bool = False):
        if ramp_name not in ASCII_RAMPS:
            print(f"Ramp '{ramp_name}' not found. Defaulting to {DEFAULT_RAMP_NAME}.")
            ramp_name = DEFAULT_RAMP_NAME

        self.ramp_name = ramp_name
        self.ramp = ASCII_RAMPS[ramp_name]
        self.ramp_len = len(self.ramp)
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
            row = [self.map_pixel(pixels[i*width + j]) for j in range(width)]
            ascii_matrix.append(row)
        
        return ascii_matrix