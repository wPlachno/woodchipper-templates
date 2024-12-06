import pathlib

class WoodchipperTemplatingFile:
    def __init__(self, file_path):
        self.path = pathlib.Path(file_path)
        self.content = ""

    def name(self):
        return self.path.name

    def exists(self):
        return self.path.exists()

    def load(self):
        with (open(self.path, 'r')
              as text_file):
            self.content = text_file.read()
        return self.content

    def save(self):
        with (open(self.path, 'w')
              as text_file):
            text_file.write(self.content)

    def add(self, text):
        self.content += text