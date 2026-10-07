def aantal_dagen(inputFile):

    #Leest het invoer van het bestand en de "with" zorgt ervoor dat het bestand ook weer sluit
    with open(inputFile, "r", encoding="utf-8") as f:
        lines = f.readlines()

    #het aantal lijnen min -1 omdat we de kolomnamen niet meetellen
    aantal = len(lines) -1
    return aantal

def auto_bereken(inputFile, outputFile):

    # Leest het invoer van het bestand en de "with" zorgt ervoor dat het bestand ook weer sluit
    with open(inputFile, "r", encoding="utf-8") as f:
        lines = f.readlines()
        data = lines[1:]

    # Leest het invoer van het bestand en de "with" zorgt ervoor dat het bestand ook weer sluit
    with open(outputFile, "w", encoding="utf-8") as f:

        #voor elke regel in data
        for regel in data:
            #lege regel overslaan
            if regel.strip() == "":
                continue

            # 10-10-2026 2 4 6 8 -> ["10-10-2026","2", "4", "6", "8" ]
            delen = regel.split()

            datum = str(delen[0])
            numPeople = int(delen[1])
            tempSetpoint = float(delen[2])
            tempOutside = float(delen[3])
            precip = float(delen[4])

            verschil = tempSetpoint - tempOutside

            if verschil >= 20:
                cv = 100
            if verschil >= 10 or verschil < 20:
                cv = 50
            if verschil < 10:
                cv = 0

            #Ventilatie uitrekenen, bij elk persoon erbij +1
            vent = numPeople + 1

            if vent > 4:
                vent = 4

            if precip > 3:
                bewatering = True
            else:
                bewatering = False

            #Uitschrijven naar het nieuwe bestand + ; tussen elke string
            uitvoering = (datum + ";"+ str(cv) + ";" + str(vent) + ";" + str(bewatering) + "\n")

            f.write(uitvoering)

        print("De uitvoeringen zijn uitgevoerd en opgeslagen in", outputFile)

def overwrite_settings(outputFile):

    #proberen het outputfile te openen en als het niet bestaat een foutcode aangeven
    try:
        with open(outputFile, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("Fout: Kies eerst een van de andere 2 opties in het menu.")
        return -1

    #Laat zien welke datums beschikbaar zijn
    print("Beschikbare datums in het bestand:")

    #doe voor elke regel in het bestand het volgende
    for regel in lines:
        regel = regel.strip()
        delen = regel.split(";")
        print("*", delen[0])


    datum = input("Welke datum moet worden aangepast (bv 01-01-2000): ")


    gevonden_datum = False
    regel_nummer = -1

    #elke regel begint met een met een datum en eindigt met een puntkomma ; en dus kun je het makkelijk opzoeken
    for i in range(len(lines)):
        if lines[i].startswith(datum + ";"):
            gevonden_datum = True
            regel_nummer = i
            break

    #als het niet bestaat voort hij dit uit:
    if gevonden_datum == False:
        print("Fout: Deze datum bestaat niet.")
        return -1

    #huidige regel uit het bestand halen
    huidige_regel = lines[regel_nummer].strip()

    #10-10-2026;50;3;True -> ["10-10-2026", "50", "3", "True"] alleen bij een (;) splitten
    delen = huidige_regel.split(";")

    huidige_cv = delen[1]
    huidige_vent = delen[2]
    huidige_bewatering = delen[3]

    print("=====================")
    print("1: CV ketel")
    print("2: Ventilatie")
    print("3: Bewatering")
    print("=====================")

    systeem_aanpassing = input("Welke van de bovenstaande wilt u aanpassen?: ")

    #CV ketal aanpassing
    if systeem_aanpassing == "1":
        cv_waarde = input("Kies een getal tussen de 0-100: ")

        #cv_waarde omzetten naar een geheel getal of int dus geen float
        try:
            nieuwe_cv_waarde = int(cv_waarde)
        except ValueError:
            print("Fout: Kies een geheel getal")
            return -3

        #De cv waarde MOET tussen de 0 en 100 liggen anders foutcode
        if nieuwe_cv_waarde < 0 or nieuwe_cv_waarde > 100:
            print("Fout: de CV-waarde moet tussen 0 en 100 liggen.")
            return -3

        #Hiervoor maken we een nieuwe regel en met de 2 andere waardes precies hetzelfde gebleven

        nieuwe_regel = (datum + ";"+ str(nieuwe_cv_waarde) + ";" + huidige_cv + ";" + huidige_bewatering + "\n")

        #Waarde voor de ventilatie
    elif systeem_aanpassing == "2":

        vent_waarde = input("Nieuwe waarde voor ventilatie, van 0 tot 4: ")

        try:
            nieuwe_vent_waarde = int(vent_waarde)
        except ValueError:
            print("Fout: je moet een geheel getal invoeren.")
            return -3

        # De waarde moet tussen 0 en 4 liggen
        if nieuwe_vent_waarde < 0 or nieuwe_vent_waarde > 4:
            print("Fout: de ventilatiewaarde moet tussen 0 en 4 liggen.")
            return -3

        #Hiervoor maken we een nieuwe regel en met de 2 andere waardes precies hetzelfde gebleven
        nieuwe_regel = (datum + ";" + huidige_cv + ";" + str(nieuwe_vent_waarde) + ";" + huidige_bewatering + "\n")

    elif systeem_aanpassing == "3":

        bewatering_waarde = input("Nieuwe waarde voor bewatering, 0 = uit en 1 = aan: ")

        if bewatering_waarde == "0":
            nieuwe_bewatering_waarde = "False"
        elif bewatering_waarde == "1":
            nieuwe_bewatering_waarde = "True"
        else:
            print("Fout: bewatering moet 0 of 1 zijn.")
            return -3

        #Hiervoor maken we een nieuwe regel en met de 2 andere waardes precies hetzelfde gebleven
        nieuwe_regel = (datum + ";"+  huidige_cv + ";" + huidige_vent + ";" + str(nieuwe_bewatering_waarde) + "\n")


    #Als er geen 1/2/3 wordt gekozen dan een foutmelding geven
    else:
        print("Fout: ongeldige optie gekozen.")
        return -3

    # Oude door nieuwe regels vervangen
    lines[regel_nummer] = nieuwe_regel

    # Alle regels herschrijven naar het nieuwe bestand
    with open(outputFile, "w", encoding="utf-8") as f:
        f.writelines(lines)

    print("Alle aanspassingen zijn opsgeslagen.")
    return 0

def smart_app_controller():

    #Bestand namen doorgeven voor het menu
    invoer_bestand = "SmartApp2.txt"
    uitvoer_bestand = "SmartApp2Out.txt"

    print(
        """
╭─╴╭─╮╭╮╷╶┬╴╭─╮╭─╮╷  ╷  ╭─╴╭─╮   ╭┬╮╭─╴╭╮╷╷ ╷
│  │ ││╰┤ │ ├┬╯│ ││  │  ├╴ ├┬╯   │││├╴ │╰┤│ │
╰─╴╰─╯╵ ╵ ╵ ╵╰╴╰─╯╰─╴╰─╴╰─╴╵╰╴   ╵ ╵╰─╴╵ ╵╰─╯
        """
    )
    print()


    while True:
        print("============================")
        print("1. Aantal dagen weergeven.")
        print("2. Automatisch berekenen.")
        print("3. Waarde overschrijven.")
        print("4. Stoppen.")
        print("============================")

        keuze = input("Wat wilt u doen van de bovenstaande?: ")

        if keuze == "1":
            # Optie 1: Tel aantal dagen en geef het weer
            print("Aantal dagen tellen...")
            aantal = aantal_dagen(invoer_bestand)
            print("Aantal dagen in het bestand:", aantal)

        elif keuze == "2":
            # Optie 2: Bereken alles en geef het weer
            print("Automatisch berekenen...")
            auto_bereken(invoer_bestand, uitvoer_bestand)

        elif keuze == "3":
            # Optie 3: Waarde aanpassen en geef het weer
            print("Waarde overschrijven...")
            resultaat = overwrite_settings(uitvoer_bestand)

            if resultaat == 0:
                print("Alles gelukt!")
            elif resultaat == -1:
                print("Datum niet gevonden.")
            elif resultaat == -3:
                print("Ongeldige invoer.")

        elif keuze == "4":
            # Optie 4: Stoppen met de programma
            print("Tot de volgende keer.")
            break

        else:
            print("Fout: Kies 1, 2, 3 of 4.")

smart_app_controller()