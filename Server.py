import subprocess
import sys
import os

class fg:
    BLACK   = '\033[30m'
    RED     = '\033[31m'
    GREEN   = '\033[32m'
    YELLOW  = '\033[33m'
    BLUE    = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN    = '\033[36m'
    WHITE   = '\033[37m'
    RESET   = '\033[39m'

base_dir = os.path.dirname(os.path.abspath(__file__))


print(fg.BLUE + """

╭─╮╭┬╮╭─╮╭─╮╶┬╴╭─╮╭─╮╭─╮   ╭┬╮╭─╴╭╮╷╷ ╷
╰─╮│││├─┤├┬╯ │ ├─┤├─╯├─╯   │││├╴ │╰┤│ │
╰─╯╵ ╵╵ ╵╵╰╴ ╵ ╵ ╵╵  ╵     ╵ ╵╰─╴╵ ╵╰─╯  
                                                                                                                                              
""")

print()
print("=====================")
print("1. Controller")
print("2. Weer")
print("3. Blackjack")
print("4. Stoppen")
print("=====================")

while True:

    keuze = input("Wat is je keuze?: ")

    #deze code is zelf geschreven na het zien van de AI code in Main.py en daarna de if statements geexpirimenteert
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

    elif keuze == "Blackjack" or keuze == "3":
        subprocess.Popen(
        [sys.executable, "blackjack.py"],
        cwd=base_dir,
        creationflags=subprocess.CREATE_NEW_CONSOLE
        )

    elif keuze == "Stoppen" or keuze == "4":
        break

    else:
        print("Kies een van de opties")