from types import SimpleNamespace

from wcutil import WoodchipperNamespace as WCNamespace
import constants as C

class WoodchipperController:
    def __init__(self):
        self.request = None
        self.data = None
        self.affect_file_system = True
        self.results = WCNamespace("ControllerResults")

    def process_request(self, process_request):
        self.request = process_request
        if self.request.debug:
            self.affect_file_system = False
        self._initialize_results()
        self.data = None
        self.results.add("data", self.data)

    def _initialize_results(self):
        self.results.add("debug", self.request.debug)
        self.results.add("path", self.request.path)
        self.results.add("files", [])

