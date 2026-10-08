import random

#Het hele deck in een tuple gooien
kaart_catogorie = ['♥', '♠', '♣', '♦']
kaart_nummers = ['Aas', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Boer', 'Vrouw', 'Koning']
deck = [(card, catogorie) for catogorie in kaart_catogorie for card in kaart_nummers]

#de waardes van de kaarten bepalen, en dan vooral de plaatjes kaarten
def kaart_waard(card):
    if card[0] in ['Boer', 'Vrouw', 'Koning']:
        return 10
    elif card[0] in ['Aas']:
        return 11
    else:
        return int(card[0])

def leesbaar_maken(card):
    kaart, soort = card
    return f"{kaart} {soort}"

def kaart_printen(kaarten):
    return ",".join(leesbaar_maken(card) for card in kaarten)

random.shuffle(deck)
player_card = [deck.pop(), deck.pop()]
dealer_card = [deck.pop(), deck.pop()]

print("""

╭╮ ╷  ╭─╮╭─╴╷╭     ╭╮╭─╮╭─╴╷╭ 
├┴╮│  ├─┤│  ├┴╮     │├─┤│  ├┴╮
╰─╯╰─╴╵ ╵╰─╴╵ ╵   ╰─╯╵ ╵╰─╴╵ ╵


    """)
print()
print("=====================")
print("1. Spel starten")
print("2. Uitleg")
print("3. Stoppen")
print("=====================")

while True:
    user_input = input("Wat wilt u doen?: ")

    if user_input == "1":
        while True:
            player_score = sum(kaart_waard(player_card) for player_card in player_card)
            dealer_score = sum(kaart_waard(dealer_card) for dealer_card in dealer_card)

            print("U heeft deze kaarten nu: ", kaart_printen(player_card))
            print("Uw score is", player_score)
            print("De dealer heeft deze kaart en 1 dichte kaart: ", leesbaar_maken(dealer_card[0]), ", [Dichte kaart]")

            speelbeurt = input("Wat wilt u doen? ['hit' om nog een kaart te krijgen, 'stand' om deze selectie te behouden]: ").lower()
            print("==================")

            if speelbeurt == 'stand':
                break

            elif speelbeurt == "hit":
                nieuwe_kaart = deck.pop()
                player_card.append(nieuwe_kaart)

                print("U trekt een", leesbaar_maken(nieuwe_kaart))

                # Score opnieuw berekenen na het trekken van de kaart om te kijken of je 21 of hoger hebt
                player_score = sum(kaart_waard(card) for card in player_card)

                # Meteen stoppen als de speler boven 21 komt
                if player_score > 21:
                    print("Dealer wint. De speler heeft meer dan 21 punten.")
                    break

            else:
                print("Geen valide keuze, kies hit of stand.")



        if player_score <= 21:
            dealer_score = sum(kaart_waard(dealer_card) for dealer_card in dealer_card)
            print("De dichte kaart van de dealer is", leesbaar_maken(dealer_card[1]),)
            print("De dealer heeft een", kaart_printen(dealer_card))
            print("De dealer heeft een score van", dealer_score)

            while dealer_score < 17:
                nieuwe_kaart = deck.pop()
                print("De dealer trekt een:", leesbaar_maken(nieuwe_kaart))
                dealer_card.append(nieuwe_kaart)
                dealer_score += kaart_waard(nieuwe_kaart)
                print("De dealer heeft een score van", dealer_score)

            if dealer_score > 21:
                print("Player wint (Dealer had meer dan 21 punten)")
            elif player_score > dealer_score:
                print("Player wint. (Dealer had minder punten dan player)")
            elif dealer_score > player_score:
                print("Dealer wint (Dealer Has Higher Score than Player)")
            else:
                print("Player en Dealer hebben evenveel punten.")

        print("Kaarten - Player:", kaart_printen(player_card), "Score:", player_score)
        print("Kaarten - Dealer:", kaart_printen(dealer_card), "Score:", dealer_score)

    elif user_input == "2":
        print("""
        
Wat is blackjack?
Dit is een kaartspel dat ook thuis wordt gespeeld. Bedoeling is om met kaarten zo dicht mogelijk bij de 21 punten te komen. 
Blackjack wordt daarom ook wel eenentwintigen genoemd. De plaatjes zijn ieder 10 punten waard, de aas 1 of 11 punten, de overige kaarten hebben hun normale waarde.

De spelers moeten voordat het spel begint hun geld inzetten. Als blackjack thuis wordt gespeeld, gaat het meestal om kleine bedragen. 
In het casino daarentegen bedraagt de minimale inzet 5 euro en de maximale inzet 5.000 euro. Meer kan niet worden ingezet. De inzetten kunnen per speeltafel variëren.
Alleen in dit spel kun je helaas geen geld inzetten omdat dit een simpele black jack code is.

Tegen de bank spelen
Als Black Jack in het casino wordt gespeeld, speelt de speler altijd tegen de bank. Als het thuis wordt gespeeld, zijn spelers om de beurt de bank.
De bank deelt de kaarten uit. Deze worden open op tafel gelegd. Vervolgens krijgt iedere speler een tweede kaart. 
Daarna vraagt de bank of de speler nog een derde kaart wil of dat hij wil passen.

Doel van het spel
De bedoeling is dat de spelers de bank proberen te verslaan, door zo dicht mogelijk of op de 21 punten te komen. 
Is de bank de winnaar dan kost het de speler zijn inzet. Is één of meer spelers de winnaar dan ontvangt hij één keer zijn inzet.
   
        """)
    elif user_input == "3":
        break
    else:
        print("Kies een van de 3 opties hierboven.")