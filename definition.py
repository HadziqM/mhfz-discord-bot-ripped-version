import os
import sys

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(ROOT_DIR, 'database.ini')
ICON_PATH = os.path.join(ROOT_DIR, 'icon')
SAVE_PATH = os.path.join(ROOT_DIR, 'save')
UPLOAD_PATH = os.path.join(ROOT_DIR, 'up')
MISC_PATH = os.path.join(ROOT_DIR, 'misc')
COG_PATH = os.path.join(ROOT_DIR, 'cogs')

sys.path.insert(0, COG_PATH)
