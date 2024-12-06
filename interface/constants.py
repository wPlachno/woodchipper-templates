from utilities import wcconstants as S
from utilities.wcconstants import COLOR_DEFAULT


# Our application uses WoodchipperNamespaces for data transfer
# between the CLI and the Controller. These constants represent
# the keys added to the request (CLI->Cntl) and results (Cntl->CLI)
# namespaces.
class KEY:
    class REQUEST:
        MODE = "mode"
        DEBUG = "debug"
        PATH = "path"
        DATA = "data"

    class RESULTS:
        HANDLER = "handler"
        SUCCESS = "success"
        ERROR = "error"
        FILES = "files"

    class FILE:
        NAME = "name"
        PATH = "path"
        CONTENT = "content"

# MODE represents the operation represented in the request passed to the Controller
class MODE:
    NONE = "none"
    TEST = "test"
    NORMAL = "normal"

class TOKEN:
    START = '@{'
    DELIMITER = '|'
    TEXT = "}{{"
    END = '}}'


# In this implementation of the CLI, we associate certain colors with certain constructs.
# Note that this is based off of the profile colors presented by the wcutil construct
class COLOR:
    NAME = S.COLOR_SUPER
    PATH = S.COLOR_SIBLING
    CONTENT = S.COLOR_OPTION
    SUCCESS = S.COLOR_GREEN
    ERROR = S.COLOR_RED
    WARNING = S.COLOR_DARK_YELLOW
    RESET = S.COLOR_DEFAULT


def clr(text, color):
    return color + text + COLOR_DEFAULT

class TAG: # .format() required

    class FILE:
        NAME = clr(S.OP0, COLOR.NAME)
        PATH = clr(S.OP1, COLOR.PATH)
        CONTENT = clr(S.OP2, COLOR.CONTENT)

class ERROR:
    class COULD_NOT_RESOLVE:
        TOOLKIT = f"There exists no {clr("Toolkit", COLOR.SUCCESS)} named '{S.OP0}'." # (target_toolkit)

class OUT:
    ERROR = clr("ERROR: ", COLOR.ERROR)+S.OP0+S.NL
    class FILE:
            NO_FILES = "No "+clr("files", COLOR.NAME)+S.EL
            LIST_ITEM = [
                S.EMPTY,                        # V0: SILENT
                S.OP0+S.CD,                     # V1: RESULTS_ONLY, will need to remove the last comma
                S.DH+TAG.FILE.NAME+S.NL,     # V2: NORMAL
                S.DH+TAG.FILE.PATH]     # V3: DEBUG