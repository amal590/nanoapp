import random
# format file : Press Ctrl + Alt + L (Windows/Linux) or Cmd + Option + L (macOS)
# Windows/Linux: Place the cursor on the line you want to delete and press Ctrl + Y.
# macOS: Place the cursor on the line and press Cmd + Delete.
# Windows/Linux: Place the cursor on the line you want to duplicate and press Ctrl + D.
# macOS: Place the cursor on the line and press Cmd + D.

def start_raadhetgetal():
    print("Welkom bij Raad het Nummer!")

    # Speler kiest het getal dat geraden moet worden
    naam = input("Wat is je naam? ")

    gekozen_getal = random.randint(0, 501)


    # Vraag de speler hoeveel kansen hij wil om het getal te raden
    aantal_pogingen = int(input("Hoeveel pogingen wilt u hebben? "))

    # Nu begint het spel
    print(f"Je moet een getal raden tussen de 1 en 500! Je hebt {aantal_pogingen} pogingen.")

    pogingen = 0

    while pogingen < aantal_pogingen:
        geraden_getal = input("Raad het getal: ")

        if geraden_getal.isdigit():
            geraden_getal = int(geraden_getal)
        else:
            print("Ongeldige invoer. Voer een geldig getal in.")
            continue

        pogingen += 1
        print(f"Poging {pogingen} van {aantal_pogingen}")

        if geraden_getal < gekozen_getal:
            print("Te laag!")
        elif geraden_getal > gekozen_getal:
            print("Te hoog!")
        else:
            print(f"Gefeliciteerd! Je hebt het getal {gekozen_getal} geraden in {pogingen} pogingen.")
            break

    if pogingen == aantal_pogingen and geraden_getal != gekozen_getal:
        print(f"Je hebt helaas geen pogingen meer! Het juiste getal was {gekozen_getal}.")


if __name__ == "__main__":
    start_raadhetgetal()
