from config import DEFAULT_WIDTH, DEFAULT_OUTPUT_FILE
from image_processor import ImageProcessor
from ascii_mapper import AsciiMapper
from ascii_renderer import AsciiRenderer

def main():
    path = input("Enter image's path: ").strip('" ')
    width_input = input(f"Enter desired width (default={DEFAULT_WIDTH}): ").strip()
    new_width = DEFAULT_WIDTH

    if width_input.isdigit():
        new_width = int(width_input)
    else:
        print(f"Width input is invalid. Defaulting to {DEFAULT_WIDTH} px.")

    reverse_input = input("Reverse ASCII mapping? (y/n): ").lower().strip()

    processor = ImageProcessor(path)

    try:
        processor.load_image()
    except Exception as e:
        print(e)
        return
    
    processor.resize(new_width)
    processor.grayscale()

    mapper = AsciiMapper(reverse=reverse_input=="y")
    ascii_matrix = mapper.map_image(processor.image)

    renderer = AsciiRenderer(ascii_matrix)
    renderer.print_ascii()
    renderer.save_to_file(DEFAULT_OUTPUT_FILE)
    print(f"\nASCII image saved to {DEFAULT_OUTPUT_FILE}")

if __name__ == "__main__":
    main()
