from models.wctmp_control_file import WoodchipperTemplatingControlFile as ControlFile
from models.wctmp_token_file import WoodchipperTokenFile as TokenFile
from core.wctmp_control_stack import WoodchipperTemplateControlStack as ControlStack
from utilities.wcutil import WoodchipperNamespace as WCNamespace
import core.constants as C

class WoodchipperTemplateExpander:
    def __init__(self, file_path):
        self.path = file_path
        self.control = ControlFile(self.path)
        self.files = []

    def expand(self):
        control_stack = ControlStack(self.control)
        remaining_content = self.control.load()
        return None

    def save(self):
        for file in self.files:
            file.save()

    def toNamespace(self):
        ns = WCNamespace("extender")
        ns.add(C.KEY.EXPANDER.CONTROL, self.control.toNamespace())
        ns.add(C.KEY.EXPANDER.FILES, [])
        for file in self.files:
            ns.files.append(file.toNamespace())
        return ns


