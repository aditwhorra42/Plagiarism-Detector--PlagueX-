import PlagueX_Main
import os
import pydoc


def show_exception_and_exit(exc_type, exc_value, tb):
    import traceback
    traceback.print_exception(exc_type, exc_value, tb)
    input("Press key to exit.")
    sys.exit(-1)

import sys
sys.excepthook = show_exception_and_exit
sys.path.append(os.getcwd())

PlagueX_Main.PlagueX()
