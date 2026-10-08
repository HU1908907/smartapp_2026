import sys
import requests

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

    print(fg.BLUE + """
    
╷ ╷╭─╴╭─╴╭─╮╭─╮╭─╮╭─╮╭─╮╭─╮╭─╮╶┬╴   ╭┬╮╭─╴╭╮╷╷ ╷
│╷│├╴ ├╴ ├┬╯├┬╯├─┤├─╯├─╯│ │├┬╯ │    │││├╴ │╰┤│ │
╰┴╯╰─╴╰─╴╵╰╴╵╰╴╵ ╵╵  ╵  ╰─╯╵╰╴ ╵    ╵ ╵╰─╴╵ ╵╰─╯
    
    """)

    print()

    print("=====================")
    print("1. Zelf invullen")
    print("2. Huidige weer in Utrecht")
    print("3. Stoppen")
    print("=====================")

    while True:
        user_input = input("Wat wilt u doen?: ")
        if user_input == "1" or user_input == "Zelf" or user_input == "zelf" or user_input == "Zelf invullen" or user_input == "zelf invullen":

            print("=====================")
            print("Om het programma te stoppen, laat de gegevens leeg en klik enter.")
            print("=====================")

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

        elif user_input == "2" or user_input == "Huidige weer in Utrecht" or user_input == "huidige weer in Utrecht":
            url = "https://geocoding-api.open-meteo.com/v1/search?name=Utrecht&count=10&language=en&format=json"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()

                # coordinaten van utrecht
                latitude = data["results"][0]["latitude"]
                longitude = data["results"][0]["longitude"]

                # url opvragen
                weer_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"
                weer_response = requests.get(weer_url)
                if weer_response.status_code == 200:
                    weer_data = weer_response.json()

                    # current = op dit moment en temperature_2m is de graden wat het NU op dit moment is.
                    temperatuur = weer_data["current"]["temperature_2m"]
                    print("De temperatuur in Utrecht is", temperatuur, "graden.")

        elif user_input == "3" or user_input == "Stoppen" or user_input == "stoppen":
            break
        else:
            print("Kies een van de 3 opties hierboven.")

weerbericht()