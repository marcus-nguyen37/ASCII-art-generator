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

    def print_ascii(self):
        # Prints to terminal

        print(self.to_string())