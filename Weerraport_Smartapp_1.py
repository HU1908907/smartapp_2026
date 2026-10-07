import sys

def vraag_getal(tekst, minimum=None, maximum=None):
    while True:
        antwoord = input(tekst).strip()
        if antwoord == "":
            sys.exit("bye")
        try:
            waarde = float(antwoord)
        except ValueError:
            print("Kies een getal en geen woorden.")
            continue
        if minimum is not None and waarde < minimum:
            print("Te laag. Minimum is", minimum)
            continue
        if maximum is not None and waarde > maximum:
            print("Te hoog. Maximum is", maximum)
            continue
        return waarde


def weerbericht():
    aantal = 8
    dag = 1
    lijst = []

    print("""
    
╷ ╷╭─╴╭─╴╭─╮╭─╮╭─╮╭─╮╭─╮╭─╮╭─╮╶┬╴   ╭┬╮╭─╴╭╮╷╷ ╷
│╷│├╴ ├╴ ├┬╯├┬╯├─┤├─╯├─╯│ │├┬╯ │    │││├╴ │╰┤│ │
╰┴╯╰─╴╰─╴╵╰╴╵╰╴╵ ╵╵  ╵  ╰─╯╵╰╴ ╵    ╵ ╵╰─╴╵ ╵╰─╯
    
    """)
    print("=====================")
    print("Om het programma te stoppen, laat de gegevens leeg en klik enter.")
    print("=====================")


    print()

    while dag <= aantal:
        celsius = vraag_getal(f"Wat is op dag {dag} de temperatuur[C]: ")
        windsnelheid = vraag_getal("Hoe snel waait het in m/s?: ", minimum=0)
        luchtvochtigheid = vraag_getal("Wat is de luchtvochtigheid percentage?: ", minimum=0, maximum=100,)

        fahrenheit = celsius * 1.8 + 32
        print(f"het is {celsius}C ({fahrenheit}F)")

        lijst.append(celsius)

        gevoelstemperatuur = (celsius - luchtvochtigheid / 100 * windsnelheid)
        if gevoelstemperatuur < 0:
            if windsnelheid > 10:
                print("Het is heel koud en het stormt! Verming helemaal aan!")
            elif windsnelheid <= 10:
                print("Het is behoorlijk koud! Verwarming aan op de benedenverdieping!")

        if 0 <= gevoelstemperatuur < 10:
            if windsnelheid < 12:
                print("Het is best koud en het waait; verwarming aan en roosters dicht!")
            elif windsnelheid >= 12:
                print("Het is een beetje koud, elektrische kachel op de benedenverdieping aan!")

        if 10 <= gevoelstemperatuur < 22:
            print("Heerlijk weer, niet te koud of te warm.")

        if gevoelstemperatuur >= 22:
            print("Warm! Airco aan!")

        print("Gem. temp tot nu toe is", sum(lijst) / len(lijst))
        print("==========================================")

        dag += 1
        if dag == aantal:
            break

weerbericht()