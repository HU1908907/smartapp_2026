import subprocess
import sys
import os

base_dir = os.path.dirname(os.path.abspath(__file__))


print("""

╭─╮╭┬╮╭─╮╭─╮╶┬╴╭─╮╭─╮╭─╮   ╭┬╮╭─╴╭╮╷╷ ╷
╰─╮│││├─┤├┬╯ │ ├─┤├─╯├─╯   │││├╴ │╰┤│ │
╰─╯╵ ╵╵ ╵╵╰╴ ╵ ╵ ╵╵  ╵     ╵ ╵╰─╴╵ ╵╰─╯  
                                                                                                                                              
""")

print()
print("=====================")
print("1. Controller")
print("2. Weer")
print("3. Stoppen")
print("=====================")

while True:

    keuze = input("Wat is je keuze?: ")


    if keuze == "Controller" or keuze == "1":
      subprocess.Popen(
        [sys.executable, "Smart_App_Controller_Smart_App_2.py"],
        cwd=base_dir,
        creationflags=subprocess.CREATE_NEW_CONSOLE
        )


    elif keuze == "Weer" or keuze == "2":
        subprocess.Popen(
        [sys.executable, "Weerraport_Smartapp_1.py"],
        cwd=base_dir,
        creationflags=subprocess.CREATE_NEW_CONSOLE
        )

    elif keuze == "Stoppen" or keuze == "3":
        break

    else:
        print("Kies een van de opties")