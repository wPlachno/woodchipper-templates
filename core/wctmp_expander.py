from models.wctmp_control_file import WoodchipperTemplatingControlFile as ControlFile
from models.wctmp_token_file import WoodchipperTokenFile as TokenFile
from wctmp_control_stack import WoodchipperTemplateControlStack as ControlStack

class WoodchipperTemplateExpander:
    def __init__(self, file_path):
        self.path = file_path
        self.control = ControlFile(self.path)
        self.files = [self.control]

    def expand(self):
        control_stack = ControlStack(self.control)
        remaining_content = self.control.load()

    def save(self):
        for file in self.files:
            file.save()
