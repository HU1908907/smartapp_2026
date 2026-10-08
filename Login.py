import subprocess
import sys
import os

# deze code is door Ai gemaakt. Ik kon het niet vinden hoe ik een terminal pop up kreeg.
base_dir = os.path.dirname(os.path.abspath(__file__))

subprocess.Popen(
    [sys.executable, "Main.py"],
    cwd=base_dir,
    creationflags=subprocess.CREATE_NEW_CONSOLE
)