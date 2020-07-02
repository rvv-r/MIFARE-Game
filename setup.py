import sys
from cx_Freeze import setup, Executable

build_exe_options = {"includes": ["tkinter"]}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup( 
    name = "HackThisMifare",
    version = "1.0",
    description = "Le jeu pour connaître et exploiter les vulnérabilités du système Mifare",
    options = {"build_exe": {"includes":["tkinter",]}},
    executables = [Executable("main.py", base = base, icon = "image/icone.ico")]
)