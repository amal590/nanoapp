import galgje
import raadhetgetal1

def main_menu():
    while True:
        print("\nkies een spel om te spelen")
        print("1. Galgje")
        print("2. Raadhetgetal1")
        print("3. Stop")

        keuze = input("Maak een keuze (1/2/3): ")
        if keuze == "1":
            galgje.start_galgje()
        elif keuze == "2":
            raadhetgetal1.start_raadhetgetal()
        elif keuze == "3":
            print("tot ziens!")
            break
        else :
            print("Ongeldige invoer, probeeer opnieuw.")

if __name__ == "__main__":
    main_menu()