
# https://stackoverflow.com/questions/16981921/relative-imports-in-python-3
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(SCRIPT_DIR + "/../..")
