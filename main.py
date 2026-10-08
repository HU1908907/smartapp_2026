import subprocess
import sys
import os
import time



print(""""

╷  ╭─╮╭─╴╷╭╮╷   ╭─╮╭─╴╷ ╷╭─╴╭─╮╭┬╮
│  │ ││╶╮││╰┤   ╰─╮│  ├─┤├╴ ├┬╯│││
╰─╴╰─╯╰─╯╵╵ ╵   ╰─╯╰─╴╵ ╵╰─╴╵╰╴╵ ╵

""")

print()
print("=====================")
print("Vul uw naam en wachtwoord in.")
print("=====================")

def login_systeem():
    with open('login.txt', 'r') as f:
        contents = f.readlines()

        nieuw = []
        for line in contents:
            fields = line.split(",")
            fields[1] = fields[1].rstrip()
            nieuw.append(fields)
        return nieuw

logins = login_systeem()


def login():
    vraag = str(input("Wat is uw gebruikersnaam?: "))
    wachtwoord = str(input("Wat is uw wachtwoord?: "))

    logged_in = False

    for line in logins:
        if line[0] == vraag and logged_in == False:
            if line[1] == wachtwoord:
                logged_in = True

    if logged_in == True:
        time.sleep(1.5)
        print("Ingelogd.")
        print("Hoofd programma wordt geopend.")
        time.sleep(1)
        main()

    else:
        print("Username of wachtwoord verkeerd.")
        login()

def main():
    # deze code is door Ai gemaakt. Ik kon het niet vinden hoe ik een terminal pop up kreeg.
    base_dir = os.path.dirname(os.path.abspath(__file__))

    subprocess.Popen(
        [sys.executable, "Server.py"],
        cwd=base_dir,
        creationflags=subprocess.CREATE_NEW_CONSOLE
            )

login()