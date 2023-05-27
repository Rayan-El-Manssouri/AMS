from generatejs.generate import generate_ajout_js_file
from display.menu import display_menu

def main():
    print("Bienvenue sur AMS !")
    print("Quelle option souhaitez-vous ?")
    display_menu()

    choix = input("Votre choix : ")

    if choix == "1":
        print("Générer un fichier Ajout.js (adapté pour React)")
        generate_ajout_js_file()
    else:
        print("Choix invalide. Veuillez sélectionner une option valide.")

main()
