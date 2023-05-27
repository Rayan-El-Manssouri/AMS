from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/ajouter', methods=['GET', 'POST'])
def ajouter():
    if request.method == 'POST':
        # Récupérer les valeurs soumises par le formulaire
        # et les enregistrer dans le fichier texte correspondant
        # à la table ou à l'entité que vous souhaitez modifier.
        # Vous pouvez utiliser la bibliothèque Python 'fileinput'
        # pour faciliter la manipulation des fichiers texte.

        # Rediriger vers une page de confirmation ou de succès
        return render_template('confirmation.html')

    # Générer le formulaire d'ajout en fonction des champs définis
    champs = []

    while True:
        champ = {}
        champ['nom'] = input("Quel est le nom du champ ? ")
        champ['type'] = input("Quel est le type du champ ? ")
        champ['aligne'] = input("Voulez-vous que ce champ soit aligné ? (Oui/Non) ")
        champs.append(champ)

        autre_champ = input("Y a-t-il d'autres champs ? (Oui/Non) ")
        if autre_champ.lower() != 'oui':
            break

    return render_template('ajouter.html', champs=champs)

if __name__ == '__main__':
    app.run()
