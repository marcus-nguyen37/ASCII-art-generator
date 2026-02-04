from config import DEFAULT_WIDTH, DEFAULT_OUTPUT_FILE, ASCII_RAMPS, DEFAULT_RAMP_NAME
from image_processor import ImageProcessor
from ascii_mapper import AsciiMapper
from ascii_renderer import AsciiRenderer

def main():
    # Image path
    path = input("Enter image's path: ").strip('" ')

    # Width
    width_input = input(f"Enter desired width (default={DEFAULT_WIDTH}): ").strip()
    new_width = DEFAULT_WIDTH

    if width_input.isdigit():
        new_width = int(width_input)
    else:
        print(f"Width input is invalid. Defaulting to {DEFAULT_WIDTH} px.\n")
    
    # Ramp type
    print("Available ramps:")
    for name in ASCII_RAMPS:
        print(f" - {name}")
    ramp_input = input(f"Select a ramp (default={DEFAULT_RAMP_NAME}): ").lower().strip()

    # Reverse mapping
    reverse_input = input("Reverse ASCII mapping? (y/n): ").lower().strip()

    # Execution
    processor = ImageProcessor(path)

    try:
        processor.load_image()
    except Exception as e:
        print(e)
        return
    
    processor.resize(new_width)
    processor.grayscale()

    mapper = AsciiMapper(ramp_name=ramp_input, reverse=reverse_input=="y")
    ascii_matrix = mapper.map_image(processor.image)

    renderer = AsciiRenderer(ascii_matrix)
    renderer.print_ascii()
    renderer.save_to_file(DEFAULT_OUTPUT_FILE)
    print(f"\nASCII image saved to {DEFAULT_OUTPUT_FILE}")

if __name__ == "__main__":
    main()
