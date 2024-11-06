import random

# Functie om een willekeurig woord te kiezen uit een tekstbestand
def kies_woord():
    with open("woorden.txt", "r") as bestand:
        woorden = bestand.readlines()
    # Verwijder eventuele extra witruimtes of newline tekens
    woorden = [woord.strip() for woord in woorden]
    return random.choice(woorden)

# Functie voor het starten van het galgje spel
def start_galgje():
    woord = kies_woord()
    geraden = ['_'] * len(woord)
    verkeerd_geraden = []
    aantal_beurten = 6
    geraden_goed = False

    print("Welkom bij Galgje!")

    while aantal_beurten > 0 and not geraden_goed:
        print(f"woord: {' '.join(geraden)}")
        print(f"Foute letters: {', '.join(verkeerd_geraden)}")
        print(f"Beurten over: {aantal_beurten}")

        gok = input("Raad een letter: ").lower()

        if len(gok) != 1 or not gok.isalpha():
            print("Ongeldige invoer. Probeer opnieuw.")
            continue

        if gok in verkeerd_geraden or gok in geraden:
            print("Je hebt deze letter al geraden!")
            continue

        if gok in woord:
            for i in range(len(woord)):
                if woord[i] == gok:
                    geraden[i] = gok
            if '_' not in geraden:
                geraden_goed = True
        else:
            verkeerd_geraden.append(gok)
            aantal_beurten -= 1

    if geraden_goed:
        print(f"Gefeliciteerd! Je hebt het woord '{woord}' geraden!")
    else:
        print(f"Helaas, je hebt verloren. Het woord was '{woord}'.")

if __name__ == "__main__":
    start_galgje()