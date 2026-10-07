import subprocess
import sys
import os

base_dir = os.path.dirname(os.path.abspath(__file__))

subprocess.Popen(
    [sys.executable, "Server.py"],
        cwd=base_dir,
        creationflags=subprocess.CREATE_NEW_CONSOLE
)