from wctmp_file import WoodchipperTemplatingFile as WCFile

class WoodchipperTemplatingControlFile(WCFile):
    def __init__(self, file_path):
        WCFile.__init__(self, file_path)
        self.draft = ""

    def add(self, text):
        self.draft += text

    def save(self):
        with (open(self.path, 'w')
              as text_file):
            text_file.write(self.draft)