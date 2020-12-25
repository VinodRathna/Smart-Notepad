from cx_Freeze import *
from cx_Freeze import sys

includefiles = ["icon.ico",'icons2']
excludes = []
packages = []
base = None
if sys.platform == "win32":
    base = "Win32GUI"

shortcut_table = [
    ("DesktopShortcut",  # Shortcut
     "DesktopFolder",  # Directory_
     "Smart Notepad",  # Name
     "TARGETDIR",  # Component_
     "[TARGETDIR]\Smart Notepad.exe",  # Target
     None,  # Arguments
     None,  # Description
     None,  # Hotkey
     None,  # Icon
     None,  # IconIndex
     None,  # ShowCmd
     "TARGETDIR",  # WkDir
     )
]

# Now create the table dictionary
msi_data = {"Shortcut": shortcut_table}

# Change some default MSI options and specify the use of the above defined tables
bdist_msi_options = {'data': msi_data}
setup(
    version="2.5",
    description="Smart Note Pad developed by Konda Sai Sri Vinod Rathna",
    author="Konda Sai Sri Vinod Rathna",
    name="Smart Notepad",
    options={'build_exe': {'include_files': includefiles}, "bdist_msi": bdist_msi_options, },
    executables=[
        Executable(
            script="SmartNote pad.py",
            base=base,
            icon='icon.ico',
        )
    ]
)
