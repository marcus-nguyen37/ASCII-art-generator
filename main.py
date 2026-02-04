from PIL import Image

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

    def resize(self, new_width: int = 100):
        # Resizes loaded image and correcting aspect ratio in accordance with ASCII character height

        if self.image is None:
            raise ValueError("No image loaded to resize. Please load image first.")
        
        width, height = self.image.size
        aspect_ratio = height / width
        new_height = int(new_width * aspect_ratio * 0.4) # adjusting for char height. Replace 0.55 with non-magical variable
        self.image = self.image.resize((new_width, new_height))

    def grayscale(self):
        # Converts loaded image to grayscale

        if self.image is None:
            raise ValueError("No image loaded to grayscale.")
        
        self.image = self.image.convert('L')

class AsciiMapper:
    """
    Maps grayscale pixels to ASCII characters.
    """

    def __init__(self, ramp: str = '@#%*+=-:. '):
        self.ramp = ramp
        self.ramp_len = len(ramp)

    def map_pixel(self, value: int) -> str:
        # Maps a grayscale pixel value (0-255) to ASCII char
        index = value * (self.ramp_len - 1) // 255
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

class AsciiRenderer:
    """
    Handles formatting and outputting of ASCII art.
    """

    def __init__(self, ascii_matrix: list[list[str]]):
        self.ascii_matrix = ascii_matrix
        self.ascii_string = None

    def to_string(self) -> str:
        # Converts ASCII matrix to a single string with newlines

        if self.ascii_string is None:
            rows = ["".join(row) for row in self.ascii_matrix]
            return "\n".join(rows)
        
        return self.ascii_string
        
    def save_to_file(self, filename: str):
        # Writes the ASCII single-string to a text file

        with open(filename, 'w', encoding='utf-8') as file:
            file.write(self.to_string())
            print("Saved ASCII string to file.")

    def print_ascii(self):
        # Prints to terminal
        
        print(self.to_string())

def main():
    path = input("Enter image's path: ").strip('" ')
    width_input = input("Enter desired width (default=100): ").strip()
    new_width = 100

    if width_input.isdigit():
        new_width = int(width_input)
    else:
        print("Width input is invalid. Defaulting to 100 px.")

    processor = ImageProcessor(path)

    try:
        processor.load_image()
    except Exception as e:
        print(e)
        return
    
    processor.resize(new_width)
    processor.grayscale()

    mapper = AsciiMapper()
    ascii_matrix = mapper.map_image(processor.image)

    renderer = AsciiRenderer(ascii_matrix)
    renderer.print_ascii()
    renderer.save_to_file("ascii_image.txt")
    print("\nASCII images saved to ascii_image.txt")

if __name__ == "__main__":
    main()
